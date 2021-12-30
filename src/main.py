#style guide utilizado -> https://numpydoc.readthedocs.io/en/latest/format.html

import pygame
from character.Character import Character
from level.Level import Level
from constant.constant import *
from sql.Connection import Connection

def get_score_level(level: int, con: Connection, pos_level: tuple):
    """Muestra los puntajes correspondientes a un nivel.

    Paramters
    ---------
    level: int
        Nivel desde donde se obtendran los datos.
    con: Connection
        Clase que contiene metodos para interactuar con sqlite.
    pos_level: tuple
        Posicion en donde se va a mostrar el puntaje.
    """
    text = ''
    rows = con.get_score_level(level)
    text = 'Level: ' +  str(level)

    score_text = FONT_SMALL.render(text , True, (255, 255, 255))
        
    SCREEN.blit(score_text, pos_level)
    coord_x = pos_level[0]
    coord_y = pos_level[1] + 30
    if rows:
        for i in rows:
            text_2 = 'Nickname: ' + str(i[1].strip()) +  ' Score: ' + str(i[2])
            score_text_2 = FONT_SMALL.render(text_2, True, (255, 255, 255))
            SCREEN.blit(score_text_2, (coord_x, coord_y))
            coord_y += 30

def show_puntaje(con: Connection):
    """Crea una pantalla con los 5 mayores puntajes de los niveles.

    Parameters
    ----------
    con: Connection
        Clase que contiene metodos para interactuar con sqlite.
    """
    finished = False
    clock = pygame.time.Clock()
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_r]:
                    finished = True

        SCREEN.fill((0, 0, 0))
        get_score_level(1, con, (50, 50))
        get_score_level(2, con, (550, 50))
        get_score_level(3, con, (50, 250))
        get_score_level(4, con, (550, 250))
        get_score_level(5, con, (50, 450))
        return_text = FONT_SMALL.render(
                "Press 'R' to return", True, (255, 255, 255))
        SCREEN.blit(return_text, (600, 680))
        pygame.display.update()
        clock.tick(FPS)

def text_box(background) -> str:
    """Permite el ingreso de un nombre de usuario
    
    Parameters
    ----------
    background: Surface
        Fondo del juego.
    
    Returns
    -------
    nickname: str  
        nombre de usuario.
    """
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)
    nickname = ''
    input_rect = pygame.Rect(270 + 200, 680, 140, 32)
    active = False
    exit_game = False
    color = (0,0,0)
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    else:
                        nickname += event.unicode
                if event.key == pygame.K_RETURN:
                    exit_game = True
        if active:
            color = (0, 255, 255)
        SCREEN.blit(background, (0,0))                
        pygame.draw.rect(SCREEN, color, input_rect, 2)
        text_surface = base_font.render(nickname, True, (255, 255, 255))  
        SCREEN.blit(text_surface, input_rect)

        init_text = FONT_SMALL.render(
                "Ingresa tu nickname: ", True, (255, 255, 255))
        SCREEN.blit(init_text, (270, 680))
        pygame.display.update()
        clock.tick(FPS)

    if nickname == '':
        return None
    else:
        return nickname
    
def start_text(background):
    """Imprime el texto de inicio.

    Parameters
    ----------
    background: Surface
        Fondo del juego.
    
    """
    SCREEN.blit(background, (0,0))
    score_text = FONT_SMALL.render(
            "Press 'P' to SCORE", True, (255, 255, 255))
    SCREEN.blit(score_text, (WIDTH/2-100, 20))
    init_text = FONT_SMALL.render(
            "Press 'I' to START", True, (255, 255, 255))
    SCREEN.blit(init_text, (600, 680))
    exit_text = FONT_SMALL.render(
            "Press 'E' to EXIT", True, (255, 255, 255))
    SCREEN.blit(exit_text, (270, 680))

def run_level(con: Connection, nickname: str,):
    """Ejecuta los niveles del juego.
    
    Parameters
    ----------
    con: Connection
        Clase que contiene metodos para interactuar con sqlite.
    nickname: str
        Nickname del jugador.
    """
    n_level = 0
    character = Character((0,200))
    while True:
        level = Level(character, n_level)
        if not level.runnin_level():
            break
        character = level.character
        character.health = 100
        score_level = character.calculate_score()
        character.bullets_shoot = 0 #contador de balas lanzadas
        character.bullets_hit = 0 #contador de balas acertadas
        con.modify_score(nickname, n_level + 1, score_level)
        if n_level == 4: 
            break
        if level.isGameWin():
            n_level = level.level + 1
        if level.isGameOver():
            break   
def main():
    """Función principal.
    """
    con = Connection()

    pygame.mixer.music.load('resources/sounds/init.mp3')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play()
    background = pygame.image.load("resources/images/level/init.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    SCREEN.fill((255, 255, 255))
    exit_game = False
    nickname = text_box(background)
    if nickname is not None:
        con.insert_player(nickname)
    else:
        exit_game = True
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_e]:
                    exit_game = True
                if keys[pygame.K_p]:
                    show_puntaje(con)
                if keys[pygame.K_i]:
                    pygame.mixer.music.stop()
                    run_level(con, nickname)
                            

        start_text(background)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


main()
exit()