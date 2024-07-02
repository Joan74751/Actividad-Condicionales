#Solicitud de datos

nombre = input("Ingresa tu nombre: ")
valor = float(input("Ingresa el valor de tu compra: $"))

#Si es menor a 80 = 0%, Si es mayor a 80 y menor que 150 = 15%

#Si es mayor o igual a 150 y menor o igual a 300 = 15%, Si es mayor a 300 y menor a 500 = 20%

if valor < 80:
    print(f'Su nombre es: {nombre}')
    print(f'Compra sin descuento ${valor}')
    print(f'Compra con descuento del 0% ${valor}')


elif valor >= 80 and valor < 150:
    print(f'Su nombre es: {nombre}')
    print(f'Compra sin descuento ${valor}')
    print(f'Compra con descuento del 10% ${valor-valor*0.1}')

elif valor >= 150 and valor <= 300:
    print(f'Su nombre es: {nombre}')
    print(f'Compra sin descuento ${valor}')
    print(f'Compra con descuento del 15% ${valor-valor*0.15}')

elif valor > 300 and valor <= 500:
    print(f'Su nombre es: {nombre}')
    print(f'Compra sin descuento ${valor}')
    print(f'Compra con descuento del 20% ${valor-valor*0.2}')

'''
Preguntas

1. Angel Mario Villa Lopez realizó una compra de 455 usd.

2. Rosa Diaz realizó una compra de 105 usd.

3. Dilan Gonzalez realizó una compra de 250 usd.

4. Kelly Daza realizó una compra de 430 usd.

Respuestas

1. Su nombre es: Angel Mario Villa Lopez
El valor de su compra es $455.0
Su descuento es de 20% dando un total de: $364.0

2. Su nombre es: Rosa Diaz
El valor de su compra es $105.0
Su descuento es de 10% dando un total de: $94.5

3. Su nombre es: Dilan Gonzalez
El valor de su compra es $250.0
Su descuento es de 15% dando un total de: $212.5

4. Su nombre es: Kelly Daza
El valor de su compra es $430.0
Su descuento es de 20% dando un total de: $344.0
'''
