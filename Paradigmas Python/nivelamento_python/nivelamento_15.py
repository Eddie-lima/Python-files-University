def questions(question):
    while True:
        answer = input(question + "(sim/não):").lower()
        if answer == "sim":
            return True
        elif answer == "não":
            return False
        else:
            print("Responda com sim ou não")

def guiltiness(answers):
    sum_positive_answer = sum(answers)

    if sum_positive_answer == 2:
        return "Suspeita"
    elif sum_positive_answer == 3 or sum_positive_answer == 4:
        return "Cúmplice"
    elif sum_positive_answer == 5:
        return "Culpada"
    else:
        return "Inocente"

print("Responda as perguntas com sim ou não:")
questions_list = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

answers = [questions(question) for question in questions_list]
guilt = guiltiness(answers)

print(f"Você é classificado como: {guilt}")

