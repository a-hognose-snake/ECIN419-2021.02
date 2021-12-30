import sqlite3

class Connection:
    def __init__(self):
        try:
            self.con = sqlite3.connect('src/sql/ProyectoProgramacionAvanzada.db')
            self.cur = self.con.cursor()
        except Exception as e:
            print('No se ha podido conectar con la base de datos')

    def insert_player(self, nickname: str) -> bool:
        """Inserta un jugador en la base de datos.

        Parameters
        ----------
        nickname: str
            Jugador a registrar.
        
        Returns
        -------
        True
            Si el nickname fue insertado.
        False
            Si el nickname ya existe en la base de datos.
        """


        try:
            self.cur.execute('INSERT INTO player (nickname) VALUES (?)', (nickname,))
            self.con.commit()
        except Exception:
            self.con.rollback()
            return False
    
    def get_score_player(self, nickname: str, id_level: int) -> int:
        """Obtiene un puntaje de un jugador en base al nickname y el nivel jugado.

        Parameters
        ----------
        nickname: str
            Jugador del cual se quiere saber el puntaje.
        id_level: int
            Nivel del cual se quiere saber el puntaje.
        
        Returns
        -------
        score: int
            El puntaje correspondiente al jugador en un nivel.
        -1
            Si no existe alguno de los datos en la base de datos.
        """
        try:
            self.cur.execute('SELECT score_level FROM score WHERE nickname = ? and id_level = ?', (nickname, id_level))
            rows = self.cur.fetchone()
            if rows:
                score = rows[0]
                return score
            return -1
        except Exception as e:
            print(e)

    def modify_score(self, nickname: str, id_level: int, score_level: int) -> bool:
        """Modifica un puntaje en la base de datos dependiendo de la situacion.
        
        Si el nivel ya ha sido jugado antes por el jugador modifica el puntaje en caso de que sea mayor al actual.
         
        Si el nivel no ha sido jugado, inserta el puntaje obtenido.

        Parameters
        ----------
        nickname: str
            Jugador al cual le pertenece el puntaje.
        id_level: int
            Id del nivel jugado.
        score_level: int
            Puntaje que se evaluara si es mayor o menor al puntaje actual.        
        
        Returns
        -------
        True
            Si el puntaje fue insertado/modificado.
        False
            Si el puntaje no se registró.
        
        """

        try:
            old_score = self.get_score_player(nickname, id_level)
            if old_score != -1:
                if score_level > old_score:
                    return self.update_score(nickname, id_level, score_level)
            else:
                return self.insert_score(nickname, id_level, score_level)

        except Exception:
            return False

    def update_score(self, nickname, id_level, score_level) -> bool:
        """Actualiza el puntaje de un jugador en un nivel.

        Parameters
        ----------
        nickname: str
            Jugador al cual le pertenece el puntaje.
        id_level: int
            Id del nivel jugado.
        score_level: int
            Puntaje obtenido.
        
        Returns
        -------
        True
            Si el puntaje fue modificado.
        False
            Si el puntaje no fue modificado.
        """
        try:
            self.cur.execute('UPDATE score SET score_level = ? WHERE nickname = ? and id_level = ?', (score_level, nickname, id_level))
            self.con.commit()
            return True
        except Exception as e:
            return False

    def insert_score(self, nickname, id_level, score_level) -> bool:
        """Inserta un puntaje de un jugador en un nivel.

        Parameters
        ----------
        nickname: str
            Jugador al cual le pertenece el puntaje.
        id_level: int
            Id del nivel jugado.
        score_level: int
            Puntaje obtenido.
        
        Returns
        -------
        True
            Si el puntaje fue insertado.
        False
            Si el puntaje no fue insertado.
        """
        try:
            self.cur.execute('INSERT INTO score (nickname, id_level, score_level) VALUES (?, ?, ?)', (nickname, id_level, score_level))
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            return False