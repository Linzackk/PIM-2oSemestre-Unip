# Classe Professor
from core import verificacao

from core.database import read
from core.database import create
from core.database import update

from core import utils

from models.conta import Conta

class Professor(Conta):
    def __init__(self, id):
        super().__init__(id)
        self.materia_ensino = None
        self.id_materia = None
        
    @classmethod
    def createFromDb(cls,id):
        professor = cls(id)
        info = professor.verificarInfos()
        for c, v in enumerate(professor.__dict__.items()):
            setattr(professor, v[0], info[0][c])
        return professor  
    
    def postar_nota(self):
        id_aluno = input("Insira o ID do aluno: ")
        while True:
            if verificacao.existencia_conta(id_aluno) and id_aluno[-1] == "A":
                break
            
            sair = verificacao.continuarEscolha()
            if sair:
                return
            
            id_aluno = input("ID inválido. Insira o ID do aluno: ")
        
        nota = input("Insira a Nota do Aluno: ")
        while True:
            if verificacao.verificarTipoEntrada("float", nota):
                nota = float(nota)
            
            if verificacao.verificarNota(nota):
                break
            
            nota = input("Nota Inválida. Insira a Nota do Aluno: ")
            
        data_prova = input("Insira a Data da prova [YYYY-MM-DD]\n")   
        while True:
            if verificacao.verificarData(data_prova):
                break
            data_prova = input("Data Inválida. Insira a Data da prova [YYYY-MM-DD]\n")
        
        create.adicionar_nota(id_aluno, self.id_materia, nota, data_prova)
        