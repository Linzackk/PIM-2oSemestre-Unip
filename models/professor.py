# Classe Professor
from core import verificacao

from core.database import read
from core.database import create
from core.database import update

from core import utils
from core import estrutura

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
    
    def mostrar_menu(self):
        opcoes = ["Ver Informações", "Alterar Informações", "Postar Notas", "Postar Faltas"]
        a = estrutura.escolher_opcao(opcoes, "MENU DO PROFESSOR")  
        return a        
    
    def escolher_opcao(self):
        escolha = self.mostrar_menu()
        match escolha:
            case 0:
                return
            case 1:
                self.mostrar_info()
            case 2:
                self.atualizar_informacao()
            case 3:
                self.postar_nota()
            case 4:
                self.subir_falta()

    def postar_nota(self):
        id_aluno = input("Insira o ID do aluno: ")
        while True:
            if verificacao.existencia_conta(id_aluno) and verificacao.verificarAluno(id_aluno): # Verifica Se a Conta existe e é de um aluno
                break
            print("Id Inválido.")
            sair = verificacao.continuarEscolha()
            if sair: # Verifica se o usuario deseja sair
                return
            id_aluno = input("Insira o ID do aluno: ")
            
        nota = input("Insira a Nota do Aluno: ")
        while True:
            if verificacao.verificarTipoEntrada("float", nota): # Verifica se a nota foi inserida corretamente (um numero float)
                nota = float(nota)
            if verificacao.verificarNota(nota): # Verifica se a nota está no intervalo correto
                break
            nota = input("Nota Inválida. Insira a Nota do Aluno: ")    
        data_prova = data_prova = utils.pegar_data()
        while True:
            if verificacao.verificarData(data_prova): # Verifica se a data da prova inserida é válida
                break
            print("Data de Prova Inválida.")
            data_prova = utils.pegar_data()
        info = read.mostrar_tripla_condicao("notas", id_aluno, self.id_materia, data_prova, "id_aluno", "materia_id", "data_prova")
        if info == []:
            create.adicionar_nota(id_aluno, self.id_materia, nota, data_prova)
            print("nota criada")
        else:
            update.atualizar_nota(id_aluno, self.id_materia, data_prova, nota)
            print("nota atualizada")
        print("Nota Postada com Sucesso.")
        
    def subir_falta(self):
        while True:
            id_aluno = input("Insira ID do Aluno: ")
            if id_aluno[-1] != "A":
                print("Insira um ID de Aluno.")
                continue
            if not verificacao.existencia_conta(id_aluno):
                print("Aluno Inexistente")
                continue
            faltas = 3 # Padrão de Faltas na UNIP (mudar com forme o uso)
            infos = read.mostrar_dupla_condicao("faltas", id_aluno, self.id_materia, "id_aluno", "materia_id")
            if infos == []:
                create.adicionar_aluno_faltas(id_aluno, self.id_materia, faltas)
            else:
                update.atualizar_faltas(id_aluno, self.id_materia, infos[0][2] + 3)
            print("Faltas Computadas com Sucesso.")
       
            continuar = input("Deseja Continuar? [s/n]").lower()
            if continuar == "n":
                break