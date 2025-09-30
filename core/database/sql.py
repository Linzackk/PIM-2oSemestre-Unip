import sqlite3 as sql

CONEXAO = sql.connect("banco-dados/banco_de_dados.db")

CURSOR = CONEXAO.cursor()