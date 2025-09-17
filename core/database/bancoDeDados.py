# Funções relacionadas ao Banco de Dados
# TODO: Funcoes para criar, ler, atualizar e deletar informações das tabelas

# ! Criar as tabelas CAMPUS, LOGIN, ALUNOS, PROFESSORES, COORDENAÇÃO, CURSOS, MATERIAS e NOTAS previamente !

# Informação das tabelas:
# Colunas por tabela

# aluno = ["id_aluno", "nome", "idade", "genero", "data_nascimento", "cpf", "campus", "curso", "turma", "horario_aula"]

# professor = ["id_professor", "nome", "idade", "genero", "data_nascimento", "cpf", "materia_ensino"]

# coordenacao = ["id_admin", "nome", "idade", "genero" "campus", "data_nascimento", "cpf", "cargo"]

# campus = ["id_campus", "endereco", "diretor", "diretor_id", "telefone"]  # Corrigi a vírgula que estava faltando entre diretor_id e telefone

# cursos = ["curso_id", "curso", "duracao_anos", "formacao"]  # Corrigi a sintaxe que estava errada: "curso_id, INTEGER PRIMARY KEY" → só "curso_id"

# materias = ["materia_id", "materia", "professor", "professor_id", "carga_horaria"]

# login = ["id", "senha"]

import sqlite3 as sql

from core import verificacao
from core import estrutura

conexao = sql.connect("banco_de_dados.db")

cursor = conexao.cursor()

# Adicionar Contas
 
def adicionar_conta_login(id: str, senha: str):
    cursor.execute("INSERT INTO login VALUES (?, ?)", (id, senha))
    conexao.commit()
    print("Login adicionado com sucesso.")

def adicionar_aluno(nome: str, idade: int, data_nascimento: str, genero: str, cpf: str, campus: str, curso: str, turma: str, horario_aula: str, senha: str="123"):
    id = verificacao.criar_id("aluno")
    cursor.execute("""
                INSERT INTO alunos VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (id, nome, idade, genero, data_nascimento, cpf, campus, curso, turma, horario_aula)
                )
                
    adicionar_conta_login(id, senha)
    conexao.commit()
    print(f"Aluno {nome} adicionado com sucesso com ID {id}")
    
def adicionar_professor(nome :str, idade :int, genero :str, data_nascimento: str, cpf: str, materia_ensino: str, senha :str="123"):
    id = verificacao.criar_id("professor")
    cursor.execute("""
                INSERT INTO professores VALUES ( ?, ?, ?, ?, ?, ?, ?)
                """, (id, nome, idade, genero, data_nascimento, cpf, materia_ensino)
                )
                
    adicionar_conta_login(id, senha)
    conexao.commit()
    print(f"Professor {nome} adicionado com sucesso com ID {id}")
    
def adicionar_coordenacao(nome: str, idade: int, genero: str, campus: str, data_nascimento: str, cpf: str, cargo: str, senha: str="123"):
    id = verificacao.criar_id("coordenador")
    cursor.execute("""
                INSERT INTO coordenacao VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
                """, (id, nome, idade, genero, campus, data_nascimento, cpf, cargo)
                )
                
    adicionar_conta_login(id, senha)
    conexao.commit()
    print(f"Coordenador {nome} adicionado com sucesso com ID {id}")
    
def adicionar_campus(nome: str, endereco: str, diretor: str, diretor_id: str, telefone: str):
    cursor.execute("""
                INSERT INTO campus (nome, endereco, diretor, diretor_id, telefone) VALUES ( ?, ?, ?, ?, ? )
                """, ( nome, endereco, diretor, diretor_id, telefone)
                )
                
    conexao.commit()
    print(f"Campus {nome} adicionado com sucesso")
    
def adicionar_curso(curso: str, duracao_anos: int, formacao: str):
    cursor.execute("""
                INSERT INTO cursos (curso, duracao_anos, formacao) VALUES ( ?, ?, ?)
                """, (curso, duracao_anos, formacao)
                )
                
    conexao.commit()
    print(f"Curso {curso} adicionado com sucesso.")
    
def adicionar_materia(materia: str, professor: str, professor_id: str, carga_horaria: int):
    cursor.execute("""
                INSERT INTO materias (materia, professor, professor_id, carga_horaria) VALUES ( ?, ?, ?, ?)
                """, (materia, professor, professor_id, carga_horaria)
                )
                
    conexao.commit()
    print(f"Materia {materia} adicionado com sucesso.")
        

 
# Mostrar Informações Únicas 
   
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

