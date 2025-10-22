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
        opcoes = ["Ver Informações", "Alterar Informações", "Ver Notas", "Ver Faltas"]
        while True:
            a = estrutura.escolher_opcao(opcoes, "MENU DO ALUNO")
            break
        return a
    
    def ver_notas(self):
        notas = read.pegar_infos_nota(self.id)
        print('-'*50)
        print("{:<30} {:<20} {:>5} {:>15}\n".format("Professor", "Matéria", "Nota", "Data"))
        for i in notas:
            print(f"{i[2]:<30} {i[1]:<20} {i[0]:>5} {utils.formatar_data_br(i[3]):>15}")
        print('-'*50)
        input(" Aperte ENTER para continuar...")
    
    def ver_faltas(self):
        faltas = read.ver_faltas(self.id)
        print('-'*50)
        print("{:<20} {:>5}".format("Matéria", "Faltas"))
        for i in faltas:
            print(f"{i[1]:<20} {i[0]:>5}x")
        print('-'*50)
        input(" Aperte ENTER para continuar...")