import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Función para crear una raqueta de jugador devolviendo un objeto
def crear_Raqueta_Jugador(x, y):
    return pygame.Rect(x, y, 10, 100)

# Función para crear una paleta de la máquina la cual devuelve un objeto
def crear_maquina_raqueta(x, y):
    return pygame.Rect(x, y, 10, 100)

# Función para crear la bola, retorna un objeto
def crear_bola():
    return pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10)

# Función para mostrar el menú inicial de usario para seleccionar el número de enemigos
def mostrar_menu(screen):
    font = pygame.font.Font(None, 36)
    text1 = font.render("1. Jugar contra una raqueta enemiga", True, WHITE)
    text2 = font.render("2. Jugar contra dos raquetas enemigas", True, WHITE)
    screen.blit(text1, (200, 200))
    screen.blit(text2, (200, 300))
    pygame.display.flip()

# Función principal del juego
def main():
    # Inicializar pantalla y establecer el título del juego
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Pong")

    # Mostrar menú inicial
    mostrar_menu(screen)

    # Variables de control del juego
    Inicio_Juego = False            # Controla el inicio del juego, verifica que la opciones
                                    # Del menú seleccionadas sean correctas
    Dos_raquetas = False            # Indica el número de raquetas enemigas False-> 1 raqueta
                                    # True-> 2 raquetas

    clock = pygame.time.Clock()

    # Velocidad de la bola, se seleccionan de manera aleatoria siguendo una función normal
    Velocidad_Bolax = 5 * random.choice([-1, 1])
    Velocidad_Bolay = 5 * random.choice([-1, 1])

    # Loop principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Eventos del teclado estamos en el menú principal del juego
            if event.type == pygame.KEYDOWN and not Inicio_Juego:
                if event.key == pygame.K_1: # Si es 1
                    Inicio_Juego = True
                elif event.key == pygame.K_2:  # Si es 2
                    Inicio_Juego = True
                    Dos_raquetas = True

        # Si el juego ha comenzado
        if Inicio_Juego:
            # Crear las raquetas y bola
            raqueta_jugador = crear_Raqueta_Jugador(50, SCREEN_HEIGHT // 2 - 50)
            bola = crear_bola()   # Crer el objeto bola

            # Si se seleccionaron dos raquetas enemigas
            if Dos_raquetas: # True
                maquina_raqueta1 = crear_maquina_raqueta(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 4 - 50)
                maquina_raqueta2 = crear_maquina_raqueta(SCREEN_WIDTH - 60, (3 * SCREEN_HEIGHT) // 4 - 50)
            else:  # False
                # Si se seleccionó una raqueta enemiga
                maquina_raqueta1 = crear_maquina_raqueta(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2 - 50)

            # Loop de juego
            while Inicio_Juego:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Inicio_Juego = False
                        running = False

                # Control de la paleta del jugador
                keys = pygame.key.get_pressed()
                jugador_velocidad = 0
                if keys[pygame.K_UP]:
                    jugador_velocidad= -5
                elif keys[pygame.K_DOWN]:
                    jugador_velocidad = 5
                raqueta_jugador.y +=  jugador_velocidad
                raqueta_jugador.y = max(0, min(raqueta_jugador.y, SCREEN_HEIGHT - raqueta_jugador.height))

                # Control de la paleta de la máquina (IA simple)
                velocidad_raqueta_maquina = 0
                if bola.y < maquina_raqueta1.y:
                    velocidad_raqueta_maquina = -5
                elif bola.y > maquina_raqueta1.y:
                    velocidad_raqueta_maquina = 5
                maquina_raqueta1.y += velocidad_raqueta_maquina
                maquina_raqueta1.y = max(0, min(maquina_raqueta1.y, SCREEN_HEIGHT - maquina_raqueta1.height))

                # Actualizar posición de la pelota
                bola.x += Velocidad_Bolax
                bola.y += Velocidad_Bolay

                # Verificar colisiones con las paletas
                if (raqueta_jugador.colliderect(bola) or
                    maquina_raqueta1.colliderect(bola) or
                    (Dos_raquetas and maquina_raqueta2.colliderect(bola))):
                    Velocidad_Bolax = -Velocidad_Bolax

                # Verificar colisiones con los bordes
                if bola.top <= 0 or bola.bottom >= SCREEN_HEIGHT:
                    Velocidad_Bolay = -Velocidad_Bolay

                # Dibujar elementos en la pantalla
                screen.fill(BLACK)
                pygame.draw.line(screen, WHITE, [SCREEN_WIDTH // 2, 0], [SCREEN_WIDTH // 2, SCREEN_HEIGHT], 5)
                pygame.draw.rect(screen, WHITE, raqueta_jugador)
                pygame.draw.rect(screen, WHITE, maquina_raqueta1)
                if Dos_raquetas:
                    pygame.draw.rect(screen, WHITE, maquina_raqueta2)
                pygame.draw.ellipse(screen, WHITE, bola)

                # Refrescar pantalla
                pygame.display.flip()
                clock.tick(60)

    pygame.quit()

# Llamar a la función principal del juego
if __name__ == "__main__":
    main()
