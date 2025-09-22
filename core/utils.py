# Funções de apoio
import json

def importarSiglasIds():
    with open("ids-tabelas/idsBanco.json", "r") as arquivo:
        siglas = json.loads("\n".join(arquivo.readlines())) 
    return siglas

def importarSiglaFuncao():
    with open("ids-tabelas/idsFuncoes.json", "r") as arquivo:
        siglas = json.loads("\n".join(arquivo.readlines()))
    return siglas

def identificarFuncao(id: str) -> str:
    siglas = importarSiglaFuncao()
    return siglas[id[-1]]
    
    