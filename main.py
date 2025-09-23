# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

from core.database import read
from core.database import create
from core import criacaoClasses
from core import verificacao

# ID coordenador Teste: LYYPU9C
# ID professor Teste: G8CKQXP
# Id Aluno Teste: L0XH2CA

#Login
id = True # ! Mudar para falso para entrar na área de login
while not id:
    id_login = input("Insira seu ID para Login [0 - Sair]\n")
    if id_login == 0:
        break
    id = verificacao.existencia_conta(id_login)
id_login = "OU84JKA" # ! APENAS PARA TESTES EVITANDO AREA DE LOGIN
if id:
    usuario = criacaoClasses.criarUsuario(id_login)
usuario.mostrar_info()
usuario.atualizar_informacao()
usuario.mostrar_info()
#lista = ["Aluno - OU84JKA", "Professor - G8CKQXP", "Coordenador - LYYPU9C"]

