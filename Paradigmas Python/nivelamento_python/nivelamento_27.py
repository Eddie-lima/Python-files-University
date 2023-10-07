N = int(input("Digite um número inteiro positivo N: "))

if N <= 0:
    print("Por favor, digite um número inteiro positivo maior que zero.")
else:
    numero = 1

    for linha in range(1, N + 1):
        for coluna in range(linha):
            print(numero, end=" ")
            numero += 1
        print()
