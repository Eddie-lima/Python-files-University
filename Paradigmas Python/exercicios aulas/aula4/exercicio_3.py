while True:
    age = int(input("Idade do nadador: "))

    if age >= 5:
        if age >= 18:
            print("Adulto")
        elif age >= 5 and age <= 7:
            print("Infantil A")
        elif age >= 8 and age <= 10:
            print("Infantil B")
        elif age >= 11 and age <= 13:
            print("Juvenil A")
        elif age >= 14 and age <= 17:
            print("Juvenil B")
        break
    else:
        print("A idade do nadador deve ser maior ou igual a 5 anos.")