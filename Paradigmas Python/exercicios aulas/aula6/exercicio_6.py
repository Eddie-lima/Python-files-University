try:
    numero = int(input("Digite o número para o qual você deseja gerar a tabuada: "))

    if numero >= 0:
        print(f"Tabuada de {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("Por favor, digite um número inteiro não negativo.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
