# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial

from core.database import read
from core.database import create
from core import criacaoClasses
from core import verificacao

# Testes:
# ? alunos = ["CW50T1A", "Z8O3J2A", "RCU91TA", "3TDZG5A"] RTRFS3A
# ? professores = ["7UC3OGP", "LOGB50P", ]
# ? coordenacao = ["YNB1JNC", "G5V0UXC", "5LQEPCC"]

# ids = {
#     "Isaac": "MG5CGRA",
#     "Andre": "CCL20KC",
#     "Arthur": "J77RH7P",
#     "Larissa": "0766Q4P",
#     "Denilson": "P9XP32P",
#     "Jose Carlos Lorand": "MJPW8SP"
# }

while True:
    #Login
    id = False 
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
    if not id:
        break
    usuario = criacaoClasses.criarUsuario(id_login)
    while True:
        escolha = usuario.escolher_opcao()
        if escolha == 0:
            break
            