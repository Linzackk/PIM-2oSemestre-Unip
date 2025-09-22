# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

import core.database.leitura as read
import core.database.gravacao as create
#from models.aluno import Aluno
from models.conta import Conta
#from models.professor import Professor
#from models.coordenacao import Coordenacao

#create.adicionar_aluno("Alice Martins", 21, "2002-05-14", "F", "12345678901", "Campus A", "Sistemas", "B", "10:00-12:00", "abc123")

# ID teste = SYJUFUA
conta = Conta("H6GU8EA")
conta.verificarInfos()
