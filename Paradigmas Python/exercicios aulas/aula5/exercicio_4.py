def factorial(num):
    if num < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

num = int(input("Diga um número: "))
fatorial = factorial(num)

if isinstance(fatorial, int):
    print(f"O fatorial de {num} é {fatorial}.")
else:
    print(fatorial)
