#29/08/23 - Paradigmas de Linguagens Python#
def main():
    try:  
            horas_mes = int(input("Quantas horas foram trabalhadas neste mês? "))
            valor_hora = float(input("Quanto vale uma hora trabalhada? "))

            total = horas_mes * valor_hora
            if horas_mes <= 672:
                print("Você ganhou esse mês:", int(total))
            else:
                print("Vocẽ não pode trabalhar mains que 672 horas em um mês")
                main()
    except ValueError:
        print("Insira um valor valido")
        main()
main()