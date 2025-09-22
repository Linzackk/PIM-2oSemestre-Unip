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
    ids = utils.importarSiglasIds()
    return mostrar_informacao_filtro(tabela, ids[tabela], id)

def mostrar_informacao_completa(tabela: str, id: str, chave_principal: str):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao

def mostrar_infos_banco():
    # Pega todas as tabelas
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()

    for tabela in tabelas:
        nome_tabela, create_sql = tabela
        print(f"Tabela: {nome_tabela}")

        # Pega o conteúdo dentro dos parênteses do CREATE TABLE
        colunas_def = create_sql[create_sql.find('(')+1:create_sql.rfind(')')]
        linhas = colunas_def.split(',')

        for linha in linhas:
            linha = linha.strip()
            # Ignora constraints globais
            if linha.upper().startswith(('PRIMARY KEY', 'FOREIGN KEY', 'UNIQUE', 'CHECK')):
                continue
            # Nome da coluna é a primeira palavra da linha
            nome_coluna = linha.split()[0]
            print(f" - {nome_coluna}")
        print("-"*50)
    