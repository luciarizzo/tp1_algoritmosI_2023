'''
#####
EJERCICIO 3 TP 1
#####
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo)
se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes
y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.
Cantidad de viajes Valor del pasaje
1 a 20 - Averiguar valor actualizado
21 a 30 - 20% de descuento sobre tarifa máxima
31 a 40 - 30% de descuento sobre tarifa máxima
Más de 40 - 40% de descuento sobre tarifa máxima
'''

def calcular_total_viajes(a, b):
    total = a * b
    if a > 0 and a < 21:
        valor_descuento = total * (20 / 100)
        if a > 21 and a < 31:
            # "20% de descuento sobre tarifa maxima"
            valor_descuento = total * (20 / 100)
            if a > 31 and a < 41:
                valor_descuento = total * (20 / 100)
    else:
        valor_descuento = total * (40 / 100)
    
    return valor_descuento
    

viajes_realizados = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
                        
if viajes_realizados > 0:
    total_gastado = calcular_total_viajes(viajes_realizados, 1)
    print(total_gastado)
else:
    print("El numero de viajes ingresado no es valido")