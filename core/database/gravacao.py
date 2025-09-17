import sqlite3 as sql

from core import verificacao

conexao = sql.connect("banco-dados/banco_de_dados.db")

cursor = conexao.cursor()

def adicionar_conta_login(id: str, senha: str):
    cursor.execute("INSERT INTO login VALUES (?, ?)", (id, senha))
    conexao.commit()
    print("Login adicionado com sucesso.")

def adicionar_conta(tabela: str, colunas: list, valores: tuple):
    placeholder = ", ".join("?") * len(valores)
    colunas_str = ", ".join(colunas)
    sql = f"INSERT INTO {tabela} ({colunas_str}) VALUES ({placeholder})"
    cursor.execute(sql, valores)
    conexao.commit()


def adicionar_aluno(nome, idade, data_nascimento, genero, cpf, campus, curso, turma, horario_aula, senha="123"):
    id = verificacao.criar_id("aluno")
    adicionar_conta("alunos",
                  ["id_aluno", "nome", "idade", "genero", "data_nascimento", "cpf", "campus", "curso", "turma", "horario_aula"],
                  (id, nome, idade, genero, data_nascimento, cpf, campus, curso, turma, horario_aula))
    adicionar_conta_login(id, senha)
    print(f"Aluno {nome} adicionado com sucesso com ID {id}")
    
def adicionar_professor(nome: str, idade: int, genero: str, data_nascimento: str, cpf: str, materia_ensino: str, senha: str="123"):
    id = verificacao.criar_id("professor")
    adicionar_conta(
        "professores",
        ["id_professor", "nome", "idade", "genero", "data_nascimento", "cpf", "materia_ensino"],
        (id, nome, idade, genero, data_nascimento, cpf, materia_ensino)
    )
    adicionar_conta_login(id, senha)
    print(f"Professor {nome} adicionado com sucesso com ID {id}")
    
def adicionar_coordenacao(nome: str, idade: int, genero: str, campus: str, data_nascimento: str, cpf: str, cargo: str, senha: str="123"):
    id = verificacao.criar_id("coordenador")
    adicionar_conta(
        "coordenacao",
        ["id", "nome", "idade", "genero", "campus", "data_nascimento", "cpf", "cargo"],
        (id, nome, idade, genero, campus, data_nascimento, cpf, cargo)
    )
    adicionar_conta_login(id, senha)
    print(f"Coordenador {nome} adicionado com sucesso com ID {id}")
    
def adicionar_campus(nome, endereco, diretor, diretor_id, telefone):
    adicionar_conta("campus",
                  ["nome", "endereco", "diretor", "diretor_id", "telefone"],
                  (nome, endereco, diretor, diretor_id, telefone))
    print(f"Campus {nome} adicionado com sucesso")

def adicionar_curso(curso, duracao_anos, formacao):
    adicionar_conta("cursos",
                  ["curso", "duracao_anos", "formacao"],
                  (curso, duracao_anos, formacao))
    print(f"Curso {curso} adicionado com sucesso")

def adicionar_materia(materia, professor, professor_id, carga_horaria):
    adicionar_conta("materias",
                  ["materia", "professor", "professor_id", "carga_horaria"],
                  (materia, professor, professor_id, carga_horaria))
    print(f"Matéria {materia} adicionada com sucesso")
