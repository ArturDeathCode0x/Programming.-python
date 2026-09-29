salário = float(input("Digite o salário atual: "))
p_aumento = float(input("Digite a porcentagem de aumento: "))

aumento = salário * p_aumento / 100
novo_salário = salário + aumento

print("Um aumento de %.2f%% em um salário de R$ %.2f" % (p_aumento, salário))
print("Resultando em um novo salário de R$ %.2f" % novo_salário)