
const produtos = {
    chocolate: {
        nome: "Cupcake de Chocolate",
        preco: 12.00
    },
    morango: {
        nome: "Cupcake de Morango",
        preco: 14.00
    },
    baunilha: {
        nome: "Cupcake de Baunilha",
        preco: 11.00
    }
};

const CHAVE_CARRINHO = "loja_cupcakes_carrinho";

function carregarCarrinho() {
    try {
        const salvo = JSON.parse(localStorage.getItem(CHAVE_CARRINHO));

        if (!salvo || typeof salvo !== "object" || Array.isArray(salvo)) {
            return {};
        }

        const carrinhoValidado = {};

        for (const id of Object.keys(produtos)) {
            const quantidade = salvo[id];

            if (Number.isSafeInteger(quantidade) && quantidade > 0) {
                carrinhoValidado[id] = quantidade;
            }
        }

        return carrinhoValidado;
    } catch {
        return {};
    }
}

let carrinho = carregarCarrinho();

function formatarMoeda(valor) {
    return valor.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
    });
}

function salvarCarrinho() {
    localStorage.setItem(CHAVE_CARRINHO, JSON.stringify(carrinho));
}

function adicionarAoCarrinho(id) {
    if (!produtos[id]) return;

    carrinho[id] = (carrinho[id] || 0) + 1;

    salvarCarrinho();
    atualizarCarrinho();
}

function alterarQuantidade(id, variacao) {
    if (!produtos[id] || !carrinho[id]) return;

    const novaQuantidade = carrinho[id] + variacao;

    if (novaQuantidade <= 0) {
        delete carrinho[id];
    } else {
        carrinho[id] = novaQuantidade;
    }

    salvarCarrinho();
    atualizarCarrinho();
}

function removerProduto(id) {
    delete carrinho[id];

    salvarCarrinho();
    atualizarCarrinho();
}

function limparCarrinho() {
    carrinho = {};

    salvarCarrinho();
    atualizarCarrinho();
}

function atualizarCarrinho() {
    const lista = document.getElementById("itens-carrinho");
    const totalElemento = document.getElementById("total-carrinho");
    const mensagemVazia = document.getElementById("carrinho-vazio");
    const botaoLimpar = document.getElementById("limpar-carrinho");

    lista.innerHTML = "";

    let total = 0;
    const ids = Object.keys(carrinho);

    mensagemVazia.hidden = ids.length > 0;
    botaoLimpar.hidden = ids.length === 0;

    ids.forEach(id => {
        const produto = produtos[id];
        const quantidade = carrinho[id];
        const subtotal = produto.preco * quantidade;

        total += subtotal;

        const item = document.createElement("li");
        item.className = "item-carrinho";

        const descricao = document.createElement("span");
        descricao.textContent = `${produto.nome} — ${formatarMoeda(subtotal)}`;

        const controles = document.createElement("div");
        controles.className = "controles-quantidade";

        const diminuir = document.createElement("button");
        diminuir.textContent = "−";
        diminuir.setAttribute("aria-label", `Diminuir ${produto.nome}`);
        diminuir.onclick = () => alterarQuantidade(id, -1);

        const contador = document.createElement("span");
        contador.textContent = quantidade;

        const aumentar = document.createElement("button");
        aumentar.textContent = "+";
        aumentar.setAttribute("aria-label", `Aumentar ${produto.nome}`);
        aumentar.onclick = () => alterarQuantidade(id, 1);

        const remover = document.createElement("button");
        remover.textContent = "Remover";
        remover.onclick = () => removerProduto(id);

        controles.append(diminuir, contador, aumentar, remover);
        item.append(descricao, controles);
        lista.appendChild(item);
    });

    totalElemento.textContent = formatarMoeda(total);
}

document.addEventListener("DOMContentLoaded", atualizarCarrinho);

async function finalizarCompra() {
    const pagamento = document.getElementById("forma-pagamento").value;
    const mensagem = document.getElementById("mensagem-pedido");

    mensagem.textContent = "Registrando seu pedido...";

    try {
        const resposta = await fetch("/finalizar-pedido", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                itens: carrinho,
                pagamento: pagamento
            })
        });

        const dados = await resposta.json();

        if (!resposta.ok) {
            mensagem.textContent = dados.erro || "Não foi possível finalizar.";

            if (resposta.status === 401) {
                mensagem.textContent += " Acesse Entrar para continuar.";
            }
            return;
        }

        carrinho = {};
        salvarCarrinho();
        atualizarCarrinho();

        mensagem.textContent =
            `Pedido #${dados.pedido_id} confirmado! Pagamento simulado.`;

    } catch (erro) {
        mensagem.textContent = "Erro de conexão. Tente novamente.";
    }
}

const atualizarCarrinhoOriginal = atualizarCarrinho;

atualizarCarrinho = function () {
    atualizarCarrinhoOriginal();

    const area = document.getElementById("area-checkout");

    if (area) {
        area.hidden = Object.keys(carrinho).length === 0;
    }
};

document.addEventListener("DOMContentLoaded", atualizarCarrinho);
