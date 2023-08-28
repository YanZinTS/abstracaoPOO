class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

Pessoa1 = Pessoa('Yan', 16)
Pessoa2 = Pessoa('Bruno', 27)

print('Meu nome é', Pessoa1.nome)
print('A idade de Bruno é:', Pessoa2.idade)