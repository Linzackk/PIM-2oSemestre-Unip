import sqlite3 as sql
import json

from core import verificacao

conexao = sql.connect("banco-dados/banco_de_dados.db")

cursor = conexao.cursor()

def mostrar_informacao_unica(tabela, chave_principal, id):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao

def mostrar_informacao(tabela, id):
    with open("ids-tabelas/ids.json", "r") as arquivo:
        ids = json.loads("\n".join(arquivo.readlines()))    
    return mostrar_informacao_unica(tabela, ids[tabela], id)


def mostrar_informacao_completa(tabela: str):
    informacao = cursor.execute(f"SELECT * FROM {tabela}").fetchall()
    return informacao