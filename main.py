# Proyecto Final Python  -Emmanuel Obregon Herrera
# Junio 2023
# main.py

from clientes import Cliente
from menu import Producto
from pedido import Pedido

def mostrar_menu():
    """
    Muestra el menú de opciones.
    """
    print("------- MENÚ -------")
    print("a. Pedidos")
    print("b. Clientes")
    print("c. Menú")
    print("d. Salir")
    print("---------------------")

def realizar_operaciones_pedidos():
    """
    Realiza las operaciones relacionadas con los pedidos.
    """
    while True:
        print("------- PEDIDOS -------")
        print("1. Crear pedido")
        print("2. Cancelar pedido")
        print("3. Volver al menú principal")
        print("------------------------")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Solicitar los datos del pedido al usuario
            pedido = input("Pedido: ")
            cliente = input("Cliente: ")
            producto = input("Producto: ")
            precio = float(input("Precio: "))

            # Crear una instancia de la clase Pedido
            nuevo_pedido = Pedido(pedido, cliente, producto, precio)
            nuevo_pedido.crear_pedido()

            print("¡Pedido creado!")
            print("-------------------")

            # Simulación de impresión de ticket
            with open('ticket.txt', 'a') as file:
                file.write(f'Pedido: {pedido}\n')
                file.write(f'Cliente: {cliente}\n')
                file.write(f'Producto: {producto}\n')
                file.write(f'Precio: {precio}\n')
                file.write('-------------------\n')

        elif opcion == "2":
            pedido = input("Ingrese el número de pedido a cancelar: ")

            # Crear una instancia de la clase Pedido
            pedido_cancelado = Pedido(pedido, "", "", 0)
            pedido_cancelado.cancelar_pedido()

            print("¡Pedido cancelado!")
            print("-------------------")

        elif opcion == "3":
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def realizar_operaciones_clientes():
    """
    Realiza las operaciones relacionadas con los clientes.
    """
    while True:
        print("------- CLIENTES -------")
        print("1. Agregar cliente")
        print("2. Eliminar cliente")
        print("3. Actualizar cliente")
        print("4. Volver al menú principal")
        print("------------------------")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Solicitar los datos del cliente al usuario
            clave = input("Clave: ")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            correo_electronico = input("Correo Electrónico: ")
            telefono = input("Teléfono: ")

            # Crear una instancia de la clase Cliente
            nuevo_cliente = Cliente(clave, nombre, direccion, correo_electronico, telefono)
            nuevo_cliente.agregar_cliente()

            print("¡Cliente agregado!")
            print("-------------------")

        elif opcion == "2":
            clave = input("Ingrese la clave del cliente a eliminar: ")

            # Crear una instancia de la clase Cliente
            cliente_eliminado = Cliente(clave, "", "", "", "")
            cliente_eliminado.eliminar_cliente()

            print("¡Cliente eliminado!")
            print("-------------------")

        elif opcion == "3":
            # Solicitar los datos actualizados del cliente al usuario
            clave = input("Clave del cliente a actualizar: ")
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            correo_electronico = input("Nuevo correo electrónico: ")
            telefono = input("Nuevo teléfono: ")

            # Crear una instancia de la clase Cliente
            cliente_actualizado = Cliente(clave, nombre, direccion, correo_electronico, telefono)
            cliente_actualizado.actualizar_cliente()

            print("¡Cliente actualizado!")
            print("-------------------")

        elif opcion == "4":
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def realizar_operaciones_menu():
    while True:
        print("------- MENÚ -------")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Volver al menú principal")
        print("---------------------")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Solicitar los datos del producto al usuario
            clave = input("Clave: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))

            # Crear una instancia de la clase Producto
            nuevo_producto = Producto(clave, nombre, precio)
            nuevo_producto.agregar_producto()

            print("¡Producto agregado!")
            print("-------------------")

        elif opcion == "2":
            clave = input("Ingrese la clave del producto a eliminar: ")

            # Crear una instancia de la clase Producto
            producto_eliminado = Producto(clave, "", 0.0)
            producto_eliminado.eliminar_producto()

            print("¡Producto eliminado!")
            print("-------------------")

        elif opcion == "3":
            # Solicitar los datos actualizados del producto al usuario
            clave = input("Clave del producto a actualizar: ")
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))

            # Crear una instancia de la clase Producto
            producto_actualizado = Producto(clave, nombre, precio)
            producto_actualizado.actualizar_producto()

            print("¡Producto actualizado!")
            print("-------------------")

        elif opcion == "4":
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def main():
    """
    Función principal del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "a":
            realizar_operaciones_pedidos()

        elif opcion == "b":
            realizar_operaciones_clientes()

        elif opcion == "c":
            realizar_operaciones_menu()

        elif opcion == "d":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
