print('Productos: A $270, B $340, C $390')

producto_elegido = input('Elija un Producto: ')

def change(product):
    money = []
    A, B, C = 270, 340, 390
    
    if product == 'A':
        val = A
    elif product == 'B':
        val = B
    elif product == 'C':
        val = C
    
    while sum(money) != val:
        client_money = int(input("Ingrese las monedas: "))
        money.append(client_money)
        
        total = sum(money)
        
        if total == val:
            print('Gracias por su compra')
            break
        elif total > val:
            changeclient = total - val
            print('Su vuelto:')
            while changeclient > 0:
                if changeclient >= 100:
                    print(100)
                    changeclient -= 100
                elif changeclient >= 50:
                    print(50)
                    changeclient -= 50
                elif changeclient >= 10:
                    print(10)
                    changeclient -= 10
            print('Gracias por su compra')
            break

change(producto_elegido)