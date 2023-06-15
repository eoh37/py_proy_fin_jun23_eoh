# Proyecto Final Python  -Emmanuel Obregon Herrera
# Junio 2023
# clientes.py

import sqlite3
"""
SQLite es un módulo de la biblioteca estándar de Python que proporciona una interfaz para trabajar con la base de datos SQLite.
SQLite es una base de datos incorporada y no requiere una instalación de servidor separada.
"""

class Cliente:
    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        self.clave = clave
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono

        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                clave TEXT PRIMARY KEY,
                nombre TEXT,
                direccion TEXT,
                correo_electronico TEXT,
                telefono TEXT
            )
        ''')
        self.conn.commit()

        # Crear la tabla clientes si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                clave TEXT PRIMARY KEY,
                nombre TEXT,
                direccion TEXT,
                correo_electronico TEXT,
                telefono TEXT
            )
        ''')
        self.conn.commit()

    def agregar_cliente(self):
        """
        Agrega un cliente a la tabla clientes.
        """
        # Implementación de la funcionalidad para agregar un cliente
        self.cursor.execute('''
            INSERT INTO clientes (clave, nombre, direccion, correo_electronico, telefono)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.clave, self.nombre, self.direccion, self.correo_electronico, self.telefono))
        self.conn.commit()

    def eliminar_cliente(self):
        """
        Elimina un cliente de la tabla clientes.
        """
        # Implementación de la funcionalidad para eliminar un cliente
        self.cursor.execute('''
            DELETE FROM clientes WHERE clave=?
        ''', (self.clave,))
        self.conn.commit()

    def actualizar_cliente(self):
        """
        Actualiza los datos de un cliente en la tabla clientes.
        """
        # Implementación de la funcionalidad para actualizar un cliente
        self.cursor.execute('''
            UPDATE clientes SET nombre=?, direccion=?, correo_electronico=?, telefono=?
            WHERE clave=?
        ''', (self.nombre, self.direccion, self.correo_electronico, self.telefono, self.clave))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
