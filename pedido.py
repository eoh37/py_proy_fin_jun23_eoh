# Proyecto Final Python  -Emmanuel Obregon Herrera
# Junio 2023
# pedido.py

import sqlite3
"""
SQLite es un módulo de la biblioteca estándar de Python que proporciona una interfaz para trabajar con la base de datos SQLite.
SQLite es una base de datos incorporada y no requiere una instalación de servidor separada.
"""

# Conectarse a la base de datos
conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()

# Crear la tabla pedido si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedido (
        pedido INTEGER,
        cliente TEXT,
        producto TEXT,
        precio REAL
    )
''')

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()


class Pedido:
    """
    Clase que representa un pedido y permite interactuar con la tabla "pedido" de la base de datos.
    """
    def __init__(self, pedido, cliente, producto, precio):
        self.pedido = pedido
        self.cliente = cliente
        self.producto = producto
        self.precio = precio

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def crear_pedido(self):
        """
        Crea un nuevo pedido y lo inserta en la tabla pedido.
        """
        # Implementación de la funcionalidad para crear un pedido
        self.cursor.execute('''
            INSERT INTO pedido (pedido, cliente, producto, precio)
            VALUES (?, ?, ?, ?)
        ''', (self.pedido, self.cliente, self.producto, self.precio))
        self.conn.commit()

        # Simulación de impresión de ticket
        with open('ticket.txt', 'a') as file:
            file.write(f'Pedido: {self.pedido}\n')
            file.write(f'Cliente: {self.cliente}\n')
            file.write(f'Producto: {self.producto}\n')
            file.write(f'Precio: {self.precio}\n')
            file.write('-------------------\n')

    def cancelar_pedido(self):
        """
        Cancela un pedido existente eliminándolo de la tabla pedido.
        """
        # Implementación de la funcionalidad para cancelar un pedido
        self.cursor.execute('''
            DELETE FROM pedido WHERE pedido=?
        ''', (self.pedido,))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

