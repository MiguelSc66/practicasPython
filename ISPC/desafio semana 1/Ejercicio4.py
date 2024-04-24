def calcular_tiempo_total(tramos): #Funcion para calcular el tiempo en horas y minutos
    min = sum(tramos) #Sumamos los tiempos de los tramos
    horas = min // 60 #caclulamos las horas 
    minutos = min % 60 #calculamos los minutos
    return horas, minutos

tramos = [] # acumulador

while True: # repetira el bucle hasta que llegue al break
    tiempo = int(input("Ingrese el tiempo del tramo: "))
    if tiempo == 0: # si es 0 frena todo el bucle
        break
    tramos.append(tiempo) #Agrega el tiempo al acumulador

# Llamamos a la funcion para calcular el tiempo total
horas, minutos = calcular_tiempo_total(tramos)

print(f"El tiempo total es de {horas}:{minutos}")
