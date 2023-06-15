# Proyecto Final Python  -Emmanuel Obregon Herrera
# Junio 2023
# menu.py

import sqlite3
"""
SQLite es un módulo de la biblioteca estándar de Python que proporciona una interfaz para trabajar con la base de datos SQLite.
SQLite es una base de datos incorporada y no requiere una instalación de servidor separada.
"""

class Producto:
    def __init__(self, clave, nombre, precio):
        """
        Inicializa una instancia de la clase Producto.

        Parameters:
            clave (str): Clave del producto.
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
        """
        self.clave = clave
        self.nombre = nombre
        self.precio = precio

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        # Crear la tabla menu si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu (
                clave TEXT PRIMARY KEY,
                nombre TEXT,
                precio REAL
            )
        ''')
        self.conn.commit()

    def agregar_producto(self):
        """
        Agrega un producto a la tabla menu.
        """
        # Implementación de la funcionalidad para agregar un producto
        self.cursor.execute('''
            INSERT INTO menu (clave, nombre, precio)
            VALUES (?, ?, ?)
        ''', (self.clave, self.nombre, self.precio))
        self.conn.commit()

    def eliminar_producto(self):
        """
        Elimina un producto de la tabla menu.
        """
        # Implementación de la funcionalidad para eliminar un producto
        self.cursor.execute('''
            DELETE FROM menu WHERE clave=?
        ''', (self.clave,))
        self.conn.commit()

    def actualizar_producto(self):
        """
        Actualiza los datos de un producto en la tabla menu.
        """
        # Implementación de la funcionalidad para actualizar un producto
        self.cursor.execute('''
            UPDATE menu SET nombre=?, precio=?
            WHERE clave=?
        ''', (self.nombre, self.precio, self.clave))
        self.conn.commit()

    def __del__(self):
        """
        Cierra la conexión y el cursor al destruir la instancia de la clase Producto.
        """
        self.cursor.close()
        self.conn.close()
