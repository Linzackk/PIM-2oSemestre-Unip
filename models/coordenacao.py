# Classe Coordenacao
from core.database import read
from core.database import create
from core import utils
from core import estrutura
from core import verificacao

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
            opcoes = ["Ver Informações", "Alterar Informações", "Alunos", "Professores", "Matérias"]
        elif complemento == "Alunos":
            opcoes = ["Adicionar Aluno", "Ver Alunos", "Atualizar Aluno", "Deletar Aluno"]
        elif complemento == "Professores":
            opcoes = ["Adicionar Professor", "Ver Professores", "Atualizar Professor", "Deletar Professor"]
        elif complemento == "Matérias":
            opcoes = ["Adicionar Materia", "Ver Materias", "Atualizar Materia", "Deletar Materia"]
        a = estrutura.escolher_opcao(opcoes, "MENU DA COORDENACAO")
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
                while True:
                    escolha2 = self.mostrar_menu("Alunos")
                    match escolha2:
                        case 0:
                            break
                        case 1:
                            self.adicionar_aluno()
                        case 2:
                            self.ver_alunos()
                        case 3:
                            self.atualizar_aluno()
                        case 4:
                            self.deletar_aluno()
                
            case 4:
                while True:
                    escolha2 = self.mostrar_menu("Professores")
                    match escolha2:
                        case 0:
                            break
                        case 1:
                            self.adicionar_professor()
                        case 2:
                            self.ver_professores()
                        case 3:
                            self.atualizar_professor()
                        case 4:
                            self.deletar_professor()
            case 5:
                while True:
                    escolha2 = self.mostrar_menu("Matérias")
                    match escolha2:
                        case 0:
                            break
                        case 1:
                            self.adicionar_materia()
                        case 2:
                            self.ver_materias()
                        case 3:
                            self.atualizar_materia()
                        case 4:
                            self.deletar_materia()
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
            turma = input("Insira a Turma do Aluno: ")
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
        
    def atualizar_aluno(self):
        # Atualizar as informações padrão do aluno
        pass
    
    def atualizar_professor(self):
        # Atualizar as informações padrão do aluno
        pass
    
    def deletar_conta(self):
        # Deletar uma conta com base no ID das tabelas que a conta faz parte
        pass
    
    def ver_professores(self):
        # ('7UC3OGP', 'Joao Carlos', 39, 'Masculino', '(11) 912345678', '123.456.789-10', '1986-04-18', 'Matemática Básica', 1)
        professores = read.mostrar_tabela_completa("professores")
        print("-"*176)
        print("{:<9}{:<50}{:<7}{:<11}{:<16}{:<16}{:<17}{:<50}".format("ID", "Nome", "Idade", "Gênero", "Telefone", "CPF", "Data Nascimento", "Matéria de Ensino"))
        print("- "*88)
        for i in professores:
            print("{:<9}{:<50}{:<7}{:<11}{:<16}{:<16}{:<17}{:<50}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        print("-"*176)
        input("    Aperte ENTER para continuar...")
        
    def ver_alunos(self):
        # ('CW50T1A', 'Isaac de Medeiros', 20, 'Masculino', '(11) 91234-5678', '123.456.789-00', '2005-03-15', 'Campus Centro', 'Análise e Desenvolvimento de Sistemas', 'Turma A', 'Matutino')
        alunos = read.ver_alunos()
        print("-"*246)
        print("{:<9}{:<50}{:<7}{:<11}{:<16}{:<16}{:<17}{:<50}{:<50}{:<10}{:<10}".format("ID", "Nome", "Idade", "Gênero", "Telefone", "CPF", "Data Nascimento", "Campus", "Curso", "Turma", "Periodo"))
        print("- "*123)
        for i in alunos:
            print("{:<9}{:<50}{:<7}{:<11}{:<16}{:<16}{:<17}{:<50}{:<50}{:<10}{:<10}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        print("-"*246)
        input("    Aperte ENTER para continuar...")
    
    def deletar_professor(self):
        # Passar o deletar_conta() para reomver do Login, Professores e Matéria.
        pass
    
    def deletar_aluno(self):
        # Passar o deletar_conta() para remover do Login, Alunos, Matérias e Faltas
        pass
    
    def adicionar_materia(self):
        # Cria uma matéria no sistema
        while True:
            nome_materia = input("Insira o nome da Matéria: ")
            carga_horaria = utils.pegar_carga_horaria()
            print(f"As informações\nMatéria: {nome_materia}\nCarga Horária: {carga_horaria} horas")
            valido = input("Estão Corretas? [s/n] ").lower()
            if valido == "s":
                break
        create.adicionar_materia(nome_materia, carga_horaria)
        
    def ver_materias(self):
        # Ve as materias presentes no sistema
        materias = read.ver_materias()
        print(materias)
        print("-"*110)
        print("{:<5}{:<50}{:<50}{:<5}".format("ID", "Matéria", "Professor", "Horas"))
        print(" -"*55)
        for i in materias:
            professor = i[3] if not i[3] == None else "None"
            print("{:<5}{:<50}{:<50}{:>5}".format(i[0], i[1], professor, i[2]))
        print("-"*110)
        input("    Aperte ENTER para continuar...")
        
    def atualizar_materia(self):
        # Atualiza o nome da matéria e/ou professor 
        pass
    
    def deletar_materia(self):
        # Deleta uma matéria (provavelmente não necessário.)
        pass
        
    # ? Criar funções para Atualização de Professores e Ou alunos (informações pessoais, turmas e materias)