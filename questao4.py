# Programa para calcular o peso ideal de acordo com a altura e sexo
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem de altura {altura} m é: {peso_ideal:.2f} kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher de altura {altura} m é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido! Use 'M' para masculino ou 'F' para feminino.")
