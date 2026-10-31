
# Plano de Testes Funcionais — Loja de Cupcakes

## 1. Objetivo

Verificar o funcionamento das principais funcionalidades do sistema Loja de Cupcakes, identificando possíveis erros e oportunidades de melhoria.

## 2. Ambiente de testes

- Aplicação web desenvolvida em Python e Flask
- Banco de dados SQLite
- Interface HTML, CSS e JavaScript
- Execução local em http://127.0.0.1:5000
- Navegador web

## 3. Casos de teste

| ID | Funcionalidade | Procedimento | Resultado esperado |
|---|---|---|---|
| CT01 | Cadastro | Cadastrar cliente com dados válidos | Conta criada com sucesso |
| CT02 | Cadastro duplicado | Cadastrar e-mail já existente | Exibir mensagem de erro |
| CT03 | Login | Entrar com credenciais corretas | Usuário autenticado |
| CT04 | Login inválido | Informar senha incorreta | Impedir acesso |
| CT05 | Catálogo | Acessar a página inicial | Exibir produtos e preços |
| CT06 | Carrinho | Adicionar cupcakes | Atualizar itens e total |
| CT07 | Quantidades | Utilizar botões + e - | Atualizar quantidades e valores |
| CT08 | Remoção | Remover um produto | Recalcular total |
| CT09 | Finalização | Finalizar pedido autenticado | Registrar pedido no banco |
| CT10 | Acesso não autenticado | Tentar finalizar sem login | Solicitar autenticação |
| CT11 | Histórico | Acessar Meus Pedidos | Exibir pedidos do cliente |
| CT12 | Administração | Entrar como administrador | Abrir painel administrativo |
| CT13 | Gerenciamento | Alterar status de um pedido | Salvar novo status |
| CT14 | Segurança | Cliente tentar acessar painel administrativo | Bloquear acesso |

## 4. Registro dos resultados

Para cada teste, registrar:

- Data da execução
- Identificação do testador
- Resultado: aprovado ou reprovado
- Descrição do erro, caso exista
- Evidência, como captura de tela

## 5. Testes com usuários

O sistema será avaliado por cinco participantes.

Cada participante deverá executar tarefas como:

1. Acessar o catálogo.
2. Criar uma conta ou entrar no sistema.
3. Adicionar produtos ao carrinho.
4. Alterar quantidades.
5. Finalizar uma compra simulada.
6. Consultar o histórico de pedidos.

Ao final, o participante deverá avaliar a facilidade de uso, a clareza das informações e possíveis problemas encontrados.

## 6. Critérios de aprovação

Um caso de teste será considerado aprovado quando o resultado observado corresponder ao resultado esperado.

Os problemas encontrados deverão ser registrados e corrigidos, quando possível, antes da entrega final.
