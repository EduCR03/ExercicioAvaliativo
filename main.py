import AulaDB
from Aluno import Aluno
from Aula import Aula
from Professor import Professor

CRUD = str(input('Ecolha um metodo CRUD (Create, Read, Update, Delete: '))
if CRUD == 'Create':
    aulaNome = str(input('Entre com a materia: '))

    professorNome = str(input('Entre com o nome do professor: '))

    professorEspecialidade = str(input('Entre com a especialidade: '))

    numAlunos = int(input('Insira quantos alunos terao na aula: '))
    alunos = []
    aux = 0
    while aux < numAlunos:
        nome = str(input('Entre com um nome: '))
        matricula = int(input('Entre com a matricula: '))
        curso = str(input('Entre com o curso: '))
        periodo = int(input('Entre com o periodo: '))

        aluno = Aluno(nome, matricula, curso, periodo)
        alunos.append(aluno)
        aux +=1

    professor = Professor(professorNome, professorEspecialidade)

    aula = Aula(aulaNome, professor, alunos)
    print('---------------------------------')
    aula.getListaPresenca()

    AulaDB.create(aula)

if CRUD == 'Read':
    AulaDB.read()

if CRUD == 'Update':
    assunto = str(input('Insira qual aula atualizar o assunto: '))
    professorNome = str(input('Insira o nome de outro professor: '))
    AulaDB.udate(assunto, professorNome)

if CRUD == 'Delete':
    assunto = str(input('Insira qual materia remover: '))
    AulaDB.delete(assunto)


