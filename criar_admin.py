
import getpass
import sqlite3

from werkzeug.security import generate_password_hash
from app import conectar_banco, criar_banco


def criar_administrador():
    criar_banco()

    nome = input("Nome do administrador: ").strip()
    email = input("E-mail do administrador: ").strip().lower()
    senha = getpass.getpass("Senha (mínimo 8 caracteres): ")

    if not nome or "@" not in email or len(senha) < 8:
        print("Dados inválidos. Verifique nome, e-mail e senha.")
        return

    try:
        with conectar_banco() as conexao:
            conexao.execute(
                """INSERT INTO usuarios (nome, email, senha, tipo)
                   VALUES (?, ?, ?, 'admin')""",
                (nome, email, generate_password_hash(senha))
            )

        print("Administrador criado com sucesso!")

    except sqlite3.IntegrityError:
        print("Este e-mail já está cadastrado. Use outro e-mail.")


if __name__ == "__main__":
    criar_administrador()
