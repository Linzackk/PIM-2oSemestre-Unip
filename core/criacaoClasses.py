# Criação de classes
from models.aluno import Aluno
from models.professor import Professor
from models.coordenacao import Coordenador
from core import utils

def criarAluno(id: str) -> Aluno:
    return Aluno(id)

def criarProfessor(id: str) -> Professor:
    return Professor(id)

def criarCoordenador(id: str) -> Coordenador:
    return Coordenador(id)

def criarUsuario(id: str):
    funcoes = utils.importarSiglaFuncao()
    classe = funcoes[id[-1]]
    if classe == "alunos":
        usuario = criarAluno(id)
    elif classe == "professores":
        usuario = criarProfessor(id)
    elif classe == "coordenacao":
        usuario = criarCoordenador(id)
    else:
        return False
    return usuario
