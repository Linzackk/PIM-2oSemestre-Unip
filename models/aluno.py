# Classe Aluno
from core.database import read
from core.database import create
from core import utils
from core import estrutura

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
    
    def mostrar_menu(self):
        opcoes = ["Ver Informações", "Alterar Informações", "Ver Notas"]
        while True:
            a = estrutura.escolher_opcao(opcoes, "MENU DO ALUNO")
            break
        return a
    
    def ver_notas(self):
        notas = read.pegar_infos_nota(self.id)
        print('-'*50)
        for i in notas:
            print(f"Professor: {i[2]}; Matéria: {i[1]}; Nota: {i[0]}")
        print('-'*50)