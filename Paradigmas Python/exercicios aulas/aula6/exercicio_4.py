while True:
    try:
        numero = int(input("Digite um número para calcular o fatorial: "))
        if numero < 0:
            print("O fatorial não está definido para números negativos.")
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f"O fatorial de {numero} é {fatorial}")
            break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
