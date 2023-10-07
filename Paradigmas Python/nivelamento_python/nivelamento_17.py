while True:
    try:
        distancia_km = float(input("Digite a distância em Km: "))
        if distancia_km > 0:
            break
        else:
            print("Digite um valor válido para a distância.")
    except ValueError:
        print("Digite um valor válido para a distância.")

while True:
    try:
        litros_gasolina = float(input("Digite a quantidade de litros de gasolina consumidos: "))
        if litros_gasolina > 0:
            break
        else:
            print("Digite um valor válido para a quantidade de litros de gasolina.")
    except ValueError:
        print("Digite um valor válido para a quantidade de litros de gasolina.")

consumo_kmpl = distancia_km / litros_gasolina

if consumo_kmpl < 8:
    print("Venda o carro!")
elif 8 <= consumo_kmpl <= 12:
    print("Econômico")
else:
    print("Super econômico")
