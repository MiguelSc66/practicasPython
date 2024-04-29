filAlf = int(input('Fila Alfil: '))
colAlf = int(input('columna Alfil: '))
filTor = int(input('Fila Torre: '))
colTor = int(input('columna Torre: '))

def validador(fila, columna):
    if fila < 1 or fila > 8 or columna > 1 or columna < 1:
        return False
    else:
        return True

if validador(filAlf, colAlf) or validador(filTor, colTor):
    print('Error, coordenadas fuera de rango')
else:
    if filAlf == filTor or colAlf == colTor:
        print('La torre captura')
    elif abs(filAlf - filTor) == abs(colAlf - colTor):
        print('El alfil captura')
    else:
        print('No hay captura')