import sqlite3 as sql

from core import verificacao

conexao = sql.connect("banco_de_dados.db")

cursor = conexao.cursor()

def mostrar_informacao_unica(tabela, chave_principal, id):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao
    
def mostrar_aluno(id: str):
    return mostrar_informacao_unica("alunos", "id_aluno", id)
    
def mostrar_login(id: str):
    return mostrar_informacao_unica("login", "id", id)

def mostrar_professor(id: str):
    return mostrar_informacao_unica("professores", "id_professor", id)
    
def mostrar_coordenacao(id: str):
    return mostrar_informacao_unica("coordenacao", "id_admin", id)
    
def mostrar_campus(id: str):
    return mostrar_informacao_unica("campus", "id_campus", id)
    
def mostrar_curso(curso: str):
    return mostrar_informacao_unica("cursos", "curso", curso)
    
def mostrar_materia(materia: str):
    return mostrar_informacao_unica("materias", "materia", materia)

def mostrar_tudo_tabela(tabela: str):
    informacao = cursor.execute(f"SELECT * FROM {tabela}").fetchall()
    return informacao