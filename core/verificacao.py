# Funções relacionadas a verificação dos inputs no sistema
# TODO: Verificação de Usuarios, Senha, Valores de escolhas.
import string
import secrets
from core import utils

from .database import leitura as read_info

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
    info = read_info.mostrar_informacao("login", id)
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
