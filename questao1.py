# Programa para calcular o valor da conta com desconto
conta = float(input("Digite o valor da conta: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

# Cálculo do valor com desconto
valor_com_desconto = conta - (conta * desconto / 100)

# Exibe o resultado
print(f"O valor da conta com {desconto}% de desconto é: R$ {valor_com_desconto:.2f}")
