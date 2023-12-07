import random

def listar_productos(arch):
    with open(arch, "rt") as file:
        print(file.read())

# Carga de productos
def cargar_productos(arch):
    while True:
        try:
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio: "))
            id_producto = random.randint(1, 100)
            producto = f"ID: {id_producto}, Nombre: {nombre_producto}, Precio: {precio_producto}\n"
            
            with open(arch, "at") as file:
                file.write(producto)

        except ValueError:
            print("Datos invalidos")
        
        finally:
            nuevo_producto = input("¿Quiere ingresar otro producto? (S/N): ")
            if nuevo_producto.upper() != "S":
                print("Estos son los productos que usted cargó: ")
                listar_productos(arch)
                break

def buscar_por_id(arch, id_a_buscar):
    with open(arch, "rt") as file:
        for line in file:
            if f"ID: {id_a_buscar}" in line:
                return line

    print(f"No se halló el producto con el ID {id_a_buscar}")
    return None

def actualizar_productos(arch):
    while True:
        try:
            id_producto_elegido = int(input("Elegir el ID del producto que desea actualizar: "))
            producto = buscar_por_id(arch, id_producto_elegido)
            
            if producto is not None:
                nuevo_precio = float(input("Ingrese un nuevo precio para el producto: "))
                producto_actualizado = producto.replace(f"Precio: {producto.split(', Precio: ')[-1]}", f"Precio: {nuevo_precio}")
                
                with open(arch, "rt") as file:
                    productos = file.readlines()

                with open(arch, "wt") as file:
                    for p in productos:
                        if f"ID: {id_producto_elegido}" in p:
                            file.write(producto_actualizado)
                        else:
                            file.write(p)
                
                print("Producto actualizado:", producto_actualizado)
            else:
                print(f"No se encontró ningún producto con el ID {id_producto_elegido}.")
                    
        except ValueError:
            print("Datos inválidos")
        
        finally:
            nueva_actualizacion = input("¿Desea actualizar otro producto? (S/N): ")
            if nueva_actualizacion.upper() != "S":
                print("Estos son los productos actualizados:")
                listar_productos(arch)
                break

def eliminar_producto(arch):
    while True:
        try:
            id_producto_elegido = int(input("Elegir el ID del producto que desea borrar: "))
            producto = buscar_por_id(arch, id_producto_elegido)
            
            if producto is not None:
                confirmacion_borrar = input(f"¿Está seguro que desea eliminar el producto con ID {id_producto_elegido}? (S/N): ")
                
                if confirmacion_borrar.upper() == "S":
                    with open(arch, "rt") as file:
                        productos = file.readlines()

                    with open(arch, "wt") as file:
                        for p in productos:
                            if f"ID: {id_producto_elegido}" not in p:
                                file.write(p)
                    
                    print("El producto ha sido eliminado.")
                else:
                    print("Operación cancelada.")
            else:
                print(f"No se encontró ningún producto con el ID {id_producto_elegido}.")
                    
        except ValueError:
            print("Por favor, ingrese un ID válido.")
        
        finally:
            borrar_otro = input("¿Desea borrar otro producto? (S/N): ")
            if borrar_otro.upper() != "S":
                print("Estos son los productos después de borrar:")
                listar_productos(arch)
                break  # Salir del bucle de eliminar_producto

def main():
    archivo_productos = "productos.txt"
    
    while True:
        opcion = int(input("Elija entre las siguientes opciones:\n 1. Cargar productos\n 2. Actualizar productos\n 3. Eliminar productos\n 4. Listar productos\n 5. Salir\n"))
        
        if opcion == 1:
            cargar_productos(archivo_productos)
        elif opcion == 2:
            actualizar_productos(archivo_productos)
        elif opcion == 3:
            eliminar_producto(archivo_productos)
        elif opcion == 4:
            print("Estos son los productos:")
            listar_productos(archivo_productos)
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
            
main()
