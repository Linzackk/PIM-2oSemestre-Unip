# Classe Mãe "Conta" 
from core.database import leitura
from core.database import gravacao
from core import utils

class Conta:
    def __init__(self, id):
        self.id = id
        self.nome = ""
        self.idade = 0
        self.genero = ""
        self.cpf = ""
        
    def verificarInfos(self):
        id = self.id
        tabela = utils.identificarFuncao(id)
        chave = utils.importarSiglasIds()[tabela]
        infos = leitura.mostrar_informacao_completa(tabela, id, chave)
        