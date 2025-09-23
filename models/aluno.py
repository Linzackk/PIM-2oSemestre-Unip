# Classe Aluno
from core.database import read
from core.database import create
from core import utils

from models.conta import Conta

class Aluno(Conta):
    def __init__(self, id):
        super().__init__(id)
        self.campus = None
        self.curso = None
        self.turma = None
        self.horario_aula = None
               
    @classmethod
    def createFromDb(cls,id):
        aluno = cls(id)
        info = aluno.verificarInfos()
        for c, v in enumerate(aluno.__dict__.items()):
            setattr(aluno, v[0], info[0][c])
        return aluno