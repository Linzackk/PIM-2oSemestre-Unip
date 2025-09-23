# Classe Coordenacao
from core.database import read
from core.database import create
from core import utils

from models.conta import Conta

class Coordenador(Conta):
    def __init__(self, id):
        super().__init__(id)
        self.campus = None
        self.cargo = None
    
    @classmethod
    def createFromDb(cls,id):
        coordenador = cls(id)
        info = coordenador.verificarInfos()
        for c, v in enumerate(coordenador.__dict__.items()):
            setattr(coordenador, v[0], info[0][c])
        return coordenador      
