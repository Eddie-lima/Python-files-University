nmrA = int(input("Diga um número inteiro: "))
nmrB = int(input("Diga mais um número inteiro: "))
nmrC = int(input("Diga outro número inteiro: "))

if nmrA == nmrB == nmrC:
    print("Todos os números são iguais")

else:
    maior = max(nmrA, nmrB, nmrC)
    menor = min(nmrA, nmrB, nmrC)

    print(f"O maior número é {maior}")
    print(f"O menor número é {menor}")