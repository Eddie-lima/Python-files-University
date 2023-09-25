cargo = int(input("Digite o código do seu cargo: "))
salario = float(input("Digite o valor do seu salário: "))

if cargo == 310 or cargo == 456 or cargo == 885:
    if cargo == 310:
        salario_novo = salario + (salario * 0.05)

    elif cargo == 456:
        salario_novo = salario + (salario * 0.075)

    elif cargo == 885:
        salario_novo = salario + (salario * 0.1)
else:
    salario_novo = salario + (salario * 1.5)

diferenca = salario_novo - salario

print(f"Seu salário novo é R${salario_novo}.\nSeu salário antigo era R${salario}.\nA diferença entre esses salários é R${diferenca}")