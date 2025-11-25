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
    
    def escolher_opcao(self):
        escolha = self.mostrar_menu()
        match escolha:
            case 0:
                return escolha
            case 1:
                self.mostrar_info()
            case 2:
                self.atualizar_informacao()
            case 3:
                self.ver_notas()
            case 4:
                self.ver_faltas()
    
    def ver_notas(self):
        notas = read.pegar_infos_nota(self.id)
        print('-'*103)
        print("{:<30} {:<50} {:>5} {:>15}\n".format("Professor", "Matéria", "Nota", "Data"))
        for i in notas:
            print(f"{i[2]:<30} {i[1]:<50} {i[0]:>5} {utils.formatar_data_br(i[3]):>15}")
        print('-'*103)
        input(" Aperte ENTER para continuar...")
    
    def ver_faltas(self):
        faltas = read.ver_faltas(self.id)
        print('-'*103)
        print("{:<20} {:>5}".format("Matéria", "Faltas"))
        for i in faltas:
            print(f"{i[1]:<20} {i[0]:>5}x")
        print('-'*103)
        input(" Aperte ENTER para continuar...")