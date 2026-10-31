
# Dicionário de Dados — Loja de Cupcakes

## 1. Objetivo

Documentar a estrutura do banco de dados utilizado no sistema Loja de Cupcakes, desenvolvido para o Projeto Integrador Transdisciplinar em Engenharia de Software II.

## 2. Tecnologias

- Banco de dados: SQLite
- Linguagem de programação: Python
- Framework: Flask
- Arquivo local do banco: loja.db

## 3. Tabela: usuarios

Armazena os dados de cadastro e autenticação dos usuários.

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único do usuário |
| nome | TEXT | Nome completo |
| email | TEXT | E-mail único |
| senha | TEXT | Hash da senha |
| tipo | TEXT | Perfil de acesso: cliente ou administrador |
| criado_em | TIMESTAMP | Data de criação do cadastro |

## 4. Tabela: pedidos

Armazena as compras realizadas pelos clientes.

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único do pedido |
| usuario_id | INTEGER | Identificador do cliente |
| total_centavos | INTEGER | Valor total em centavos |
| forma_pagamento | TEXT | Forma de pagamento simulada |
| status | TEXT | Situação atual do pedido |
| criado_em | TIMESTAMP | Data de criação do pedido |

## 5. Tabela: itens_pedido

Armazena os produtos associados a cada pedido.

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único do item |
| pedido_id | INTEGER | Identificador do pedido |
| produto_id | TEXT | Código do produto |
| nome_produto | TEXT | Nome do cupcake |
| quantidade | INTEGER | Quantidade comprada |
| preco_unitario_centavos | INTEGER | Preço unitário em centavos |

## 6. Relacionamentos

- Um usuário pode realizar vários pedidos.
- Cada pedido pertence a um usuário.
- Um pedido pode conter vários itens.
- Cada item pertence a um pedido.

## 7. Regras de negócio

- O e-mail do usuário deve ser único.
- As senhas são armazenadas como hashes.
- Apenas usuários autenticados podem finalizar compras.
- Os valores monetários são armazenados em centavos.
- O pagamento é simulado, sem transações financeiras reais.
- O administrador pode consultar os pedidos e atualizar seus status.
