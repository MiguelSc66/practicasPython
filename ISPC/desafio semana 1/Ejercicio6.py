numer = int(input("ingrese la cantidad de renglones: "))

def triangulo_rectangulo(numero): 
    primer = 2
    for f in range(1, numero + 1):
        # print(f, 'testt')
        for c in range(1, f + 1):
            # print(c, 'test')
            print(primer + (c-1) * 2, end=" ")
        print()

triangulo_rectangulo(numer)
