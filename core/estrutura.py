# Funções relacionadas a estilização na saída no Console
from core import verificacao

def escolher_opcao(lista: list, mensagem=""):
    lista.insert(0, "Sair")
    if mensagem != "":
        print(f"{mensagem}".upper().center(50))
    for c, i in enumerate(lista):
        print(f"[ {c} ] - {i}")
    print("-" * 50)
    
    escolha = input("Insira sua escolha: ")
    escolha_valida = verificacao.verificarTipoEntrada("int", escolha)
    
    while escolha_valida and int(escolha) > (len(lista) -1) or escolha_valida and int(escolha) < 0:
        escolha = input("Escolha inválida, por favor escolha novamente: ")
        escolha_valida = verificacao.verificarTipoEntrada("int", escolha)
        
    return int(escolha)