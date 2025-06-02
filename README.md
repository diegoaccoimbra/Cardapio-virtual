# 📄 Cardápio Virtual

## 📝 Descrição
O projeto consiste numa aplicação que permite o cadastro, visualização, edição, exclusão e exportação de pedidos para um arquivo PDF. 

---

## 🛠️ Ferramentas utilizadas
- Linguagem Python;
- Biblioteca PyQt5 para a interface gráfica;
- MySQL para gerenciamento de dados;
- ReportLab para geração do PDF com a lista de pedidos.

---

## ⚙️ Funcionalidades

- 📥 **Cadastrar pedidos:** insira código, descrição, preço e categoria.
- 📋 **Listar pedidos:** visualize todos os registros armazenados em uma tabela.
- 🗑️ **Excluir pedidos:** remova qualquer pedido do banco de dados com um clique.
- ✏️ **Editar pedidos:** altere os dados de pedidos existentes.
- 📄 **Gerar PDF:** exporte a lista de pedidos para um arquivo PDF formatado.

---

## 💻 Estrutura das Telas

- `formulario.ui`: Tela principal de cadastro.
- `listar_pedidos.ui`: Tela com listagem de todos os pedidos.
- `menu_editar.ui`: Tela para editar um pedido selecionado.

---

## 🗃️ Banco de Dados

A tabela utilizada é `tbl_pedidos` com os seguintes campos:

| Campo     | Tipo      |
|-----------|-----------|
| ID        | INT (PK)  |
| código    | VARCHAR   |
| descrição | VARCHAR   |
| preço     | FLOAT ou VARCHAR |
| categoria | VARCHAR   |

---

## 🧠 Como funciona

1. **Tela de Cadastro:**
   - O usuário insere o código, descrição, preço e escolhe a categoria (Bebida, Lanche ou Sobremesa).
   - Ao clicar em "Cadastrar", os dados são armazenados no banco.

2. **Listagem:**
   - A tela mostra todos os pedidos cadastrados em uma tabela.
   - É possível editar ou excluir pedidos diretamente dessa interface.

3. **Edição:**
   - Carrega os dados do pedido selecionado para a tela de edição.
   - O usuário altera e salva, atualizando os dados no banco.

4. **Geração de PDF:**
   - Cria um arquivo chamado `cadastro_pedidos.pdf` com todos os pedidos formatados.
  
