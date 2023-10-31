def main():
    salarios = []
    filhos = []

    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario < 0:
                break
            salarios.append(salario)

            nmr_filhos = int(input("Digite quantos filhos você tem: "))
            if nmr_filhos >= 0:
                filhos.append(nmr_filhos)
            else:
                print("Digite um valor válido")
        except ValueError:
            print("Digite um valor válido")

    if len(salarios) > 0:
        media_salario = sum(salarios) / len(salarios)
        print(f"Média de salário: {media_salario}")

        maior_salario = max(salarios)
        print(f"Maior salário: {maior_salario}")
        
        salario_menor_150 = len([s for s in salarios if s < 150])
        porcentagem_menor_150 = (salario_menor_150 / len(salarios)) * 100
        print(f"Porcentagem de salários menores que 150 reais: {porcentagem_menor_150:.2f}%")

    if len(filhos) > 0:
        media_filhos = sum(filhos) / len(filhos)
        print(f"Média de filhos: {media_filhos}")

main()
