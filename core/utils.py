# Funções de apoio
import json
from datetime import date, datetime

def importarSiglasIds():
    with open("ids-tabelas/idsBanco.json", "r") as arquivo:
        siglas = json.loads("\n".join(arquivo.readlines())) 
    return siglas

def importarSiglaFuncao():
    with open("ids-tabelas/idsFuncoes.json", "r") as arquivo:
        siglas = json.loads("\n".join(arquivo.readlines()))
    return siglas

def gerarTimestamp(dataDB: str = None):
    if not dataDB:
        data = date.today()
    else:
        data = dataDB[0]
        data = datetime.strptime(data, "%Y-%m-%d")
    valorTimeStamp = datetime(data.year, data.month, data.day)
    return int(valorTimeStamp.timestamp())

def calcularIdade(nascimento):
    return int((gerarTimestamp() - gerarTimestamp(nascimento)) / 31556926)


    