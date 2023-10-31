try:
    n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))
    if n <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        fib = [1, 1]

        if n == 1:
            print("Série de Fibonacci até o 1º termo: [1]")
        elif n == 2:
            print("Série de Fibonacci até o 2º termo: [1, 1]")
        else:
            for i in range(2, n):
                next_term = fib[i - 1] + fib[i - 2]
                fib.append(next_term)

            print(f"Série de Fibonacci até o {n}° termo: {fib}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
