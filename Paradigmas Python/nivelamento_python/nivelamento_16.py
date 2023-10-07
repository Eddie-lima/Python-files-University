def age_loop():
    while True:
        try:
            age = int(input("Insira sua idade: "))
            if age >= 0:
                return age
            elif age <= 120:
                return age
            else:
                print("Insira uma idade válida")
        except ValueError:
            print("Insira uma idade válida")

def service_loop(age):
    while True:
        try:
            service_time = int(input("Digite a quantidade de anos que trabalhou: "))
            if 0 <= service_time <= age:
                return service_time
            else:
                print("Insira um tempo de serviço válido")
        except ValueError:
            print("Insira um tempo de serviço válido")

age = age_loop()

service_time = service_loop(age)

if age >= 65:
    print("O trabalhador pode se aposentar")
elif service_time >= 30:
    print("O trabalhador pode se aposentar")
elif age >= 60 and service_time >= 25:
    print("O trabalhador pode se aposentar")
else:
    print("Vai trabalhar mais rei")
