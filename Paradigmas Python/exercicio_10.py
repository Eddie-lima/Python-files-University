import math

cober_lit = 3
lit_lata = 18
preço_lata = 80

area_metros = float(input("Quantos metros quadrados serão pintados? "))

lit_necess = area_metros / cober_lit

lata_necess = math.ceil(lit_necess / lit_lata)

preço_total = lata_necess * preço_lata

resto = math.ceil(lata_necess * 18 - lit_necess)

print(f"Serão necessários",preço_total ,"reais. Sobrarão ", resto, "litros. ")