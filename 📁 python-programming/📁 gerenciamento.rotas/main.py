# Exercício 4: Sistema de Logística (Busca e Extensão) A empresa "LogTrack" tem uma rota de entregas: rota = ["Sao
# Paulo", "Campinas", "Jundiai", "Sorocaba"].
# Novas cidades foram adicionadas por uma empresa parceira: novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
# 1. Unir as duas listas em uma só (usando extend).
# 2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
# 3. Exibir a lista completa e a posição encontrada.
# 4. Exibir uma mensagem final: “Sorocaba é a Xa cidade da rota”



rotas = ["são paulo","campinas","jundiai","sorocaba"]
novas_cidade = ["itu","valinhos"]
rotas.extend(novas_cidade)
sorocaba_position = rotas.index("sorocaba")
print("sorocaba é a xa cidade da rotas", sorocaba_position)

