estimativaVida = 100
vidaExpira = 10

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
quantidadeCigarro = int(input("Digite quantos cigarros fuma por dia: "))
quantosAnos = int(input("Digite há quantos anos fuma: "))

# Cada cigarro representa 10 minutos
perde = quantidadeCigarro * quantosAnos * 365 * vidaExpira

# Convertendo minutos para horas
horasPerdidas = perde / 60

# Convertendo horas para dias
diasPerdidos = horasPerdidas / 24

print(f"\nNome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cigarros por dia: {quantidadeCigarro}")
print(f"Anos fumando: {quantosAnos}")
print(f"Estimativa de tempo perdido: {diasPerdidos:.2f} dias")