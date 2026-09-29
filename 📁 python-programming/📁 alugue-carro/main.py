distancia = float(input("Digite velocidade "))

if distancia  >= 200:
    preco = distancia * 0.55
elif distancia <=200:
      preco  = distancia * 0.60

print(f"preço da passagem: R${preco:.2f}")

