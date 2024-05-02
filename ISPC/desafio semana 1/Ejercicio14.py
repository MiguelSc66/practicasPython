signos = {
'aries': (( 3, 21), ( 4, 20)),
'tauro': (( 4, 21), ( 5, 21)),
'geminis': (( 5, 22), ( 6, 21)),
'cancer': (( 6, 22), ( 7, 23)),
'leo': (( 7, 24), ( 8, 23)),
'virgo': (( 8, 24), ( 9, 23)),
'libra': (( 9, 24), (10, 23)),
'escorpio': ((10, 24), (11, 22)),
'sagitario': ((11, 23), (12, 21)),
'capricornio': ((12, 22), ( 1, 20)),
'acuario': (( 1, 21), ( 2, 19)),
'piscis': (( 2, 20), ( 3, 20)),
}
def  es_signo(dia=int(input("dia: ")), mes=int(input("mes: "))) :
    for i in signos:
        if (signos[i][0][0]== mes and signos[i][0][1] <= dia) or (signos[i][1][0] == mes and signos[i][1][1] >=dia):
            print("tu signo es: ",i)
            break

es_signo()