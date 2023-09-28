'''Un comercio de electrodomésticos necesita para su línea de cajas un programa que le
indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números
enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes
de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la
cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir
un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona con $500,
el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1'''

monto_compra = int(input("Ingrese el monto total de la compra: "))
monto_recibido = int(input("Ingrese el monto recibido por el cliente: "))

vuelto = monto_recibido - monto_compra

cantidad_500 = vuelto // 500
vuelto = vuelto % 500

cantidad_100 = vuelto // 100
vuelto = vuelto % 100

cantidad_50 = vuelto // 50
vuelto = vuelto % 50

cantidad_20 = vuelto // 20
vuelto = vuelto % 20

cantidad_10 = vuelto // 10
vuelto = vuelto % 10

cantidad_5 = vuelto // 5
vuelto = vuelto % 5

cantidad_1 = vuelto // 1
vuelto = vuelto % 1

print("El vuelto a entregar es de un total de: ", vuelto)
print("La cantidad de billetes de 500 que debe entregar al cliente es: ", cantidad_500)
print("La cantidad de billetes de 100 que debe entregar al cliente es: ", cantidad_100)
print("La cantidad de billetes de 50 que debe entregar al cliente es: ", cantidad_50)
print("La cantidad de billetes de 20 que debe entregar al cliente es: ", cantidad_20)
print("La cantidad de billetes de 10 que debe entregar al cliente es: ", cantidad_10)
print("La cantidad de billetes de 5 que debe entregar al cliente es: ", cantidad_5)
print("La cantidad de billetes de 1 que debe entregar al cliente es: ", cantidad_1)


