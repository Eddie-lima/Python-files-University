while True:
    try:
        base = float(input("Digite a base: "))
        break
    except ValueError:
        print("Por favor, digite um número válido para a base.")

while True:
    try:
        expoente = int(input("Digite o expoente: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido para o expoente.")

resultado = 1

if expoente == 0:
    resultado = 1
elif base == 0:
    resultado = 0
elif expoente > 0:
    for _ in range(expoente):
        resultado *= base
else:
    for _ in range(-expoente):
        resultado /= base

print(f"{base} elevado a {expoente} é igual a {resultado}")
