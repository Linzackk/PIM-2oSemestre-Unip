# Sistema Colaborativo de uma Plataforma de Educação Digital com apoio de Inteligência Artificial
# TODO: Classes: Conta, Aluno, Professor, Coordenação
# TODO: Banco de Dados, Tabelas: Login, Alunos, Professores, Coordenação, Campus, Cursos, Matérias e Notas

import core.database.bancoDeDados as db

# id_aluno, nome, idade, genero, data_nascimento, cpf, campus, curso, turma, horario_aula


print(db.mostrar_aluno("teste"))
print(db.mostrar_professor("0"))
print(db.mostrar_coordenacao("0"))
print(db.mostrar_curso("0"))
print(db.mostrar_campus("0"))
print(db.mostrar_materia("0"))
print(db.mostrar_login("0"))

