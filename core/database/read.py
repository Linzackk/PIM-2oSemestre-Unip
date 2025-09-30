from core.database.sql import CURSOR as cursor
from core.database.sql import CONEXAO as conexao

from core import utils
from core import verificacao

from core.database import update

def mostrar_informacao_filtrada(tabela, chave_principal, id, chave_alvo):
    informacao = cursor.execute(f"SELECT {chave_alvo} FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchone()
    return informacao

def mostrar_informacao(tabela, id):
    id_tabela = verificacao.identificarId(tabela)
    if not id_tabela:
        return False
    return mostrar_informacao_completa(tabela, id, id_tabela)

def mostrar_informacao_completa(tabela: str, id: str, chave_principal: str):
    if tabela in "alunosprofessorescoordenacao":
        update.atualizar_idade(id)
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao

def mostrar_tabela_completa(tabela):
    return cursor.execute(f"SELECT * FROM {tabela}").fetchall()
