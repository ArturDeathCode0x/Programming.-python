
estoque = ["monito","mouse","teclado","hedset"]
estoque.append("webcan")

posicao_teclado = estoque.index("teclado")
estoque[posicao_teclado] = ("teclado mecanico")

impressora_tem = "impressora" in  estoque

print("impressora no estoque ? ",impressora_tem)
estoque.remove("mouse")
print(estoque)