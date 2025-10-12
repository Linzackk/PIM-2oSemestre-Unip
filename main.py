# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

from core.database import read
from core.database import create
from core import criacaoClasses
from core import verificacao

# Testes:
# alunos = ["CW50T1A", "Z8O3J2A", "RCU91TA"]
# professores = ["7UC3OGP", "LOGB50P", ]
# coordenacao = ["YNB1JNC", "G5V0UXC", "5LQEPCC"]

#Login
id = True # ! Mudar para falso para entrar na área de login
while not id:
    id_login = input("Insira seu ID para Login [0 - Sair]\n")
    if id_login == 0:
        break
    id = verificacao.existencia_conta(id_login)
id_login = "CW50T1A" # ! APENAS PARA TESTES EVITANDO AREA DE LOGIN

if id:
    usuario = criacaoClasses.criarUsuario(id_login)
    while True:
        # Mostra o menu:
        escolha = usuario.mostrar_menu()
        if escolha == 0:
            break
        if escolha == 1:
            usuario.mostrar_info()
        if escolha == 2:
            usuario.atualizar_informacao()
        if id_login[-1] == "A":
            if escolha == 3:
                usuario.ver_notas()
        if id_login[-1] == "P":
            if escolha == 3:
                usuario.postar_nota()
            if escolha == 4:
                usuario.subir_falta()
        if id_login[-1] == "C":
            if escolha == 3:
                usuario.adicionar_aluno()
            if escolha == 4:
                usuario.adicionar_professor()
# Testar se o menu é melhor criar aqui no main com diversos if elses ou nas respectivas classes
#usuario.mostrar_info()

