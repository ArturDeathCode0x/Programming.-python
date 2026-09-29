estoque = ["monitor", "teclado", "mouse", "headset"]

# 1. Adicionar webcam
estoque.append("webcam")

# 2. Atualizar teclado
indice = estoque.index("teclado")
estoque[indice] = "teclado mecanico"

# 3. Verificar impressora
print("impressora" in estoque)

# 4. Remover mouse
estoque.remove("mouse")

print(estoque)