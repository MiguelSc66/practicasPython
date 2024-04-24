numer = int(input("ingrese un numero: "))

def collatz(number):
    secuencia = [number]
    while number != 1:
        if number % 2 == 0: # si es par lo dividimos por 2
            number = number // 2 
            # print(number)
        else: # si es impar lo multiplicamos por 3 y le sumamos 1
            number = 3 * number + 1
            # print(number)
        secuencia.append(number)
    print(secuencia)


collatz(numer)
