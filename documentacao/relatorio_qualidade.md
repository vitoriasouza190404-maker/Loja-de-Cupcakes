
# Relatório de Qualidade e Testes
## Loja de Cupcakes — Projeto Integrador II

### 1. Introdução

Este relatório tem como objetivo apresentar a avaliação da qualidade do sistema Loja de Cupcakes, desenvolvido como parte do Projeto Integrador Transdisciplinar em Engenharia de Software II.

O sistema permite consultar produtos, utilizar um carrinho de compras, cadastrar clientes, realizar login, registrar pedidos com pagamento simulado e acompanhar o histórico de compras.

Também possui um painel administrativo para visualizar pedidos e atualizar seus status.

### 2. Objetivos dos testes

- Verificar o funcionamento das funcionalidades.
- Avaliar a facilidade de utilização do sistema.
- Identificar erros e dificuldades.
- Registrar sugestões dos participantes.
- Propor melhorias com base nos resultados.

### 3. Ambiente de testes

- Linguagem: Python
- Framework: Flask
- Banco de dados: SQLite
- Front-end: HTML, CSS e JavaScript
- Navegador: [preencher]
- Sistema operacional: [preencher]
- Data dos testes: [preencher]

### 4. Metodologia

A avaliação será realizada com cinco participantes, identificados como P01, P02, P03, P04 e P05.

Cada participante deverá executar as tarefas descritas no documento avaliacao_usuarios.md.

Após a execução, responderá ao questionário de usabilidade com notas de 1 a 5 e perguntas abertas.

### 5. Resultados dos testes funcionais

| Finalização de pedidos | Aprovado | Pedido #2 registrado com Pix e total de R$ 12,00 |
| Histórico de compras | Aprovado | Pedido #2 exibido corretamente |
| Painel administrativo | Aprovado | Pedido #2 visível para o administrador |
| Atualização do status | Aprovado | Status Em preparo permaneceu após F5 |
| Controle de acesso administrativo | Aprovado | Cliente autenticado recebeu acesso negado (HTTP 403) ao acessar /admin |

### 6. Resultados dos cinco participantes

| Participante | Resultado | Sugestões de melhoria |
|---|---|---|
| P01 - Daniel | Teste realizado | Confirmação e alteração de senha; personalização de produtos |
| P02 - Hosana | Teste realizado | Não sugeriu melhorias |
| P03 - Braz | Teste realizado | Login automático após cadastro e mensagens de validação |
| P04 - Douglas | Teste realizado | Confirmação visual no carrinho e verificação da persistência dos itens |
| P05 - Ana | Teste realizado | Confirmação mais detalhada após finalizar o pedido |

Os cinco participantes realizaram avaliações em 31/10/2026.

Os relatos indicaram uma percepção positiva da facilidade de uso
e do funcionamento das funcionalidades avaliadas.

Não foram relatados erros impeditivos durante os testes.
As sugestões serão consideradas no planejamento de melhorias.

### 7. Indicadores de qualidade

Após a realização dos testes, calcular:

**Taxa de conclusão das tarefas**

(Total de tarefas concluídas / Total de tarefas propostas) × 100

**Média de satisfação**

Soma das notas obtidas / Quantidade de respostas

**Quantidade de problemas**

Número total de problemas distintos identificados durante os testes.

### 8. Problemas encontrados e melhorias

### 8. Problemas encontrados e melhorias

| Problema ou oportunidade | Melhoria proposta | Situação |
|---|---|---|
| Cadastro sem confirmação de senha | Adicionar confirmação de senha | Implementado e testado|
| Ausência de alteração de senha | Permitir alteração de senha | Planejado |
| Login necessário após cadastro | Autenticar automaticamente após cadastro | Implementado e testado |
| Mensagens de validação pouco claras | Melhorar orientações ao usuário | Implementado e testado |
| Ausência de confirmação visual no carrinho | Exibir mensagem ao adicionar produtos | Planejado |
| Persistência do carrinho não avaliada | Realizar teste específico | Pendente |
| Confirmação de compra pouco detalhada | Exibir informações do pedido finalizado | Planejado |
| Personalização e agendamento | Avaliar implementação futura | Versão futura |

### 9. Evidências

Inserir capturas de tela ou registros dos testes realizados.

Exemplos:

- Cadastro e login.
- Carrinho de compras.
- Confirmação de pedido.
- Histórico de compras.
- Painel administrativo.
- Formulários de avaliação preenchidos.

Evitar incluir senhas ou dados pessoais dos participantes nas evidências.

### 10. Conclusão

[A preencher após os testes.]

Apresentar os resultados observados, os principais problemas encontrados, as melhorias realizadas e uma avaliação final da qualidade do sistema.
