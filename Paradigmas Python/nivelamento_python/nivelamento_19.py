soma = 0

for i in range(10):
    while True:
        try:
            valor = float(input(f"Digite o {i + 1}º valor: "))
            soma += valor
            break
        except ValueError:
            print("Digite um valor numérico válido.")

print(f"A soma dos 10 valores é: {soma}")
