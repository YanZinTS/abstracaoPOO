class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2


    def calcular_media(self):
        calc = (self.nota1 + self.nota2) / 2
        return calc


InformacoesAluno = Aluno('Yan', 10, 9)

print('O nome do aluno é', InformacoesAluno.nome)
print('Sua média de notas é:', InformacoesAluno.calcular_media())