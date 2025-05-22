from PyQt5 import uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

#Variável global que vai ser acessada por outras funções#

numero_id = 0


#Criação da instância banco, com os dados do servidor do banco de dados#

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sql1107",
    database="db_produtos"
)

#Para fazer a exclusão se utiliza o objeto segunda_tela com o elemento tableWidget e método cuurentRow() salvos na variável linha que corresponde a linha clicada na interface para a exclusão | o método removeRow é utlizado para a exclusão da linha, passando para ele o parâmetro da linha que deseja-se eliminar, que no caso é a variável linha | É dado um SELECT pra ler os dados do banco de dados, mas retornar só o ID, assim todos os ID são pegos e salvos em dados_lidos | valor_id vai pegar a posição que se deseja excluir em dado_lidos, que é a posição armazenada em linha | em seguida é executado o comando sql para a exclusão da linha#

def excluir_item():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT ID FROM tbl_pedidos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM tbl_pedidos WHERE ID=" + str(valor_id))


#Segue praticamente a mesma lógica da função anterior | A variável pedido é onde os valores do item selecionado serão salvos#

def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT ID FROM tbl_pedidos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM tbl_pedidos WHERE ID=" + str(valor_id))
    pedido = cursor.fetchall()
    tela_editar.show()

#A variável global numero_id vai receber o valor ID que foi pego acima#

    numero_id = valor_id

    tela_editar.lineEdit.setText(str(pedido[0][0]))
    tela_editar.lineEdit_2.setText(str(pedido[0][1]))
    tela_editar.lineEdit_3.setText(str(pedido[0][2]))
    tela_editar.lineEdit_4.setText(str(pedido[0][3]))
    tela_editar.lineEdit_5.setText(str(pedido[0][4]))

#Aqui vai pegar o que o usuário digitou em cada campo na tela de editar utilizando o método .text()#

def salvar_dados_editados():
    global numero_id
    codigo = tela_editar.lineEdit_2.text()
    descricao = tela_editar.lineEdit_3.text()
    preco = tela_editar.lineEdit_4.text()
    categoria = tela_editar.lineEdit_5.text()

#Agora os valores do banco vão ser atualizados. A tabela ta sendo atualizada com os valores que foram digitados acima, com a condição de onde o valor ID foi o valor passado da varivável global numero_id | Abaixo tem os métodos para fechar e chamar telas para atualizar a tela com a lista de pedidos#

    cursor = banco.cursor()
    cursor.execute("UPDATE tbl_pedidos SET codigo = '{}', descricao = '{}', preco = '{}', categoria = '{}' WHERE ID = {}".format(codigo, descricao, preco, categoria, numero_id))
    tela_editar.close()
    segunda_tela.close()
    abrir_segunda_tela()


#Função usada para gerar o pdf com a lista de pedidos | O SELECT para fazer a leitura dos dados armazenados no banco, executar esse comando e armazernar os dados na variável dado_lidos#

def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tbl_pedidos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

 #A variável y = 0 é usada para escrever no pdf, pois durante a escrita do pdf irão ser passadas coordenadas (x, y). | O objeto do canvas é iniciado na variável pdf, sendo cadastro_pedidos.pdf o nome do arquivo que será gerado. | O Título Produtos Cadastrados é definido com a fonte e tamanho 20 e a posição (x, y) que ele será escrito no pdf que é (200, 800)#
    y = 0
    pdf = canvas.Canvas("cadastro_pedidos.pdf")
    pdf.setFont("Times-Bold", 20)
    pdf.drawString(200, 800, "Pedidos Cadastrados:")

#Depois a fonte é diminuída pra 15 e são escritas as tabelas e suas posições variando no eixo x#

    pdf.setFont("Times-Bold", 15)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "Código")
    pdf.drawString(210, 750, "Descrição")
    pdf.drawString(410, 750, "Preço")
    pdf.drawString(510, 750, "Categoria")

#Aqui se faz um for até o tamanho dos dados que se tem. O y vai escrevendo os dados e pulando uma linha, já que seu valor vai sendo incrementado em 50. O valor a ser escrito é passado a partir do i até o 0 a 4 que são os valores da coluna#

    pdf.setFont("Times-Roman", 15)
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(510, 750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("O PDF foi gerado")


#Criação da função principal que é executada após o usuário clicar no botão de "enviar"#

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    categoria = ""

    print("\nSuas informações:")

#Aqui onde se verifica categoria selecionada, a gente utiliza a string vazia categoria e usa para armazenar o valor do que foi selecionado. Cada vez que o pushButton for clicado, a função principal vai ser utilizada, assim a variável categoria fica vazia novamente para armazenar o valor selecionado#

    if formulario.radioButton.isChecked():
        print("Categoria Bebida foi selecionada")
        categoria = "Bebida"

    elif formulario.radioButton_2.isChecked():
        print("Categoria Lanche foi selecionada")
        categoria = "Lanche"

    elif formulario.radioButton_3.isChecked():
        print("Categoria Sobremesa foi selecionada")
        categoria = "Sobremesa"

    print("Código: {}".format(linha1))
    print("Descrição: {}".format(linha2))
    print("Preço: {}".format(linha3))

#Criou um cursor e usou a instância do mysql.conecctor que foi criada: banco | tem a string que define o comando sql que vai ser usado | a variável "dados" tem o que vai ficar no lugar dos %s | método execute recebe dois paramêtros: o comando sql que vai ser executado e os valores armazenados na variável "dados" | O commit serve para mandar esses comandos sql pro banco#

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tbl_pedidos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()

""" #Aqui é pra limpar o campo de digitação após o envio de um pedido#
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

    formulario.radioButton.setChecked(False)
    formulario.radioButton_2.setChecked(False)
    formulario.radioButton_3.setChecked(False) """
    

#Função que vai ser chamada após o botão pushButton2 ser clicado e assim mostrar a segunda tela com a lista de pedidos#

def abrir_segunda_tela():
    segunda_tela.show()

#O método fetchall vai pegar o que foi feito na última linha do cursor. Todos os dados do banco foram lidos e vão ser salvos na variável dados_lidos#

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tbl_pedidos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

#Aqui o objetivo é mostrar a tabela na interface criada, assim utilizou-se a segunda_tela que é responsável por carregar a lista de dados | o setRowCount determina quantas linhas terá a tabela, assim o parâmetro passado é o tamanho dos dados_lidos | o setColumnCount define o número de colunas, que no nosso caso são 5#
  
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

#Aqui é para salvar os dados listados dentro da tabela na interface. O primeiro for vai de 0 até o número de linhas da tabela, enquanto o segundo que é o número de colunas vai de 0 até 5 | Utilizando o médoto setItem, onde tem que passar cada posição em que o elemento precisa ser inserido na tabela | o QtWidgets com o métodos QTableWidgetItem é onde vai ser passado o elemento dados_lidos para aparecer na tabela na posição [i][j], ele é convertido pra string pois o método só aceita string#

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("telas/formulario.ui")
segunda_tela=uic.loadUi("telas/listar_pedidos.ui")
tela_editar=uic.loadUi("telas/menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(abrir_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_item)
segunda_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados_editados)

formulario.show()
app.exec()
