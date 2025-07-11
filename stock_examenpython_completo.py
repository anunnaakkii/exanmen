productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["Lenovo", 14, "4GB" "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16Gb", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "IT", "Intel Core i3", "integrada"],
}

stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
}

def stock_marca(marca):
    """
    Calcula y muestra el stock total de una marca particular.
    La búsqueda no es sensible a mayúsculas/minúsculas.
    """
    total_stock = 0
    for modelo, detalles in productos.items():
        if detalles[0].lower() == marca.lower():
            if modelo in stock:
                total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")

def busqueda_precio(p_min, p_max):
    """
    Encuentra y muestra los modelos de notebooks que están dentro de un rango de precios
    dado y que tienen stock disponible. La lista de resultados se ordena alfabéticamente.
    """
    modelos_encontrados = []
    for modelo, info_stock in stock.items():
        precio = info_stock[0]
        cantidad_stock = info_stock[1]
        if p_min <= precio <= p_max and cantidad_stock > 0:
            marca = productos[modelo][0]
            modelos_encontrados.append(f"{marca}--{modelo}")

    modelos_encontrados.sort()

    if modelos_encontrados:
        print(f"Los notebooks entre los precios consultas son: {modelos_encontrados}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p_nuevo):
    """
    Actualiza el precio de un modelo específico en el diccionario 'stock'.
    Retorna True si el modelo existe y el precio se actualiza, False en caso contrario.
    """
    if modelo in stock:
        stock[modelo][0] = p_nuevo
        return True
    return False

def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def main():
    """
    Función principal
    """
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción que desea usar: ")

        if opcion == '1':
            marca_consultar = input("Ingrese marca a consultar: ")
            stock_marca(marca_consultar)
        elif opcion == '2':
            while True:
                try:
                    precio_min_str = input("Ingrese precio mínimo: ")
                    p_min = int(precio_min_str)
                    precio_max_str = input("Ingrese precio máximo: ")
                    p_max = int(precio_max_str)
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
        elif opcion == '3':
            while True:
                modelo_actualizar = input("Ingrese modelo a actualizar: ")
                while True:
                    try:
                        precio_nuevo_str = input("Ingrese precio nuevo: ")
                        p_nuevo = int(precio_nuevo_str)
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros para el precio!!")

                if actualizar_precio(modelo_actualizar, p_nuevo):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
                if respuesta != 's':
                    break
        elif opcion == '4':
            print("Final del programa.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    main()