class Aula:
    def __init__(self, assunto, professor, alunos):
        self.assunto = assunto
        self.professor = professor
        self.alunos = alunos

    def getListaPresenca(self):
        print(f"Aula de {self.assunto} "
              f"\nProfessor: {self.professor.nome} "
              f"\nEspecialidade: {self.professor.especialidade} "
              f"\nAlunos presentes: ")

        for aluno in self.alunos:
            print('--------------------')
            aluno.toString()