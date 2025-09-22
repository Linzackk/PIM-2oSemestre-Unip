# Classe Mãe "Conta" 
from core.database import leitura
from core.database import gravacao
from core import verificacao

class Conta:
    def __init__(self, id):
        self.id = id
        self.nome = None
        self.idade = None
        self.genero = None
        self.data_nascimento = None
        self.cpf = None
        
    def verificarInfos(self):
        id = self.id
        tabela = verificacao.identificarFuncao(id)
        chave = verificacao.identificarId(tabela)
        infos = leitura.mostrar_informacao_completa(tabela, id, chave)
        return infos
    
    def mostrar_info(self):
        print("-"*30)
        for c, v in self.__dict__.items():
           print(f"{c.upper()}: {v}")
           
    def exportar_info(self):
        return self.__dict__.items()
        