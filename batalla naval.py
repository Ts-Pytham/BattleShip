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
BASE = 30
ALTO = 30

# MARGEN entre las cuadriculas
MARGEN = 2

# VARIABLE CONTADORA DE TURNOS
turnos = 0

# VARIABLE PARA COMENZAR EL JUEGO
comenzar = 0

# VARIABLE PARA ELEGIR EL MODO
menu = 0

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

#----------------------------------------FUNCIONES---------------------------------
def comprobar_random(valor, modo = 0):
    """
    Esta funcion busca si en las coordenadas se encuentra un 1, si es así setea 
    las variables random para comprobar que no haya ningun barco y no se peguen
    El primer parámetro es la cantidad de iteraciones y la segunda es el modo
    si es vertical (1) u horizontal (0), aunque si se elimina la segunda variable
    será 0 por defecto. 
    """
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

        
def cuadricula():
    for i in range(len(TableroEnemigo)):
        print(TableroEnemigo[i])


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
#Dependiendo del valor aleatorio este será horizontal (0) o vertical (1)
probabilidad = random.randint(0, 1)

comprobar_random(5, probabilidad)

if probabilidad == 0:
    for row in range(1):
        for column in range(5):
            TableroEnemigo[RandomX][RandomY+column] = 1
else:
    for row in range(5):
        for column in range(1):
            TableroEnemigo[RandomX+row][RandomY] = 1

#Para encontrar cualquier imagen de manera efizcas.
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, 'img')

pg.init()

#Cargar Imágenes
icon = pygame.image.load(os.path.join(image_path, 'icon.png'))

main = pygame.image.load(os.path.join(image_path, 'main.png'))

circle = pygame.image.load(os.path.join(image_path, 'circle.png'))

#DIMENSION DE LA VENTANA
DIMENSION_VENTANA = [1280, 700]
ventana = pygame.display.set_mode(DIMENSION_VENTANA)#LE DAMOS DIMENSIONES A LA VENTANA

pygame.display.set_caption("BattleShip")

pygame.display.set_icon(icon)

FPS = pygame.time.Clock() #Se obtiene la velocidad de cuadros

#-----------------------------------FUENTES-----------------------------------------
arial = pygame.font.SysFont("arial", 30)
helverica = pygame.font.SysFont("helverica", 40)
#-----------------------------------Funciones con pygame------------------------------------------
def atacar():
    global turnos
    """
        Acerca de la función: Esta función nos sirve para mostrar el ataque en la
        cuadricula, pero antes comprueba si el usuario al darle clic encuentra una
        flota enemigo, si es así muestra otro tipo de color.

    """
    try:
        # El usuario presiona el ratón. Obtiene su posición.
        pos = pygame.mouse.get_pos()
        # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
        var_1 = (BASE + MARGEN)
        column = pos[0]// var_1
        row = pos[1] // var_1
        # Comprueba si hay un barco
        if TableroEnemigo[row][column] == 1:
            TableroEnemigo[row][column] = 2 #Si lo hay setea la variable a 2
            turnos = 1
        elif TableroEnemigo[row][column] == 2: #Si lo destruye
            print("Ya lo destruiste!") # No pasa nada :v
            turnos = 0
        else:
            TableroEnemigo[row][column] = 3 #Valor del tiro
            turnos = 1
        #-------------------Modo desarollador--------------------------------------
        print("Click ", pos, "Coordenadas de la retícula: ", row, column)
        cuadricula()
        print(f"fila: {row}, columna: {column}")
    except:
        turnos = 0


def ataque_bot():
    global RandomX, RandomY
    RandomX = random.randint(0, 9)
    RandomY = random.randint(0, 9)
    while True:
        if TableroJugador[RandomX][RandomY] == 3 or TableroJugador[RandomX][RandomY] == 2:
            RandomX = random.randint(0, 9)
            RandomY = random.randint(0, 9)

        elif TableroJugador[RandomX][RandomY] == 1:
            TableroJugador[RandomX][RandomY] = 2
            break
        
        if TableroJugador[RandomX][RandomY] == 0:
            TableroJugador[RandomX][RandomY] = 3
            break
        


