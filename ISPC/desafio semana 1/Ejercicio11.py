marcador=[0,0]

while marcador[0] != 3 and marcador[1]!= 3: # pregunta hasta que uno gana
    J1 = str(input('j1: '))
    J2 = str(input('j2: '))
    
    if J1==J2:#esto es empate   
        print('Empate ',marcador,' Prosiga')
    else:  
        if J1 == 'piedra' and J2 == 'papel':
            marcador[1]+=1
            print(marcador)
        if J1 == 'piedra' and J2 =='tijera':
            marcador[0]+=1
            print(marcador)
        if J2 == 'piedra' and J1 == 'papel':
            marcador[0]+=1
            print(marcador)
        if J2 == 'piedra' and J1 =='tijera':
            marcador[1]+=1
            print(marcador)
        if J1 =='tijera' and J2 == 'papel':
            marcador[0]+=1
            print(marcador)
        if J2 =='tijera' and J1 == 'papel':
            marcador[1]+=1
            print(marcador)