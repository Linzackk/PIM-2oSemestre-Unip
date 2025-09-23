# Funções relacionadas a atualizacao de informacoes

import sqlite3 as sql

from core import verificacao
from core import estrutura
from core import utils

conexao = sql.connect("banco-dados/banco_de_dados.db")

cursor = conexao.cursor()

def atualizar_informacoes(id_conta: str, informacao: str, nova_informacao: str):
    # Acessa a Tabela da conta, filtra pelo ID e altera a informação.
    tabela = verificacao.identificarFuncao(id_conta)
    id = verificacao.identificarId(tabela)
    cursor.execute(f"UPDATE {tabela} SET {informacao} = ? WHERE {id} = ?", (nova_informacao, id_conta))
    
    print()
    print(f"UPDATE {tabela} SET {informacao} = {nova_informacao} WHERE {id} = {id_conta}")
    print()
    print(F"TABELA {tabela}\nColuna Alterada: {informacao}\nNova Informacao: {nova_informacao}\nId_Alterado: {id_conta}\nId da Tabela: {id}")
    
    conexao.commit()

# TODO: Atualizar_Informacoes, Atualizar_Notas, Atualizar_Professores, etc

