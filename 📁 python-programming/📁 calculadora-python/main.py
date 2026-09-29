num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("=======================================")
print("=       escolha sua operação           =")
print("=======================================")
print("= 0-sair                               =")
print("= 1- adição                            =")
print("= 2- subtração                         =")
print("= 3- multiplicação                     =")
print("= 4- divisão                           =")
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "1":
    resultado = num1 + num2
elif operacao == "2":
    resultado = num1 - num2
elif operacao == "3":
    resultado = num1 * num2
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")