while(True):
    salario1 = float(input("Salário do primeiro mês: "))
    salario2 = float(input("Salário do segundo mês: "))
    salario3 = float(input("Salário do terceiro mês: "))

    media_salario = (salario1+salario2+salario3)/3

    print("A média do seu salário durante os últimos 3 meses é aproximadamente:", (media_salario))

    continua = input("Deseja continuar? (s/n): ")
    if continua == 'n':
        break