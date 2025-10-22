# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

from core.database import read
from core.database import create
from core import criacaoClasses
from core import verificacao
# Testes:
# ? alunos = ["CW50T1A", "Z8O3J2A", "RCU91TA", "3TDZG5A"]
# ? professores = ["7UC3OGP", "LOGB50P", ]
# ? coordenacao = ["YNB1JNC", "G5V0UXC", "5LQEPCC"]

# ! Agora as senhas são salvas como strings padrão, mudar para o hash das senhas para segurança

while True:
    #Login
    id = False # ! Mudar para falso para entrar na área de login
    while not id:
        print("-"*50)
        id_login = input("Insira seu ID para Login [0 - Sair]\n")
        if id_login == "0":
            break
        senha = input("Insira sua Senha: ")
        
        id = verificacao.existencia_conta(id_login)
        if not verificacao.validar_senha(senha, id_login) and id:
            print("Informações Incorretas. Por favor insira novamente.")
            id = False
        
    #id_login = "YNB1JNC" # ! APENAS PARA TESTES EVITANDO AREA DE LOGIN

    if not id:
        break
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
            if escolha == 4:
                usuario.ver_faltas()
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

