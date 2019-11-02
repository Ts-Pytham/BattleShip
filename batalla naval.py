import pygame, sys, random, os
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

#----------------------------------------FUNCIONES---------------------------------
def comprobar_random(valor, modo = 0):
    global RandomX, RandomY
    cont = 0
    pv = True
    #Este bucle comprueba si hay un barco cerca
    while True:
        if modo == 0:
            if pv:
                RandomX = random.randint(0, 9)
                RandomY = random.randint(0, 9-valor)
                print(f"Valor X: {RandomX}, Valor Y: {RandomY}")
                pv = False

            if TableroEnemigo[RandomX][RandomY+cont] == 1:
                RandomX = random.randint(0, 9)
                RandomY = random.randint(0, 9-valor)
                print(f"Valor Nuevo de X: {RandomX}, Valor Y: {RandomY}")
                cont = 0
            else:
                cont+=1

        elif modo == 1:
            if pv:
                RandomX = random.randint(0, 9-valor)
                RandomY = random.randint(0, 9)
                print(f"Valor X: {RandomX}, Valor Y: {RandomY}")
                pv = False
                
            if TableroEnemigo[RandomX+cont][RandomY] == 1:
                RandomX = random.randint(0, 9-valor)
                RandomY = random.randint(0, 9)
                print(f"Nuevo valor de X: {RandomX}, Valor Y: {RandomY}")
                cont = 0
            else:
                cont+=1
        if cont == valor:
            break


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

comprobar_random(2, 1)
#Hacemos el bucle para la nave  Vertical del enemigo
for row in range(2):
    for column in range(1):
            TableroEnemigo[RandomX+row][RandomY] = 1

#---------------------BUCLES DE SUBMARINO (VALOR 3)-------------------------------
"""
    Esta funcion busca si en las coordenadas se encuentra un 1, si es así setea 
    las variables random para comprobar que no haya ningun barco y no se peguen
    El primer parámetro es la cantidad de iteraciones y la segunda es el modo
    si es vertical (1) u horizontal (0), aunque si se elimina la segunda variable
    será 0 por defecto. 
"""
comprobar_random(3, 0)
#Hacemos el bucle para el submarino Horizontal del enemigo.
for row in range(1):
    for column in range(3):
        TableroEnemigo[RandomX][RandomY+column] = 1

#------------------BUCLES DEL CRUCERO O COMO SE LLAME :V (VALOR 4)----------------

comprobar_random(4, 1)

#Hacemos el bucle para el crucero Vertical del enemigo.
for row in range(4):
    for column in range(1):
        TableroEnemigo[RandomX+row][RandomY] = 1


#----------------BUCLES DE PORTA-AVIONES (VALOR 5)-------------------------------
probabilidad = random.randint(0, 1)

comprobar_random(5, probabilidad)

if probabilidad == 0:
    #El porta-aviones será horizontal
    for row in range(1):
        for column in range(5):
            TableroEnemigo[RandomX][RandomY+column] = 1

else:
    #El porta-aviones será vertical
    for row in range(5):
        for column in range(1):
            TableroEnemigo[RandomX+row][RandomY] = 1


#Imprimimos
#for i in range(len(TableroJugador)):
 #   print(TableroJugador[i])

#Para encontrar cualquier imagen de manera efizcas.
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, 'img')

pg.init()

#Cargar Imágenes
icon = pygame.image.load(os.path.join(image_path, 'icon.png'))

#DIMENSION DE LA VENTANA
DIMENSION_VENTANA = [1280, 700]
ventana = pygame.display.set_mode(DIMENSION_VENTANA)#LE DAMOS DIMENSIONES A LA VENTANA

pygame.display.set_caption("BattleShip")

pygame.display.set_icon(icon)

FPS = pygame.time.Clock() #Se obtiene la velocidad de cuadros

#-----------------------------------FUENTES-----------------------------------------
arial = pygame.font.SysFont("arial", 30)

#-----------------------------------Textos------------------------------------------


#BUCLE PRINCIPAL
while True:
    tiempo = int(pygame.time.get_ticks()/1000) #Calcula el tiempo

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
    

    T_tiempo = arial.render(f"Tiempo: {tiempo}",0, NEGRO) 
    ventana.blit(T_tiempo, (0, 0))      
    pygame.display.flip()
    FPS.tick(60) #Se ajusta la velocidad de fotogramas per segundos a 60
