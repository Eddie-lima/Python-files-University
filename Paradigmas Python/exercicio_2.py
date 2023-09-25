horas_prova = int(input("Quantas horas a prova teve? "))
minuto_prova = int(input("Quantos minutos a prova teve? "))

resul_minu = horas_prova * 60
resul_sec = (resul_minu + minuto_prova) * 60

print(f"Sua prova teve {resul_minu + minuto_prova} minutos")
print(f"Sua prova teve {resul_sec} segundos")