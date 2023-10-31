try:
    numero = int(input("Digite um número inteiro: "))
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        soma_divisores = 0
        for i in range(1, numero):
            if numero % i == 0:
                soma_divisores += i
        print(f"A soma de todos os divisores de {numero} é {soma_divisores}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")