def cuadricula_jugador(distanciax = 0, distanciay = 370, modo = 0):
    for fila in range(10):
        for columna in range(10):
            color = AZULC
            if modo == 0:
                if TableroJugador[fila][columna] == 1 or TableroJugador[fila][columna] == 2:
                    color = VERDE
            else:
                if TableroJugador[fila][columna] == 3:
                    color = VERDE
                elif TableroJugador[fila][columna] == 2:
                    color = ROJO
            pygame.draw.rect(ventana,
                                color,
                                [(MARGEN+BASE) * columna + MARGEN+distanciax,
                                (MARGEN+ALTO) * fila + MARGEN+distanciay,
                                BASE,
                                ALTO])


def cuadricula_enemigo (distanciax = 0, distanciay = 0, modo = 0):
    for fila in range(10):
        for columna in range(10):
            color = AZULC
            if modo == 0:
                if TableroEnemigo[fila][columna] == 1 or TableroEnemigo[fila][columna] == 3:
                    color = VERDE
                elif TableroEnemigo[fila][columna] == 2:
                    color = ROJO
            else:
                if TableroEnemigo[fila][columna] == 2:
                    color = ROJO
            pygame.draw.rect(ventana,
                                color,
                                [(MARGEN+BASE) * columna + MARGEN+distanciax,
                                (MARGEN+ALTO) * fila + MARGEN+distanciay,
                                BASE,
                                ALTO])


def coordenadas_letras():
    incre = 0
    increy = 0
    for _ in range(10):
        ASCII = chr(65+incre)
        F_letras = helverica.render(f"{ASCII}",0, NEGRO)
        ventana.blit(F_letras, (325, 0+increy))
        ventana.blit(F_letras, (325, 370+increy))
        ventana.blit(F_letras, (940, 0+increy))
        ventana.blit(F_letras, (940, 370+increy))
        incre+=1 
        increy+=32

def coordenadas_numeros():
    incre = 0
    increx = 0
    for _ in range(10):
        ASCII = chr(48+incre)
        F_letras = helverica.render(f"{ASCII}",0, NEGRO)
        incre+=1 
        ventana.blit(F_letras, (8+increx, 330))
        ventana.blit(F_letras, (970+increx, 330))
        increx+=32
#--------------------------------------FIN DE FUNCIONES------------------------------
#BUCLE PRINCIPAL
while True:
    tiempo = 0
    for evento in pygame.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
            pg.quit()
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #LLama la función atacar.
            if comenzar == 1:
                atacar()
                if turnos == 1:
                    ataque_bot()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pg.K_DOWN:
                menu+=1
                if menu > 2:
                    menu = 0
            if evento.key == pg.K_UP:
                menu-=1
                if menu < 0:
                    menu = 2
            if evento.key == pg.K_SPACE:
                print("entre")
                if menu == 0:
                    comenzar = 1
                else:
                    sys.exit()
                    pg.quit()
            print(menu)
    ventana.fill(BLANCO)

    if comenzar == 1:
        tiempo = int(pygame.time.get_ticks()/1000) #Calcula el tiempo
        #LLAMAMOS A LA CUADRICULA DEL ENEMIGO
        cuadricula_enemigo()

        #Llamamos a la cuadricula del jugador
        cuadricula_jugador()

        #Creamos otra cuadricula pero ahí es donde ataca el bot.
        cuadricula_jugador(960, 0, 1)

        #LLAMAMOS A LA CUADRIDCULA DEL ENEMIGO PERO ESTA VEZ NOS MOSTRARÁ LOS BARCOS
        #CUANDO ATAQUEMOS
        cuadricula_enemigo(960, 370, 1)

        T_tiempo = arial.render(f"Tiempo: {tiempo}",0, NEGRO) 
        ventana.blit(T_tiempo, (1200/2, 650/2))  
        coordenadas_letras()
        coordenadas_numeros()
    else:
        ventana.blit(main, (0, 0))
        
        if menu == 0:
            ventana.blit(circle, (260, 255))
        elif menu == 1:
            ventana.blit(circle, (260, 380))
        else:
            ventana.blit(circle, (260, 490))

    pygame.display.flip()
    FPS.tick(60) #Se ajusta la velocidad de fotogramas per segundos a 60
