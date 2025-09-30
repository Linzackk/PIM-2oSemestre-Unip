# Classe Mãe "Conta" 
from core.database import read
from core.database import create
from core.database import update
from core import verificacao
from core import estrutura

class Conta:
    def __init__(self, id):
        self.id = id
        self.nome = None
        self.idade = None
        self.genero = None
        self.telefone = None
        self.cpf = None
        self.data_nascimento = None
        
    def verificarInfos(self):
        id = self.id
        tabela = verificacao.identificarFuncao(id)
        chave = verificacao.identificarId(tabela)
        infos = read.mostrar_informacao_completa(tabela, id, chave)
        return infos
    
    def mostrar_info(self):
        print("-"*30)
        for c, v in self.__dict__.items():
           print(f"{c.upper()}: {v}")
           
    def exportar_info(self):
        return self.__dict__.items()
    
    def atualizar_informacao(self):
        opcoes = {
            1: "nome",
            2: "idade",
            3: "genero",
            4: "telefone"
        }
        escolha = self.escolher_informacao()
        
        try:
            tipo_escolha = opcoes[escolha]
        except KeyError:
            return
        
        certeza = False
        while not certeza:
            sair = verificacao.continuarEscolha()
            if sair:
                break
            
            nova_escolha = input(f"A nova informação para {tipo_escolha}: ")
            certeza = verificacao.verificarCerteza(nova_escolha)
            
            if certeza:
                update.atualizar_informacoes(self.id, tipo_escolha, nova_escolha)
                self.atualizar_localmente(tipo_escolha, nova_escolha)
                return
            
        
    def escolher_informacao(self):
        opcoes = ["Nome", "Idade", "Genero", "Telefone"]
        escolha = estrutura.escolher_opcao(opcoes)
        return escolha
    
    def atualizar_localmente(self, informacao, nova_informacao):
        setattr(self, informacao, nova_informacao)
        