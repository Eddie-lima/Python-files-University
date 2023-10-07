soma = 0

for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número inteiro: "))
            soma += numero
            break
        except ValueError:
            print("Digite um número inteiro válido.")

media = soma / 10

print(f"A média dos 10 números inteiros é: {media}")
