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
        escolha = self.escolher_informacao()
        if escolha == 1:
            tipo_escolha = "nome"
        if escolha == 2:
            tipo_escolha = "idade"
        if escolha == 3:
            tipo_escolha = "genero"
        else:
            pass
        
        certeza = False
        while not certeza:
            nova_escolha = input(f"A nova informação para {tipo_escolha}: ")
            certeza = verificacao.verificarCerteza(nova_escolha)
            if not certeza:
                sair = verificacao.continuarEscolha()
                if sair:
                    break
            if certeza:
                update.atualizar_informacoes(self.id, tipo_escolha, nova_escolha)
                self.atualizar_localmente(tipo_escolha, nova_escolha)
        
    def escolher_informacao(self):
        opcoes = ["Nome", "Idade", "Genero"]
        escolha = estrutura.escolher_opcao(opcoes)
        return escolha
    
    def atualizar_localmente(self, informacao, nova_informacao):
        setattr(self, informacao, nova_informacao)
        