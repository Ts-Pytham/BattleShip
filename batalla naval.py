import pygame, sys, random
import pygame as pg

#COLORES
BLANCO    = (255, 255, 255)
NEGRO     = (  0,   0,   0)
ROJO      = (255,   0,   0)
AMARILLO  = (255, 255,   0) 
AZUL      = (  0,   0, 200)
AZULC     = (  0,   0, 255)
VERDE     = (  0, 255,   0)

# BASE Y ALTO DE LAS CUADRICULAS
BASE = 35
ALTO = 35
var_1 = 0
var_2 = 0
# MARGEN entre las cuadriculas
MARGEN = 2

#CREAMOS EL TABLERO DEL JUGADOR
TableroJugador = []

for row in range(10):
    TableroJugador.append([])
    for column in range(10):
        TableroJugador[row].append(0)

#CREAMOS EL TABLERO DEL CONTRICANTE
TableroEnemigo = []

for row in range(10):
    TableroEnemigo.append([])
    for column in range(10):
        TableroEnemigo[row].append(0)

#CODIGO PARA PROBAR LAS COORDENADAS
bucle = 0
while bucle != 1:
    a = int(input("Ingrese la coordenada en X:"))
    b = int(input("Ingrese la Coordenada en Y:"))
    v = int(input("Ingrese si va a ser vertical u horizontal: "))
    while True:
        n = int(input("Ingrese que tipo de flota será: "))
        if n >= 2 and n <= 5:
            break
        else:
            print("La flota no puede tener ese tamaño!")
    if v == 1:
        for i in range(1):
            for j in range(n):
                TableroJugador[a][b+j] = 1
    else:
        for i in range(n):
            for j in range(1):
                TableroJugador[a+i][b] = 1
    bucle+=1    
#----------------------FLOTA ENEMIGA-----------------------------------------------
#VARIABLES RANDOM

RandomX = random.randint(0, 9)
RandomY = random.randint(0, 8)
contador = 0

#----------------------BUCLES DE NAVES (VALOR 2)-----------------------------------
#Hacemos el bucle para la nave Horizontal del enemigo
for row in range(1):
    for column in range(2):
        TableroEnemigo[RandomX][RandomY+column] = 1
#SETEO LAS VARIABLES DE RANDOM
RandomX = random.randint(0, 8)
RandomY = random.randint(0, 7)

#Hacemos el bucle para la nave  Vertical del enemigo
for row in range(2):
    for column in range(1):
        if TableroEnemigo[RandomX+row][RandomY] == 1:
            if TableroEnemigo[RandomX][RandomY] == 1:
                TableroEnemigo[RandomX][RandomY] = 0
            RandomX = random.randint(0, 8)
            RandomY = random.randint(0, 7)
            TableroEnemigo[RandomX][RandomY] = 1
            TableroEnemigo[RandomX+row][RandomY] = 1 
        else:
            TableroEnemigo[RandomX+row][RandomY] = 1

#---------------------BUCLES DE SUBMARINO (VALOR 3)-------------------------------
#Hacemos el bucle para el submarino Horizontal del enemigo.
NRandomY = random.randint(0, 7)
NRandomX = random.randint(0, 9)
for row in range(1):
    for column in range(3):
        if RandomX == NRandomX and RandomY == NRandomY:
            NRandomY = random.randint(0, 7)
            NRandomX = random.randint(0, 9)     
        TableroEnemigo[NRandomX][NRandomY+column] = 1

#Imprimimos
#for i in range(len(TableroJugador)):
 #   print(TableroJugador[i])

pg.init()

#DIMENSION DE LA VENTANA
DIMENSION_VENTANA = [1280, 700]
ventana = pygame.display.set_mode(DIMENSION_VENTANA)#LE DAMOS DIMENSIONES A LA VENTANA

pygame.display.set_caption("BattleShip")

FPS = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
            pg.quit()
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            try:
                # El usuario presiona el ratón. Obtiene su posición.
                pos = pygame.mouse.get_pos()
                # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
                var_1 = (BASE + MARGEN)
                print(var_1)
                column = pos[0]// var_1
                row = pos[1] // var_1
                # Establece esa ubicación a cero
                TableroEnemigo[row][column] = 1
                print("Click ", pos, "Coordenadas de la retícula: ", row, column)
            except:
                print("entre")
            
    ventana.fill(BLANCO)
        #DIBUJAMOS LA CUADRICULA DEL ENEMIGO:
    for fila in range(10):
        for columna in range(10):
            color = AZULC
            if TableroEnemigo[fila][columna] == 1:
                color = VERDE
            pygame.draw.rect(ventana,
                                color,
                                [(MARGEN+BASE) * columna + MARGEN+50,
                                (MARGEN+ALTO) * fila + MARGEN+50,
                                BASE,
                                ALTO])
     #DIBUJAMOS LA CUADRICULA DEL JUGADOR:
    for fila in range(10):
        for columna in range(10):
            color = AZULC
            if TableroJugador[fila][columna] == 1:
                color = VERDE
            pygame.draw.rect(ventana,
                                color,
                                [(MARGEN+BASE) * columna + MARGEN+810,
                                (MARGEN+ALTO) * fila + MARGEN+50,
                                BASE,
                                ALTO])
            
    pygame.display.flip()
    FPS.tick(60)
