
# Relatório de Qualidade e Testes
## Loja de Cupcakes — Projeto Integrador II

### 1. Introdução

Este relatório apresenta a avaliação da qualidade do sistema
Loja de Cupcakes, desenvolvido como parte do Projeto Integrador
Transdisciplinar em Engenharia de Software II.

O sistema permite consultar produtos, utilizar um carrinho de
compras, cadastrar clientes, realizar login, registrar pedidos
com pagamento simulado e acompanhar o histórico de compras.

Também possui um painel administrativo para visualizar pedidos
e atualizar seus status.

### 2. Objetivos dos testes

- Verificar o funcionamento das funcionalidades.
- Avaliar a facilidade de utilização do sistema.
- Identificar erros e dificuldades.
- Registrar sugestões dos participantes.
- Propor e implementar melhorias com base nos resultados.

### 3. Ambiente de testes

- Linguagem: Python
- Framework: Flask
- Banco de dados: SQLite
- Front-end: HTML, CSS e JavaScript
- Ambiente de desenvolvimento: Visual Studio Code
- Execução: servidor local Flask
- Data dos testes com participantes: 31/10/2026
- Quantidade de participantes: 5

### 4. Metodologia

A avaliação do sistema foi realizada com cinco participantes,
identificados como P01, P02, P03, P04 e P05.

Os participantes utilizaram funcionalidades da Loja de Cupcakes
e relataram suas percepções sobre facilidade de uso,
funcionamento e oportunidades de melhoria.

Os resultados foram registrados individualmente e analisados
para identificar melhorias prioritárias.

Além das avaliações dos participantes, foram realizados testes
funcionais para verificar o registro de pedidos, o histórico
de compras, o painel administrativo, a atualização do status
dos pedidos e o controle de acesso.

Após a análise dos feedbacks, foram implementadas melhorias
no cadastro de clientes e realizados testes de validação.

### 5. Resultados dos testes funcionais

| Funcionalidade | Resultado | Evidência |
|---|---|---|
| Finalização de pedidos | Aprovado | Pedido #2 registrado com Pix e total de R$ 12,00 |
| Histórico de compras | Aprovado | Pedido #2 exibido corretamente |
| Painel administrativo | Aprovado | Pedido #2 visível para o administrador |
| Atualização do status | Aprovado | Status Em preparo permaneceu após F5 |
| Controle de acesso administrativo | Aprovado | Cliente autenticado recebeu HTTP 403 ao acessar /admin |

### 6. Resultados dos cinco participantes

| Participante | Resultado | Sugestões de melhoria |
|---|---|---|
| P01 - Daniel | Teste realizado | Confirmação e alteração de senha; personalização de produtos |
| P02 - Hosana | Teste realizado | Não sugeriu melhorias |
| P03 - Braz | Teste realizado | Login automático após cadastro e mensagens de validação |
| P04 - Douglas | Teste realizado | Confirmação visual no carrinho e verificação da persistência dos itens |
| P05 - Ana | Teste realizado | Confirmação mais detalhada após finalizar o pedido |

Os cinco participantes realizaram avaliações em 31/10/2026.

Os relatos indicaram uma percepção positiva da facilidade
de uso e do funcionamento das funcionalidades avaliadas.

Não foram relatados erros impeditivos durante os testes.
As sugestões foram consideradas no planejamento de melhorias.

### 7. Indicadores de qualidade

- Participantes que realizaram os testes: 5.
- Falhas impeditivas relatadas: nenhuma.
- Melhorias implementadas após os feedbacks: 3.
- Funcionalidades verificadas nos testes funcionais:
  finalização de pedidos, histórico de compras, painel
  administrativo, atualização de status e controle de acesso.

A avaliação dos participantes foi qualitativa.
Por esse motivo, não foram calculadas médias numéricas
de satisfação ou taxas de conclusão de tarefas.

### 8. Problemas encontrados e melhorias

| Problema ou oportunidade | Melhoria proposta | Situação |
|---|---|---|
| Cadastro sem confirmação de senha | Adicionar confirmação de senha | Implementado e testado |
| Ausência de alteração de senha | Permitir alteração de senha | Planejado |
| Login necessário após cadastro | Autenticar automaticamente após cadastro | Implementado e testado |
| Mensagens de validação pouco claras | Melhorar orientações ao usuário | Implementado e testado |
| Ausência de confirmação visual no carrinho | Exibir mensagem ao adicionar produtos | Planejado |
| Persistência do carrinho não avaliada | Realizar teste específico | Pendente |
| Confirmação de compra pouco detalhada | Exibir informações do pedido finalizado | Planejado |
| Personalização e agendamento | Avaliar implementação futura | Versão futura |

### 9. Evidências

Foram registradas evidências dos testes funcionais e das
melhorias implementadas no sistema.

As evidências incluem:

- Formulário de cadastro com confirmação de senha.
- Mensagem de validação para senhas divergentes.
- Autenticação automática após cadastro.
- Carrinho de compras.
- Histórico de pedidos.
- Painel administrativo.
- Atualização do status de pedidos.
- Bloqueio de acesso não autorizado ao painel administrativo.

As capturas de tela selecionadas serão apresentadas
no relatório acadêmico, preservando os dados pessoais.

### 10. Conclusão

O sistema Loja de Cupcakes apresentou resultados satisfatórios
nos testes funcionais e nas avaliações realizadas com cinco
participantes.

Não foram relatadas falhas impeditivas nas funcionalidades
avaliadas. Os feedbacks permitiram identificar oportunidades
de melhoria na experiência do usuário.

Com base nas avaliações, foram implementadas três melhorias:
confirmação de senha no cadastro, mensagens de validação
mais claras e autenticação automática após a criação da conta.

As alterações foram testadas e apresentaram o comportamento
esperado. As demais sugestões foram registradas para
avaliação em versões futuras.

Conclui-se que o sistema atende aos principais objetivos
funcionais definidos para esta etapa do projeto, mantendo
oportunidades de evolução contínua.
