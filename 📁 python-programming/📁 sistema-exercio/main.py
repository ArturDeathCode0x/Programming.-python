# ===== FUNÇÕES =====

def ex1():
    km = float(input("Km percorridos: "))
    dias = int(input("Dias alugados: "))
    preco = (dias * 60) + (km * 0.15)
    print(f"Total a pagar: R$ {preco:.2f}")


def ex2():
    cigarros = int(input("Cigarros por dia: "))
    anos = int(input("Anos fumando: "))
    total = cigarros * 365 * anos
    minutos = total * 10
    dias = minutos / (60 * 24)
    print(f"Dias de vida perdidos: {dias:.2f}")


def ex3():
    vel = float(input("Velocidade (km/h): "))
    if vel > 80:
        multa = (vel - 80) * 5
        print(f"Multado! Valor: R$ {multa:.2f}")
    else:
        print("Sem multa")


def ex4():
    salario = float(input("Salário: R$ "))
    porc = float(input("Aumento (%): "))
    aumento = salario * (porc / 100)
    print(f"Aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {salario + aumento:.2f}")


def ex5():
    preco = float(input("Preço do produto: R$ "))
    desc = float(input("Desconto (%): "))
    valor_desc = preco * (desc / 100)
    print(f"Desconto: R$ {valor_desc:.2f}")
    print(f"Preço final: R$ {preco - valor_desc:.2f}")


def ex6():
    salario = float(input("Salário: R$ "))
    if salario > 1250:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.15
    print(f"Novo salário: R$ {salario + aumento:.2f}")


def ex7():
    km = float(input("Distância (km): "))
    if km <= 200:
        preco = km * 0.50
    else:
        preco = km * 0.45
    print(f"Preço da passagem: R$ {preco:.2f}")


def ex8():
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    op = input("Operação (+ - * /): ")

    if op == "+":
        print(f"Resultado: {n1 + n2}")
    elif op == "-":
        print(f"Resultado: {n1 - n2}")
    elif op == "*":
        print(f"Resultado: {n1 * n2}")
    elif op == "/":
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: divisão por zero")
    else:
        print("Operação inválida")


# ===== MENU =====

while True:
    print("\n===== SISTEMA PROVA =====")
    print("1 - Aluguel de carro")
    print("2 - Vida de fumante")
    print("3 - Multa velocidade")
    print("4 - Aumento salário (%)")
    print("5 - Desconto produto")
    print("6 - Aumento automático")
    print("7 - Passagem viagem")
    print("8 - Calculadora")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        ex1()
    elif op == "2":
        ex2()
    elif op == "3":
        ex3()
    elif op == "4":
        ex4()
    elif op == "5":
        ex5()
    elif op == "6":
        ex6()
    elif op == "7":
        ex7()
    elif op == "8":
        ex8()
    elif op == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")