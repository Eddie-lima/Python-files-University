#Programa nmrs inteiros#

nmr_int1 = int(input("Me dê um número inteiro: "))
nmr_int2 = int(input("Me dê outro número inteiro: "))
nmr_real = float(input("Agora me dê um número real: "))

a = (2 * nmr_int1) * (nmr_int2 / 2)
b = 3 * nmr_int1 + nmr_real
c = nmr_real**3

print("O produto do dobro do primeiro com metade do segundo é: ", a)
print("A soma do triplo do primeiro com o terceiro é: ", b)
print("o terceiro elevado ao cubo é: ", c)