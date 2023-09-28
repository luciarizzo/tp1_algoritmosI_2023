'''
Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos,
donde la cantidad de filas se recibe como parámetro:
**********
**********
**********
**********
**********

**
****
******
********
**********
'''

def impresion_lineal(filas):
    for i in range(filas):
        print("**********")
        
def impresion_creciente(filas):
    caracter = "*"
    cadena_caracter = ""
    for i in range(1, filas + 1):
        print(caracter * i)
        
        
filas_lineal = int(input("Ingrese una cantidad de filas para imprimir el patron lineal: "))
impresion_lineal(filas_lineal)


filas_crecientes = int(input("Ingrese una cantidad de filas para imprimir el patron creciente: "))
impresion_creciente(filas_crecientes)
