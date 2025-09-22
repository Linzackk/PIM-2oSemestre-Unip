import sqlite3 as sql
import re
from core import utils
from core import verificacao

conexao = sql.connect("banco-dados/banco_de_dados.db")

cursor = conexao.cursor()

def mostrar_informacao_filtro(tabela, chave_principal, id):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao

def mostrar_informacao(tabela, id):
    id_tabela = verificacao.identificarId(tabela)
    print(id_tabela)
    if not id_tabela:
        return False
    return mostrar_informacao_filtro(tabela, id_tabela, id)

def mostrar_informacao_completa(tabela: str, id: str, chave_principal: str):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao
