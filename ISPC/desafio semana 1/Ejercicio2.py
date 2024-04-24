# Ejercicio 2
time = int(input('ingrese la hora actual: '))
future_time = int(input('ingrese la cantidad de horas: '))
# indicar que hora marcara el reloj dentro de future_time
if time <= 24 and time >= 0:
    newTime = (time + future_time) % 24
    print(f'la hora marcará {newTime} horas')
else:
    print('ingrese una hora valida')