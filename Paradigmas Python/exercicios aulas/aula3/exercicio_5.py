#programa área círculo#

raio = float(input("Qual o raio do círculo? "))
CONST_PI = 3.14159265358979323846
area = CONST_PI * (raio**2)

perim = (CONST_PI*2)*raio

print(f"a área, perímetro, e diâmetro, respectivamente são:", area, perim, area*2)