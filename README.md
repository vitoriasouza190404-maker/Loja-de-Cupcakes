
# 🧁 Loja de Cupcakes

## Projeto Integrador Transdisciplinar em Engenharia de Software II

Sistema web desenvolvido para simular o funcionamento de uma loja virtual de cupcakes gourmet.

O projeto contempla levantamento de requisitos, modelagem de banco de dados, desenvolvimento front-end e back-end, autenticação de usuários, gerenciamento de pedidos, testes de software e documentação técnica.

## Objetivo

Desenvolver uma aplicação web que permita aos clientes consultar produtos, realizar pedidos com pagamentos simulados e acompanhar o histórico de compras.

O sistema também oferece funcionalidades administrativas para acompanhamento e gerenciamento dos pedidos.

## Funcionalidades

### Área do cliente

- Visualização do catálogo de cupcakes.
- Carrinho de compras com inclusão e remoção de produtos.
- Alteração da quantidade de produtos no carrinho.
- Cálculo automático do valor total.
- Cadastro de clientes com confirmação de senha.
- Validação de dados no formulário de cadastro.
- Login automático após a criação da conta.
- Login e logout de usuários.
- Finalização de pedidos com pagamento simulado.
- Consulta ao histórico de pedidos.

### Área administrativa

- Acesso restrito a usuários administradores.
- Visualização dos pedidos realizados.
- Consulta aos detalhes dos pedidos.
- Acompanhamento dos valores das vendas.
- Atualização do status dos pedidos.

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Visual Studio Code
- Git e GitHub

## Estrutura do projeto

```text
Loja-de-Cupcakes/
├── app.py
├── criar_admin.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── index.html
│   ├── cadastro.html
│   ├── login.html
│   ├── pedidos.html
│   └── admin.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── documentacao/
    ├── avaliacao_usuarios.md
    ├── dicionario_de_dados.md
    ├── diagrama_banco.md
    ├── plano_de_testes.md
    └── relatorio_qualidade.md
```

## Como executar o projeto

### 1. Baixar o repositório

Clone o projeto ou baixe os arquivos pelo GitHub.

### 2. Criar o ambiente virtual

No terminal, dentro da pasta do projeto:

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
python app.py
```

### 6. Acessar no navegador

Abra:

http://127.0.0.1:5000

O banco de dados SQLite é utilizado para armazenar usuários, pedidos e itens dos pedidos.

As funcionalidades administrativas exigem uma conta com perfil de administrador, configurada separadamente no ambiente local.

## Testes e avaliação de qualidade

O sistema foi avaliado por cinco participantes em 31/10/2026.

Os testes envolveram funcionalidades de cadastro, navegação, carrinho de compras, finalização de pedidos e consulta ao histórico.

Também foram realizados testes funcionais no painel administrativo, incluindo atualização de status e restrição de acesso.

Os participantes relataram uma experiência positiva de utilização e apresentaram sugestões para aprimorar o sistema.

### Melhorias implementadas

Com base nos feedbacks recebidos, foram realizadas três melhorias:

1. Inclusão do campo de confirmação de senha.
2. Aprimoramento das mensagens de validação do cadastro.
3. Autenticação automática após a criação da conta.

As alterações foram testadas após a implementação.

### Melhorias futuras

- Alteração de senha pelo cliente.
- Personalização dos cupcakes.
- Agendamento de pedidos.
- Confirmação visual ao adicionar produtos ao carrinho.
- Confirmação de compra mais detalhada.
- Avaliações dos produtos.
- Possibilidade de parcelamento.

## Documentação

Os arquivos da pasta `documentacao` apresentam:

- Avaliação dos usuários.
- Dicionário de dados.
- Diagrama do banco de dados.
- Plano de testes.
- Relatório de qualidade e melhorias.

## Observações

Este sistema foi desenvolvido para fins acadêmicos.

As formas de pagamento são simuladas. Não existe integração com serviços de pagamento reais.

O projeto utiliza um banco de dados local, que não é publicado no repositório para preservar as informações armazenadas.

## Status do projeto

**Protótipo funcional desenvolvido e testado, com melhorias implementadas após avaliação dos usuários.**
