# Funções relacionadas a atualizacao de informacoes
from core.database.sql import CURSOR as cursor
from core.database.sql import CONEXAO as conexao

from core.database import read
from core import verificacao
from core import estrutura
from core import utils

def atualizar_informacoes(id_conta: str, informacao: str, nova_informacao: str):
    # Acessa a Tabela da conta, filtra pelo ID e altera a informação.
    tabela = verificacao.identificarFuncao(id_conta)
    id = verificacao.identificarId(tabela)
    cursor.execute(f"UPDATE {tabela} SET {informacao} = ? WHERE {id} = ?", (nova_informacao, id_conta))  
    conexao.commit()
    
def atualizar_idade(id_conta: str):
    tabela = verificacao.identificarFuncao(id_conta)
    chave_principal = verificacao.identificarId(tabela)
    nova_idade = utils.calcularIdade(read.mostrar_informacao_filtrada(tabela, chave_principal, id_conta, "data_nascimento"))
    atualizar_informacoes(id_conta, "idade", nova_idade)
    
def atualizar_nota(id_conta: str, nota: float):
    atualizar_informacoes(id_conta, )
    
    
# ? Fazer hoje: Atualizar_Notas, Atualizar_Professores, Atualizar_Materia
    
# TODO: Atualizar_Informacoes, Atualizar_Notas, Atualizar_Professores, etc

# ! Popular a Tabela "Faltas"