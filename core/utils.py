# Funções de apoio
import json
from datetime import date, datetime
from core.database import read
from core import verificacao

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

def pegarIdMateria(materia):
    return read.mostrar_informacao_filtrada("materias", "materia", materia, "materia_id")

def pegar_data():
    dia = input("Insira o Dia: ")
    mes = input("Insira o Mes: ")
    ano = input("Insira o Ano: ")
    data = ""
    if verificacao.verificarTipoEntrada("int", dia) and verificacao.verificarTipoEntrada("int", mes) and verificacao.verificarTipoEntrada("int", ano):
        data = f"{ano}-{mes}-{dia}"
    return data

def pegar_telefone():
    while True:
        ddd = input("Insira o DDD: ")
        numero = input("Insira o seu numero de telefone celular: ")
        if ddd.isnumeric() and numero.isnumeric():
            numero_formatado = f"({ddd}) {numero[:5]}-{numero[5:]}"
            if len(numero_formatado) == 15:
                return f"({ddd}) {numero}"
        print("Telefone inválido, por favor escreva novamente")
    
def pegar_cpf():
    while True:
        cpf = input("Insira seu CPF (apenas numeros): ")
        if cpf.isnumeric() and len(cpf) == 11:
            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        print("Cpf inválido, por favor escreva novamente.")