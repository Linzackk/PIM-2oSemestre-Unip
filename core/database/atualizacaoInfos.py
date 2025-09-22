# Funções relacionadas a atualizacao de informacoes

import sqlite3 as sql

from core import verificacao
from core import estrutura

conexao = sql.connect("banco-dados/banco_de_dados.db")

cursor = conexao.cursor()

# TODO: Atualizar_Informacoes, Atualizar_Notas, Atualizar_Professores, etc

