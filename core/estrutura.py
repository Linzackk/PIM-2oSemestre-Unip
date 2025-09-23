# Funções relacionadas a estilização na saída no Console

def escolher_opcao(lista: list):
    lista.insert(0, "Sair")
    
    for c, i in enumerate(lista):
        print(f"[ {c} ] - {i}")
        
    escolha = int(input("Insira sua escolha: "))
    while escolha > (len(lista) -1) or escolha < 0:
        escolha = int(input("Escolha inválida, por favor escolha novamente: "))
    return escolha