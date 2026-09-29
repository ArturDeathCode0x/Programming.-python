salario = int(input(""))
porcentagem = int(input(""))

aumento = salario * (porcentagem / 100)
Novosalario = aumento + salario

print(f" seu aumento foi : {aumento:.2f}")
print(f" seu novo salario :{Novosalario:.1f}")