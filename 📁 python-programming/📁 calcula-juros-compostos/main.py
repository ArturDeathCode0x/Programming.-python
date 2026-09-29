# A célula contém instruções em português, não código Python. Abaixo está uma sugestão de código para a tarefa.

deposito_inicial = 5000.00
taxa_juros_anual = 0.03 # 3%
taxa_juros_mensal = taxa_juros_anual / 12

saldo = deposito_inicial
juros_ganhos_total = 0

print(f"Depósito Inicial: R$ {deposito_inicial:.2f}")
print(f"Taxa de Juros Mensal: {taxa_juros_mensal*100:.2f}%")
print("----------------------------------------")

for mes in range(1, 25):
    juros_do_mes = saldo * taxa_juros_mensal
    saldo += juros_do_mes
    juros_ganhos_total += juros_do_mes
    print(f"Mês {mes:2d}: Saldo R$ {saldo:.2f} (Juros do mês R$ {juros_do_mes:.2f})")

print("----------------------------------------")
print(f"Total ganho com juros em 24 meses: R$ {juros_ganhos_total:.2f}")