# def bisiesto(year): 
#     if year < 1582:
#         return year % 4 == 0
#     else:
#         if year % 4 != 0:
#             return False
#         elif year % 100 != 0:
#             return True
#         elif year % 400 != 0:
#             return False
#         else: 
#             return True

def bisiesto2(year): 
    if year < 1582:
        return year % 4 == 0
    else:
        print(year % 4 == 0 and year % 100 != 0)
        print(year % 400 == 0)
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) # si alguno de estos dos se cumple, el año es bisiesto y en caso de que ninguno lo cumpla no es bisiesto


year = int(input('ingrse el año: '))

# if bisiesto(year):
#     print(f'{year} es bisiesto')
# else:
#     print(f'{year} no es bisiesto')

if bisiesto2(year): 
    print(f'{year} es bisiesto')
else:
    print(f'{year} no es bisiesto')