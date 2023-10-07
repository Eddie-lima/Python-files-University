N = int(input("Digite um número inteiro positivo N: "))

if N < 0:
    print("Por favor, digite um número inteiro positivo ou igual a zero.")
else:
    for i in range(N + 1):
        print(i)
