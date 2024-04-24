# Ejercicio 1
num = int(input('ingrese numero: '))
cadena_num = str(num)
lon = len(cadena_num)
if lon == 3:
    invert = cadena_num[::-1]
    print(invert)
else: 
    print('ingrese un numero de tres digitos')

