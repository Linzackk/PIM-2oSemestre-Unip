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

def mostrar_dupla_condicao(tabela, id1, id2, chave1, chave2):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave1} = ? AND {chave2} = ?", (id1, id2)).fetchall()
    return informacao

def mostrar_tripla_condicao(tabela, id1, id2, id3, chave1, chave2, chave3):
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave1} = ? AND {chave2} = ? AND {chave3} = ?", (id1, id2, id3)).fetchall()
    return informacao

def mostrar_informacao_completa(tabela: str, id: str, chave_principal: str):
    if tabela in "alunosprofessorescoordenacao":
        update.atualizar_idade(id)
    informacao = cursor.execute(f"SELECT * FROM {tabela} WHERE {chave_principal} = ?", (id, )).fetchall()
    return informacao

def mostrar_tabela_completa(tabela):
    return cursor.execute(f"SELECT * FROM {tabela}").fetchall()

def pegar_infos_nota(id_aluno):
    informacao = cursor.execute("""
                                SELECT 
                                    notas.nota,
                                    materias.materia AS nome_materia,
                                    professores.nome AS nome_professor,
                                    notas.data_prova as data
                                FROM notas
                                INNER JOIN materias 
                                    ON CAST(notas.materia_id AS INTEGER) = materias.materia_id
                                INNER JOIN professores 
                                    ON materias.id_professor = professores.id_professor
                                WHERE notas.id_aluno = ?;
                                """, (id_aluno,)).fetchall()
    return informacao

def ver_faltas(id_aluno):
    info = cursor.execute("""
                          SELECT faltas.quantidade, 
                          materias.materia as nome_materia
                          FROM faltas
                          INNER JOIN materias
                            ON CAST(faltas.materia_id AS INTEGER) = materias.materia_id
                          WHERE id_aluno = ?;
                          """, (id_aluno, )).fetchall()
    return info

def ver_materias():
    info = cursor.execute("""
                            SELECT materias.materia_id,
                                materias.materia as nome_materia,
                                materias.carga_horaria,
                                professores.nome
                            FROM materias
                            INNER JOIN professores
                                ON CAST(professores.id_professor AS TEXT) = materias.id_professor
                          """).fetchall()
    return info