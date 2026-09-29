print("qual velocidade do carro")
velocidade = int(input("Digite Velocidade do carro "))

if velocidade > 60 :
    multa =(velocidade - 60)*5
    print (" voce foi multado")
    print(f'Valor da multa R${multa:.2f}')
else :
    print("sem multa  irmão ")



