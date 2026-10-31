
# Diagrama do Banco de Dados — Loja de Cupcakes

```mermaid
erDiagram
    usuarios ||--o{ pedidos : realiza
    pedidos ||--o{ itens_pedido : contem

    usuarios {
        INTEGER id PK
        TEXT nome
        TEXT email UK
        TEXT senha
        TEXT tipo
        TIMESTAMP criado_em
    }

    pedidos {
        INTEGER id PK
        INTEGER usuario_id FK
        INTEGER total_centavos
        TEXT forma_pagamento
        TEXT status
        TIMESTAMP criado_em
    }

    itens_pedido {
        INTEGER id PK
        INTEGER pedido_id FK
        TEXT produto_id
        TEXT nome_produto
        INTEGER quantidade
        INTEGER preco_unitario_centavos
    }
```

## Descrição dos relacionamentos

- Um usuário pode realizar vários pedidos (1:N).
- Um pedido pertence a um único usuário.
- Um pedido pode conter vários itens (1:N).
- Cada item pertence a um único pedido.
