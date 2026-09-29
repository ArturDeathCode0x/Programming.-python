quantidade_produto_100 = 0
quantidade_produto_101 = 0
quantidade_produto_102 = 0
quantidade_produto_103 = 0
quantidade_produto_104 = 0
quantidade_produto_105 = 0

total = 0

print(
    "  produto     codigo   preços"
    "\n---------------------------------------"
    "\nCachorro quente "        "100 " "R$ 1.20"
    "\nBauru simples"           "101"  "R$ 1.30"
    "\nBauru com ovo"           "102"  "R$ 1.50"
    "\nHamburguer "             "103"  "R$ 1.20"
    "\nchesseburguer "          "104"  "R$ 1.30"
    "\nRefrigerante"            "105"  "R$ 1.00\n"
)

while True:
    codigo = int(input("Digite o Codigo do produto ou 0 para encerrar: "))
    if codigo  == 0 :
        break
    if codigo > 105 or codigo <100:
        print("codigo invalido")
        # It's better to continue or re-prompt rather than break if the user just made a mistake
        continue
    quantidade = int(input("digite a quantidade desse produto :"))

    if codigo == 100:
         quantidade_produto_100 += quantidade
    elif codigo  == 101:
        quantidade_produto_101 += quantidade
    elif codigo == 102 :
        quantidade_produto_102 += quantidade
    elif codigo == 103 :
        quantidade_produto_103 += quantidade
    elif codigo == 104 :
        quantidade_produto_104 += quantidade
    elif codigo ==  105:
        quantidade_produto_105 += quantidade
    else :
        print("numero não está na lista ") # Changed from string literal to print statement

# Moved the summary printing outside the loop and fixed indentation
print(
    "\nFechamento do pedido"
    "\nCodigo - Quantidade - Preço unidade - Preço total"
)

# Reset total to 0 here to calculate the final total correctly after the loop
total = 0

if quantidade_produto_100 > 0:
    print(
        f"100\t-\t{quantidade_produto_100}\t- R$ 1.20\t-"
        f"\tR$ {quantidade_produto_100 * 1.2:.2f}"
    )
    total += quantidade_produto_100 * 1.2

if quantidade_produto_101 > 0:
    print(
        f"101\t-\t{quantidade_produto_101}\t- R$ 1.30\t-"
        f"\tR$ {quantidade_produto_101 * 1.3:.2f}"
    )
    total += quantidade_produto_101 * 1.3

if quantidade_produto_102 > 0:
    print(
        f"102\t-\t{quantidade_produto_102}\t- R$ 1.50\t-"
        f"\tR$ {quantidade_produto_102 * 1.5:.2f}"
    )
    total += quantidade_produto_102 * 1.5

if quantidade_produto_103 > 0:
    print(
        f"103\t-\t{quantidade_produto_103}\t- R$ 1.20\t-"
        f"\tR$ {quantidade_produto_103 * 1.2:.2f}"
    )
    total += quantidade_produto_103 * 1.2

if quantidade_produto_104 > 0:
    print(
        f"104\t-\t{quantidade_produto_104}\t- R$ 1.30\t-"
        f"\tR$ {quantidade_produto_104 * 1.3:.2f}"
    )
    total += quantidade_produto_104 * 1.3

if quantidade_produto_105 > 0:
    print(
        f"105\t-\t{quantidade_produto_105}\t- R$ 1.00\t-"
        f"\tR$ {quantidade_produto_105 * 1.0:.2f}"
    )
    total += quantidade_produto_105 * 1.0

print(f"\nTotal geral do pedido: R$ {total:.2f}")