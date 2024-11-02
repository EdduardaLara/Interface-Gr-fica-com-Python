# Programa para manipular sequência de números
numeros = []
while True:
    num = int(input("Digite um número (negativo para parar): "))
    if num < 0:
        break
    numeros.append(num)

if numeros:
    # Soma dos números positivos
    soma = sum(numeros)
    # Média de todos os números
    media = soma / len(numeros)
    # Número com maior valor
    maior = max(numeros)
    # Números negativos (caso tenha sido digitado algum antes do encerramento)
    negativos = [n for n in numeros if n < 0]

    print("Soma dos números positivos:", soma)
    print("Média dos números:", media)
    print("Maior número:", maior)
    print("Números negativos digitados:", negativos)
else:
    print("Nenhum número positivo foi digitado.")
