number1 = int(input("Diga um número: "))
number2 = int(input("Diga outro número: "))

while number1 <= number2:
    if number1 % 2 == 0:
        print(number1)
    number1 += 1


print(f"A quantidade de números pares entre {number1} e {number2} é {count}")
