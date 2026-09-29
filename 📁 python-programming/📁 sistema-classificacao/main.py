# Exercício 3: Organização de Preços (Ordenação e Slicing) uma importadora listou os preços de frete em dólar:
# fretes = [50, 80, 20, 150, 40]. Para apresentar em uma reunião, você deve:
# 1. Ordenar a lista do maior para o menor preço.
# 2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova lista chamada top_fretes.
# 3. Exibir a lista original ordenada e a lista dos top_fretes.



fretes = [50, 80, 20 ,150 ,40]
ordenar = sorted(fretes, reverse=True)

top_fretes = ordenar[:2]

print(f"Lista original ordenada (do maior para o menor): {ordenar}")


print(f"Os 2 fretes mais caros: {top_fretes}")