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

conexao = sql.connect("banco-dados/banco_de_dados.db")

cursor = conexao.cursor()
