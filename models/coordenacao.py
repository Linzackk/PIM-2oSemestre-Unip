# Classe Coordenacao
from core.database import read
from core.database import create
from core import utils
from core import estrutura

from models.conta import Conta

class Coordenador(Conta):
    def __init__(self, id):
        super().__init__(id)
        self.campus = None
        self.cargo = None
    
    @classmethod
    def createFromDb(cls,id):
        coordenador = cls(id)
        info = coordenador.verificarInfos()
        for c, v in enumerate(coordenador.__dict__.items()):
            setattr(coordenador, v[0], info[0][c])
        return coordenador  
    
    def mostrar_menu(self, complemento=""):
        if complemento == "":
            opcoes = ["Ver Informações", "Alterar Informações", "Alunos", "Profesores", "Matérias"]
        elif complemento == "Alunos":
            opcoes = ["Adicionar Aluno", "Atualizar Aluno", "Deletar Aluno"]
        elif complemento == "Professores":
            opcoes = ["Adicionar Professor", "Atualizar Professor", "Deletar Professor"]
        elif complemento == "Matérias":
            opcoes = ["Adicionar Materia", "Ver Materias", "Atualizar Materia", "Deletar Materia"]
        a = estrutura.escolher_opcao(opcoes, "MENU DA COORDENACAO")
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
                escolha2 = self.mostrar_menu("Alunos")
            case 4:
                escolha2 = self.mostrar_menu("Professores")
            case 5:
                escolha2 = self.mostrar_menu("Matérias")
            case 6:
                self.mostrar_contas()
        
    def adicionar_aluno(self):
        # Pegar informações dos alunos: NOME COMPLETO, IDADE, GENERO, TELEFONE, CPF, DATA_NASCIMENTO, CAMPUS, CURSO, TURMA, HORARIO_AULA
        infos_corretas = "n"
        while infos_corretas != "s":
            nome = input("Insira seu Nome completo: ").lower().title()
            idade = int(input("Insira sua Idade: "))
            genero = input("Insira seu Genero: ")
            telefone = utils.pegar_telefone()
            cpf = utils.pegar_cpf()
            print("Insira sua Data de Nascimento")
            data_nascimento = utils.pegar_data()
            campus = input("Insira o Campus: ")
            curso = input("Insira o Curso: ")
            turma = None
            horario_aula = input("Horário Matutino, Vespertino ou Noturno: ")
            print("-"*50)
            print(f"Nome: {nome}\n Idade: {idade}\nGenero: {genero}\nTelefone: {telefone}\nCpf: {cpf}\nData de Nascimento: {data_nascimento}\nCampus: {campus}\nCurso: {curso}\nHorario de Aula: {horario_aula}")
            infos_corretas = input("As informações inseridas estão corretas? [s/n]\n").lower()
            print("Reiniciando para inserção de dados.")
        create.adicionar_aluno(nome, idade, genero, telefone, cpf, data_nascimento, campus, curso, turma, horario_aula)
            
    def adicionar_professor(self):
        infos_corretas = "n"
        while infos_corretas != "s":
            nome = input("Insira seu Nome completo: ").lower().title()
            idade = int(input("Insira sua Idade: "))
            genero = input("Insira seu Genero: ")
            telefone = utils.pegar_telefone()
            cpf = utils.pegar_cpf()
            print("Insira sua Data de Nascimento")
            data_nascimento = utils.pegar_data()
            materia_ensino = input("Insira a matéria de Ensino: ")
            print(f"Nome: {nome}\n Idade: {idade}\nGenero: {genero}\nTelefone: {telefone}\nCpf: {cpf}\nData de Nascimento: {data_nascimento}\nMatéria de Ensino: {materia_ensino}")
            infos_corretas = input("As informações inseridas estão corretas? [s/n]\n").lower()
            print("Reiniciando para inserção de dados.")
            
        # ! VINCULAR O PROFESSOR A MATERIA NA TABELA "materias"
        create.adicionar_professor(nome,idade,genero,telefone,cpf,data_nascimento,materia_ensino)
    
    def mostrar_contas(self):
        print("     Mostrando contas...")
        
    # ? Criar funções para Atualização de Professores e Ou alunos (informações pessoais, turmas e materias)