import data
import sqlite3
from PyQt5 import uic, QtWidgets


# funçao para pedir o nome do usuario antes de salvar no banco
def insere_dados(score):
    # verificação de qual opçao o usuario marcou para guardar a pontuação na variavel score
    if tela_quiz.radioButton_3.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_8.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_15.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_16.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_21.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_26.isChecked():
        score += 1
    else:
        score += 0
    tela_adicionar.label_2.setText(f'Sua pontuação: {score} pontos')
    tela_adicionar.show()
    tela_quiz.close()


# funçao para adicionar nome e pontos obtidos no quiz dentro do banco
def salvar_dados(score):
    conexao = data.connect()
    data.create(conexao)  # comentar essa linha depois de criar a tabela

    nome = tela_adicionar.lineEdit.text()
    if tela_quiz.radioButton_3.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_8.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_15.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_16.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_21.isChecked():
        score += 1
    else:
        score += 0
    if tela_quiz.radioButton_26.isChecked():
        score += 1
    else:
        score += 0
    data.insert(conexao, nome, score)
    tela_adicionar.close()


def mostrar_dados():
    conexao = data.connect()
    dados_lidos = data.busca(conexao)

    # Jogando os itens na tabela
    tela_dados.tableWidget.setRowCount(len(dados_lidos))
    tela_dados.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_dados.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    conexao.close()
    tela_dados.show()


def inicia_quiz():
    tela_quiz.show()


def apagar():
    banco = sqlite3.connect('questoes.db')
    linha = tela_dados.tableWidget.currentRow()  # selecionar a linha
    tela_dados.tableWidget.removeRow(linha)  # para renover a linha

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM questoes")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM questoes WHERE id=" + str(valor_id))
    banco.commit()
    banco.close()


app = QtWidgets.QApplication([])
tela = uic.loadUi("Telainicial.ui")
tela_adicionar = uic.loadUi("adicionar.ui")
tela_quiz = uic.loadUi("tela_quiz.ui")
tela_dados = uic.loadUi("dados.ui")

# evento dos botoes
tela.pushButtonIniciar.clicked.connect(inicia_quiz)
tela_quiz.pushButtonEnviar.clicked.connect(insere_dados)
tela_adicionar.pushButtonEnviar.clicked.connect(salvar_dados)
tela.pontuacao.clicked.connect(mostrar_dados)
tela_dados.pushButton.clicked.connect(apagar)

tela.show()
app.exec()
