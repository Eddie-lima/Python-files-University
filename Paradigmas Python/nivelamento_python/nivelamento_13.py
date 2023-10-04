def main():
    try:
        height = float(input("Digite sua altura em metros(Ex: 1.70): ").replace(',', '.'))
        if height > 2.51:
            print("Por favor, insira os dados corretamente")
            main()
        else:
            sexo = input("Digite seu sexo (h/m): ").lower()
            if sexo == 'h':
                peso_ideal = (72.7 * height) - 58
                print(f"Seu peso ideal é aproximadamente {peso_ideal:.2f} kg.")
            elif sexo == 'm':
                peso_ideal = (62.1 * height) - 4.7
                print(f"Seu peso ideal é aproximadamente {peso_ideal:.2f} kg.")
            else:
                print("Por favor, insira 'h' para homem ou 'm' para mulher.")
                main()
    except ValueError:
        print("Por favor, insira uma altura válida (Ex: 1.70).")
        main()
main()

