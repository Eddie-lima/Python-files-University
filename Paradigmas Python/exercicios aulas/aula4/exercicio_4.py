def par_impar(number):
    if number % 2 == 0:
        print("Esse número é par")
    else:
        print("Esse número é ímpar")

def posi_nega(number):
    if number > 0:
        print("Esse número é positivo")
    else:
        print("Esse número é negativo")

number = int(input("Diga um número inteiro: "))
par_impar(number)
posi_nega(number)