N = int(input("Digite um número inteiro positivo N: "))

if N <= 0:
    print("Por favor, digite um número inteiro positivo maior que zero.")
else:
    contador = 0
    numero_impar = 1

    while contador < N:
        print(numero_impar)
        numero_impar += 2
        contador += 1
