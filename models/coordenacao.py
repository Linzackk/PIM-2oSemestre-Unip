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
    
    def mostrar_menu(self):
        opcoes = ["Ver Informações", "Alterar Informações", "Alunos", "Professores"]
        while True:
            a = estrutura.escolher_opcao(opcoes, "MENU DA COORDENACAO")
            break
        
    def adicionar_aluno(self):
        # Pegar informações dos alunos: NOME COMPLETO, IDADE, GENERO, TELEFONE, CPF, DATA_NASCIMENTO, CAMPUS, CURSO, TURMA, HORARIO_AULA
        while True:
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
            
            if infos_corretas == "s":
                break
            print("Reiniciando para inserção de dados.")
        create.adicionar_aluno(nome, idade, genero, telefone, cpf, data_nascimento, campus, curso, turma, horario_aula)
            
    def adicionar_professor(self):
        while True:
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
            
            if infos_corretas == "s":
                break
            print("Reiniciando para inserção de dados.")
        create.adicionar_professor(nome,idade,genero,telefone,cpf,data_nascimento,materia_ensino)