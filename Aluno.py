from Pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso, periodo):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self. periodo = periodo

    def toString(self):
        print(f'nome: {self.nome} '
              f'\ncurso: {self.curso} '
              f'\nmatricula: {self.matricula} '
              f'\nperiodo: {self.periodo}')