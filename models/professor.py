# Classe Professor
from core.database import read
from core.database import create
from core import utils

from models.conta import Conta

class Professor(Conta):
    def __init__(self, id):
        super().__init__(id)
        self.materia_ensino = None
        
    @classmethod
    def createFromDb(cls,id):
        professor = cls(id)
        info = professor.verificarInfos()
        for c, v in enumerate(professor.__dict__.items()):
            setattr(professor, v[0], info[0][c])
        return professor    
