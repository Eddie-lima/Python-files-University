while True:
    try:
        salario = float(input("Digite seu salário: "))
        break
    except ValueError:
        print("Digite um salário válido: ")



while True:
    try:
        nmr_filhos = int(input("Digite quantos filhos você tem: "))
        if nmr_filhos >= 0:
            break
        else:
            print("Digite uma valor válido")
    except ValueError:
        print("Digite uma valor válido")

mean = 