# Funções relacionadas a estilização na saída no Console
from core import verificacao

def escolher_opcao(lista: list, mensagem=""):
    lista.insert(0, "Sair")
    print("-"*50)
    if mensagem != "":
        print(f"{mensagem}\n".upper().center(50))
    for c, i in enumerate(lista):
        print(f"[ {c} ] - {i}")
    print("-" * 50)
    
    escolha = input("Insira sua escolha: ")
    escolha_valida = verificacao.verificarTipoEntrada("int", escolha)
    
    while not escolha_valida or not (0 <= int(escolha) < len(lista)):
        escolha = input("Escolha inválida, por favor escolha novamente: ")
        escolha_valida = verificacao.verificarTipoEntrada("int", escolha)
    return int(escolha)