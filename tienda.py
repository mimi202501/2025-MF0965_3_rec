class Producto:
    def __init__(self, codigo, nombre, precio):

        """
        COMPLETAR 1:
        Asigna los parámetros a los atributos
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        """
        COMPLETAR 2:
        Devuelve un string con el formato especificado, usando f-string.
        Asegúrate de que el precio se muestre con 2 decimales.
        Ejemplo de formato: "[PROD001] Teclado Mecánico - Precio: 75.50 €
        """
        return f"[{self.codigo}] {self.nombre} - Precio: {self.precio:.2f} €"


def buscar_producto(inventario, codigo_buscar):
    """
    COMPLETAR 3:
    Busca en 'inventario' un producto cuyo código coincida con 'codigo_buscar'.
    Si lo encuentra, devuelve dicho objeto; si no, devuelve None.
    """
    for producto in inventario:
        if producto.codigo == codigo_buscar:
            return producto
    return None


def mostrar_inventario(inventario):
    """
    COMPLETAR 4:
    Imprime por pantalla todos los productos que hay en 'inventario'.
    """
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(producto)


def calcular_valor_total(inventario):
    """
    COMPLETAR 5:
    Calcula y devuelve la suma de los precios de todos los productos en el inventario.
    """
    for producto in inventario:
        total += producto.precio
    return total


def main():
    inventario = [
        Producto("PROD001", "Teclado Mecánico", 75.50),
        Producto("PROD002", "Mouse Inalámbrico", 25.00)
    ]

    while True:
        print("\n===============================")
        print("  MENÚ DE GESTIÓN DE INVENTARIO")
        print("===============================")
        print("1. Mostrar inventario")
        print("2. Buscar producto")
        print("3. Calcular valor total del inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            mostrar_inventario(inventario)
        elif opcion == '2':
            codigo_buscar = input("Ingrese el código del producto a buscar: ")
            producto_encontrado = buscar_producto(inventario, codigo_buscar)
            """
            COMPLETAR 6:
            Comprueba si 'producto_encontrado' es distinto de None.
            Si se encontró, imprime ">> Producto encontrado:" y luego el producto.
                     Si no, imprime ">> No se encontró ningún producto con ese código."
            """

        elif opcion == '3':
            valor_total = calcular_valor_total(inventario)
            print(f"\n>> El valor total del inventario es: {valor_total:.2f} €")
        elif opcion == '4':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija entre 1 y 4.")


if __name__ == "__main__":
    main()
