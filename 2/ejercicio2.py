'''
#####
EJERCICIO 2 TP 1
#####
Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año).
Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función'''

def verificar_fecha(a,b,c):
    if a > 1 and a < 31:
        valido = True
        if b > 1 and b < 12:
            valido = True     
            if c > 1900 and c < 3000:
                valido = True
            else:
                valido = False
        else:
            valido = False
    else:
        valido = False
        
    return valido


d = int(input("Ingresar dia "))
m = int(input("Ingresar mes"))
a = int(input("Ingresar año"))

if d > 0 and m > 0 and a > 0:
    resultado = verificar_fecha(d, m, a)
    if resultado == True:
        print("La fecha es valida")
    else:
        print("La fecha no es valida")
else:
    print("Uno de los numeros ingresado no es un numero entero positivo")