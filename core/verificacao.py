# Funções relacionadas a verificação dos inputs no sistema
# TODO: Verificação de Usuarios, Senha, Valores de escolhas.
import string
import secrets

from .database import bancoDeDados as infosdb

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
    info = infosdb.mostrar_login(id)
    if not info:
        return False
    else:
        return True
    
