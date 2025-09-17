# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

import core.database.leitura as read_info
import core.database.gravacao as create_info


print(read_info.mostrar_informacao("alunos", "RGNJ0GA"))
# nome, idade, data_nascimento, genero, cpf, campus, curso, turma, horario_aula, senha="123"
create_info.adicionar_aluno("Isaac", 35, "1990-06-15", "Masculino", "123.456.789-00", "Chácara Santo Antônio", "ADS", "DS1A40", "Noturno")

# ids = ["RGNJ0GA", "HVNFVOP", "L63Y6NC", "MZN2EHA"]