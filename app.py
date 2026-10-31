
import os
import sqlite3
from pathlib import Path
from functools import wraps

from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash, jsonify, abort
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY", "chave-local-apenas-para-desenvolvimento"
)

BANCO = Path(__file__).resolve().parent / "loja.db"

PRODUTOS = {
    "chocolate": ("Cupcake de Chocolate", 1200),
    "morango": ("Cupcake de Morango", 1400),
    "baunilha": ("Cupcake de Baunilha", 1100)
}

PAGAMENTOS = {"pix", "cartao", "dinheiro"}
STATUS_PEDIDOS = {
    "Confirmado",
    "Em preparo",
    "Saiu para entrega",
    "Entregue",
    "Cancelado"
}


def conectar_banco():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_banco():
    with conectar_banco() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                total_centavos INTEGER NOT NULL,
                forma_pagamento TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Confirmado',
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        """)

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS itens_pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido_id INTEGER NOT NULL,
                produto_id TEXT NOT NULL,
                nome_produto TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco_unitario_centavos INTEGER NOT NULL,
                FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
            )
        """)

        # Atualiza o banco existente sem apagar os clientes.
        colunas = [
            coluna["name"]
            for coluna in conexao.execute("PRAGMA table_info(usuarios)")
        ]

        if "tipo" not in colunas:
            conexao.execute("""
                ALTER TABLE usuarios
                ADD COLUMN tipo TEXT NOT NULL DEFAULT 'cliente'
            """)


def administrador_obrigatorio(funcao):
    @wraps(funcao)
    def verificar(*args, **kwargs):
        usuario_id = session.get("usuario_id")

        if not usuario_id:
            flash("Faça login para acessar esta página.")
            return redirect(url_for("login"))

        with conectar_banco() as conexao:
            usuario = conexao.execute(
                "SELECT tipo FROM usuarios WHERE id = ?",
                (usuario_id,)
            ).fetchone()

        if not usuario or usuario["tipo"] != "admin":
            abort(403)

        return funcao(*args, **kwargs)

    return verificar


@app.route("/")
def pagina_inicial():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        if not nome or not email or len(senha) < 8:
            flash("Preencha os dados e use uma senha de pelo menos 8 caracteres.")
            return render_template("cadastro.html")

        senha_protegida = generate_password_hash(senha)

        try:
            with conectar_banco() as conexao:
                conexao.execute(
                    """INSERT INTO usuarios (nome, email, senha, tipo)
                       VALUES (?, ?, ?, 'cliente')""",
                    (nome, email, senha_protegida)
                )
        except sqlite3.IntegrityError:
            flash("Este e-mail já está cadastrado.")
            return render_template("cadastro.html")

        flash("Cadastro realizado com sucesso! Faça seu login.")
        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        with conectar_banco() as conexao:
            usuario = conexao.execute(
                "SELECT * FROM usuarios WHERE email = ?",
                (email,)
            ).fetchone()

        if usuario and check_password_hash(usuario["senha"], senha):
            session.clear()
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            session["usuario_tipo"] = usuario["tipo"]

            if usuario["tipo"] == "admin":
                return redirect(url_for("painel_admin"))

            return redirect(url_for("pagina_inicial"))

        flash("E-mail ou senha incorretos.")

    return render_template("login.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Você saiu da sua conta.")
    return redirect(url_for("login"))


@app.route("/finalizar-pedido", methods=["POST"])
def finalizar_pedido():
    if "usuario_id" not in session:
        return jsonify({
            "erro": "Faça login para finalizar a compra.",
            "login": url_for("login")
        }), 401

    if session.get("usuario_tipo") == "admin":
        return jsonify({
            "erro": "Administradores não podem realizar compras."
        }), 403

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Dados inválidos."}), 400

    itens = dados.get("itens")
    pagamento = dados.get("pagamento")

    if not isinstance(itens, dict) or not itens:
        return jsonify({"erro": "Carrinho vazio ou inválido."}), 400

    if pagamento not in PAGAMENTOS:
        return jsonify({"erro": "Forma de pagamento inválida."}), 400

    total = 0
    itens_validados = []

    for produto_id, quantidade in itens.items():
        if produto_id not in PRODUTOS:
            return jsonify({"erro": "Produto inválido."}), 400

        if type(quantidade) is not int or not 1 <= quantidade <= 100:
            return jsonify({"erro": "Quantidade inválida."}), 400

        nome, preco = PRODUTOS[produto_id]
        total += preco * quantidade
        itens_validados.append((produto_id, nome, quantidade, preco))

    with conectar_banco() as conexao:
        cursor = conexao.execute(
            """INSERT INTO pedidos
               (usuario_id, total_centavos, forma_pagamento)
               VALUES (?, ?, ?)""",
            (session["usuario_id"], total, pagamento)
        )

        pedido_id = cursor.lastrowid

        conexao.executemany(
            """INSERT INTO itens_pedido
               (pedido_id, produto_id, nome_produto,
                quantidade, preco_unitario_centavos)
               VALUES (?, ?, ?, ?, ?)""",
            [
                (pedido_id, produto_id, nome, quantidade, preco)
                for produto_id, nome, quantidade, preco in itens_validados
            ]
        )

    return jsonify({
        "mensagem": "Pedido registrado com sucesso!",
        "pedido_id": pedido_id,
        "total": total / 100
    }), 201


@app.route("/meus-pedidos")
def meus_pedidos():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    with conectar_banco() as conexao:
        pedidos = conexao.execute(
            """SELECT * FROM pedidos
               WHERE usuario_id = ?
               ORDER BY id DESC""",
            (session["usuario_id"],)
        ).fetchall()

    return render_template("pedidos.html", pedidos=pedidos)


@app.route("/admin")
@administrador_obrigatorio
def painel_admin():
    with conectar_banco() as conexao:
        pedidos = conexao.execute("""
            SELECT
                p.id,
                p.total_centavos,
                p.forma_pagamento,
                p.status,
                p.criado_em,
                u.nome AS cliente_nome,
                u.email AS cliente_email
            FROM pedidos p
            JOIN usuarios u ON u.id = p.usuario_id
            ORDER BY p.id DESC
        """).fetchall()

        itens = conexao.execute("""
            SELECT pedido_id, nome_produto, quantidade
            FROM itens_pedido
            ORDER BY id
        """).fetchall()

    itens_por_pedido = {}

    for item in itens:
        itens_por_pedido.setdefault(item["pedido_id"], []).append(item)

    total_vendas = sum(
        pedido["total_centavos"]
        for pedido in pedidos
        if pedido["status"] != "Cancelado"
    )

    return render_template(
        "admin.html",
        pedidos=pedidos,
        itens_por_pedido=itens_por_pedido,
        total_vendas=total_vendas,
        status_disponiveis=STATUS_PEDIDOS
    )


@app.route("/admin/pedido/<int:pedido_id>/status", methods=["POST"])
@administrador_obrigatorio
def atualizar_status(pedido_id):
    novo_status = request.form.get("status", "")

    if novo_status not in STATUS_PEDIDOS:
        abort(400)

    with conectar_banco() as conexao:
        cursor = conexao.execute(
            "UPDATE pedidos SET status = ? WHERE id = ?",
            (novo_status, pedido_id)
        )

        if cursor.rowcount == 0:
            abort(404)

    flash(f"Status do pedido #{pedido_id} atualizado!")
    return redirect(url_for("painel_admin"))


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
