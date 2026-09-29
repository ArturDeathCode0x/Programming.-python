from typing import Self
class conta :
    def __init__(self):
        self.nome = 'pedro artur carvalho'
        self.saldo = 1200
    def ver_saldo(self):
        print(self.nome)
        print(f'Seu saldo {self.saldo:.2f}')
    def adicionar_saldo (self):
        recarrega = float(input('digite valor'))
        self.saldo += recarrega
        print('saldo altualizado')
conta = conta()
print('1- ver saldo                 -')
print('2- adicionar saldo           -')
print('------------------------------')

opc = int(input('Digite Sua opcão'))

if opc == 1:
    conta.ver_saldo()
elif opc == 2 :
     conta.adicionar_saldo()
     conta.ver_saldo()
