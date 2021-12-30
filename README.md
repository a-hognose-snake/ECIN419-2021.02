# Proyecto de Programación Avanzada 2021.02

## Proyecto

Construcción de un videojuego con un mínimo de 5 niveles. Debe incluir input, manipulación de tiempo y colisiones.

## Conocimiento necesarios:

1. [Pygame](https://www.pygame.org/news "Pygame")
2. [Manipulación del tiempo en el juego](https://www.pygame.org/docs/ref/time.html "Manipulación del tiempo en el juego")
3. [Sprites](https://www.pygame.org/docs/ref/sprite.html "Sprites")
4. Input del usuario
5. [Detección de colisiones](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollideany)

## Diseño
### Organización
------------
    ├── img
    │   ├── Diagrama_de_clases.png
    │   └── MR.png
    ├── resources
    │   ├── fonts
    │   ├── images
    │   └── sounds
    ├── src
    │   ├── bullet
    │   │   ├── __init__.py
	│   │   └── Bullet.py
    │   ├── character
    │   │   ├── __init__.py
	│   │   └── Character.py
    │   ├── constant
    │   │   ├── __init__.py
	│   │   └── constant.py
    │   ├── enemy
    │   │   ├── __init__.py
	│   │   └── Enemy.py
    │   ├── level
    │   │   ├── __init__.py
    │   │   ├── Boss.py
	│   │   └── Level.py
    │   ├── platform
    │   │   ├── __init__.py
	│   │   └── Platform.py
    │   ├── sql
    │   │   ├── __init__.py
    │   │   ├── Connection.py
	│   │   └── ProyectoProgramacionAvanzada.db -> Base de datos Sqlite3
    │   └── main.py
--------
### Diagrama de clases
![Diagrama de clases](img/Diagrama.png)

### Modelo Relacional
![Modelo relacional](img/MR.png)
