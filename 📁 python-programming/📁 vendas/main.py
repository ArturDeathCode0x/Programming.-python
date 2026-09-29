vendas = [1500, 2000, 800, 3500, 1200]  # vendas diárias

total_vendas = sum(vendas)
quantidade_dias = len(vendas)
media_vendas = total_vendas / quantidade_dias
maior_venda = max(vendas)
menor_venda = min(vendas)

print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Média de vendas: R$ {media_vendas:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")
