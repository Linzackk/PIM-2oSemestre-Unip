from core.database.sql import CURSOR as cursor
from core.database.sql import CONEXAO as conexao

from core import verificacao
from core import utils

from core.database import read

def adicionar_conta_login(id: str, senha: str):
    cursor.execute("INSERT INTO login VALUES (?, ?)", (id, senha))
    conexao.commit()
    print("Login adicionado com sucesso.")

def adicionar_aluno(nome: str, idade: int, genero: str, telefone: str, cpf: str, data_nascimento: str, campus: str, curso: str, turma: str, horario_aula: str, senha: str = "123"):
    id = verificacao.criar_id("aluno")
    cursor.execute("""
                INSERT INTO alunos VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (id, nome, idade, genero, telefone, cpf, data_nascimento, campus, curso, turma, horario_aula)
                )
                
    adicionar_conta_login(id, senha)
    conexao.commit()
    print(f"Aluno {nome} adicionado com sucesso com ID {id}")
    
def adicionar_professor(nome: str, idade: int, genero: str, telefone: str, cpf: str, data_nascimento: str, materia_ensino: str, id_materia: str, senha: str = "123"):
    id = verificacao.criar_id("professor")
    id_materia = utils.pegarIdMateria(materia_ensino)[0]    
    print(id_materia)
    cursor.execute("""
                INSERT INTO professores VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (id, nome, idade, genero, telefone, cpf, data_nascimento, materia_ensino, id_materia)
                )
                
    adicionar_conta_login(id, senha)
    conexao.commit()
    print(f"Professor {nome} adicionado com sucesso com ID {id}")
    
def adicionar_coordenacao(nome: str, idade: int, genero: str, telefone: str, cpf: str, data_nascimento: str, campus: str, cargo: str, senha: str = "123"):
    id = verificacao.criar_id("coordenador")
    cursor.execute("""
                INSERT INTO coordenacao VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (id, nome, idade, genero, telefone, data_nascimento, cpf, campus, cargo)
                )
                
    adicionar_conta_login(id, senha)
    conexao.commit()
    print(f"Coordenador {nome} adicionado com sucesso com ID {id}")
    
def adicionar_campus(nome: str, endereco: str, diretor: str, telefone: str):
    cursor.execute("""
                INSERT INTO campus (nome, endereco, diretor_id, telefone) VALUES ( ?, ?, ?, ? )
                """, ( nome, endereco, diretor, telefone)
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
    
def adicionar_materia(materia: str, professor_id: str, carga_horaria: int):
    cursor.execute("""
                INSERT INTO materias (materia, id_professor, carga_horaria) VALUES ( ?, ?, ?)
                """, (materia, professor_id, carga_horaria)
                )
                
    conexao.commit()
    adicionar_materia_faltas()
    print(f"Materia {materia} adicionado com sucesso.")
    
def adicionar_materia_faltas():
    materia = read.mostrar_tabela_completa("materias")[-1][0]
    cursor.execute("""
                INSERT INTO faltas (materia_id) VALUES(?)
                """, (materia, ))
    conexao.commit()
    
def adicionar_nota(id_aluno, id_materia, nota, data_prova):
    cursor.execute("""
                   INSERT INTO notas (materia_id, id_aluno, nota, data_avaliacao) VALUES (?,?,?,?)
                   """, (id_aluno, id_materia, nota, data_prova)
                   )