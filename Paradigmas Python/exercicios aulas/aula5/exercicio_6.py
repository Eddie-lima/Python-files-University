while True:
    try:
        tabuada = int(input("Digite um número: "))
        for count in range(10):
            print("%d x %d = %d" % (tabuada, count + 1, tabuada * (count + 1)))     
        break    
    except ValueError:
        print("Digite um número válido")