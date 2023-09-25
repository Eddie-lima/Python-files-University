numbers = []

while len(numbers) < 3:
    n = float(input("Digite um número: "))

    if n in numbers:
        print("Este número já foi inserido. Insira um número diferente.")
    else:
        numbers.append(n)

numbers.sort()

print(numbers[0],numbers[1],numbers[2])