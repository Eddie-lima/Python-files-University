soma = 0
contador = 0

while contador < 10:
    try:
        numero = int(input(f"Digite o {contador + 1}º número inteiro positivo: "))
        if numero > 0:
            soma += numero
            contador += 1
        else:
            print("Digite um número inteiro positivo.")
    except ValueError:
        print("Digite um número inteiro válido.")

if contador > 0:
    media = soma / contador
    print(f"A média dos {contador} números inteiros positivos é: {media}")
else:
    print("Nenhum número inteiro positivo foi inserido.")
