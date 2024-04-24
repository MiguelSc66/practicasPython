num = int(input('ingrese un numero: '))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print(num,'es primo')
else: 
    print(num,'no es primo')