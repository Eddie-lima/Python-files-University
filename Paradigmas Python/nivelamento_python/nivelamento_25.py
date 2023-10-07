numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma_pares = 0
multiplicacao_impares = 1

if numero1 <= numero2:
    inicio = numero1
    fim = numero2
else:
    inicio = numero2
    fim = numero1

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
    else:
        multiplicacao_impares *= numero

print(f"A soma dos números pares é: {soma_pares}")
print(f"A multiplicação dos números ímpares é: {multiplicacao_impares}")
