try:
    n = int(input("Digite um número inteiro e positivo (n): "))
    if n <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        h = 0.0
        for i in range(1, n + 1):
            h += 1 / i
        print(f"O valor harmônico H({n}) é {h:.6f}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
