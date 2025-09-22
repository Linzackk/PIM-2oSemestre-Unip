# Classe Coordenacao
from core.database import leitura
from core.database import gravacao
from core import utils

from models.conta import Conta

class Coordenador(Conta):
    def __init__(self, id):
        super().__init__(id)
        self.campus = None
        self.cargo = None
        info = self.verificarInfos()
        for c, v in enumerate(self.__dict__.items()):
            setattr(self, v[0], info[0][c])       
        
    def atualizar_info(informacao, novaInformacao):
        # Função para atualizar alguma informacao
        print("Hello, World!")
