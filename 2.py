class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def latir(self):
        print(f'Woof!')


PUG = Cachorro('Billy', 1)

print('O nome do meu PUG é:', PUG.nome)
PUG.latir()