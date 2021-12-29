import sqlite3

class Connection:
    def __init__(self):
        try:
            self.con = sqlite3.connect('src/sql/ProyectoProgramacionAvanzada.db')
            self.cur = self.con.cursor()
            print('conexion establecida')
        except Exception as e:
            print('No se ha podido conectar con la base de datos')