def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota  # Retorna a nota válida
            else:
                print("Insira uma nota válida entre 0 e 10.")
        except ValueError:
            print("Insira um número válido.")

nota_lab = obter_nota("Digite a nota do trabalho em laboratório: ")
nota_AV = obter_nota("Digite a nota da avaliação semestral: ")
nota_exame = obter_nota("Digite a nota do exame final: ")

mean = nota_lab * 2 + nota_exame * 5 + nota_AV * 3

if mean <= 29:
    print(f"Reprovado nota: {mean}")
elif 30 <= mean < 50:
    print(f"Recuperação nota: {mean}")
else:
    print(f"Aprovado nota: {mean}")