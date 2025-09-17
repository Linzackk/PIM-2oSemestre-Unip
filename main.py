# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

import core.database.leitura as read_info
import core.database.gravacao as create_info


print(read_info.mostrar_informacao("alunos", "RGNJ0GA"))

# ids = ["RGNJ0GA", "HVNFVOP", "L63Y6NC", "MZN2EHA"]