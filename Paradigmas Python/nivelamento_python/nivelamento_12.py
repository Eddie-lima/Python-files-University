def main(nota1, nota2):
    media = (nota1 + nota2)/2
    if nota1 and nota2 > 10:
        print("Nota não válida")
    elif nota1 and nota2 < 0:
        print("Nota não válida")
    else:
        print("A média das suas notas é:",media)


nota1 = float(input("Diga sua primeira nota: "))
nota2 = float(input("Diga sua segunda nota: "))
main(nota1, nota2)