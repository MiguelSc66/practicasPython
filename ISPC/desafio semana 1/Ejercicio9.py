
def anagramas(palabra1, palabra2):

    palabra1 = palabra1.lower().replace(' ', '')
    palabra2 = palabra2.lower().replace(' ', '')

    p1_ordenada = ''.join(sorted(palabra1))
    p2_ordenada = ''.join(sorted(palabra2))

    if p1_ordenada == p2_ordenada:
        print('Las palabras son anagramas')
    else:
        print('Las palabras no son anagramas')

palabra1 = input('palabra 1: ')
palabra2 = input('palabra 2: ')
anagramas(palabra1, palabra2)