while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

while True:
    try:
        numero2 = int(input("Digite o segundo número: "))
        break 
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

contador = 0

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        contador += 1

print(f"A quantidade de números pares entre {numero1} e {numero2} é {contador}")
