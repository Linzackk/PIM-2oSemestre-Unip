# Funções relacionadas a verificação dos inputs no sistema
# TODO: Verificação de Usuarios, Senha, Valores de escolhas.
import string
import secrets
from core import utils

from .database import read

def gerar_id(cargo: str) -> str:
    caracteres = string.ascii_uppercase + string.digits
    id = ''.join(secrets.choice(caracteres) for _ in range(6)) + cargo[0].upper()
    return id

def criar_id(cargo: str): 
    id_existe = True
    while id_existe:
        id = gerar_id(cargo)
        id_existe = existencia_conta(id) # -> 1_402_410_240 possibilidade de contas
    return id

def existencia_conta(id: str):
    info = read.mostrar_informacao("login", id)
    if not info:
        return False
    else:
        return True
    
def identificarFuncao(id: str) -> str:
    siglas = utils.importarSiglaFuncao()
    try:
        return siglas[id[-1]]
    except KeyError:
        return False
        
def identificarId(tabela: str) -> str:
    siglas = utils.importarSiglasIds()
    try:
        return siglas[tabela]
    except KeyError:
        return False
    
def verificarCerteza(informacao: str):
    correto = input(f"A Informação {informacao} está correta? [S/N] ").upper()
    if correto == "S":
        return True
    else:
        return False

def continuarEscolha():
    sair = input("Deseja Sair? [S/N] ").upper()
    if sair == "S":
        return True
    else:
        return False

def verificarNota(nota):
    x = True if (nota >= 0 and nota <= 10) else False
    return x

def verificarTipoEntrada(tipo: str, entrada: str):
    opcoes = {
        "int": 1,
        "float": 2
    }
    a = opcoes[tipo]
    try:
        if a == 1:
            int(entrada)
        else:
            float(entrada)
        return True
    except KeyError:
        return False
    
def verificarData(data: str):
    from datetime import datetime
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False
# Criar função para validar entrada de numeros (nos menus)