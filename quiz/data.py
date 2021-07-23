import sqlite3

CREATE_TABLE = "create table questoes (id integer primary key, nome text, score int)"

INSERT_DADOS = "insert into questoes (nome, score ) values (?, ?);"

BUSCA_DADOS = "select * from questoes;"

DELETE_DADOS = "delete * from questoes where id = ?;"

BUSCA_LINGUAGEM_MAIS_ANTIGA = """
select * from linguagens
order by ano asc
limit 1
"""

BUSCA_LINGUAGEM_MAIS_RECENTE = """
select * from linguagens
order by ano desc
limit 2
"""


def connect():
    return sqlite3.connect("questoes.db")


def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)


def insert(conexao, nome, score):
    with conexao:
        conexao.execute(INSERT_DADOS, (nome, score))


def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_DADOS).fetchall()


def deletar(conexao):
    with conexao:
        return conexao.execute(DELETE_DADOS).fetchall()


def busca_antiga(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_ANTIGA).fetchone()

def busca_recente(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGEM_MAIS_RECENTE).fetchall()