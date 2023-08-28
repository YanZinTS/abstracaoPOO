class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero


    def Depositar(self, valor):
        self.saldo = self.saldo + valor


    def Sacar(self, tirar):
        self.saldo = self.saldo - tirar


    def ExibirSaldo(self):
        print(f'Meu saldo é de: R${self.saldo}')


PessoaDono = ContaBancaria('Yan', 1200, 5791)

PessoaDono.Depositar(500)
PessoaDono.Sacar(700)

PessoaDono.ExibirSaldo()