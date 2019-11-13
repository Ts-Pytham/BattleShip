import pygame, sys, random, os
import tkinter as tk
from tkinter import font
import pygame as pg
from tkinter import messagebox

#COLORES
BLANCO    = (255, 255, 255)
NEGRO     = (  0,   0,   0)
ROJO      = (255,   0,   0)
AMARILLO  = (255, 255,   0) 
AZUL      = (  0,   0, 200)
AZULC     = (  0,   0, 255)
VERDE     = (  0, 255,   0)

# BASE Y ALTURA DE LAS CUADRICULAS
BASE = 30
ALTO = 30

# MARGEN entre las cuadriculas
MARGEN = 2

# VARIABLE CONTADORA DE TURNOS
turnos = 0

# VARIABLE PARA COMENZAR EL JUEGO Y CAMBIAR DE ESCENA
cambiar_escena = 0

comenzar = 0

# VARIABLE PARA ELEGIR EL MODO
menu = 0

# VARIABLE PARA ELEGIR EL BARCO
elegir_barco = 1

barco_elegido = 0

# VARIABLE DE TIPO LISTA PARA PONER LOS BARCOS
poner_barcos = [0, 0, 0, 0, 0, 0]


#NOMBRE DEL USUARIO

usuario = ""

#Clave secreta
extremo = False

# SABER SI GANAMOS
ganar_bot = 0

ganar_jugador = 0

# VARIABLE PARA SABER EL TIEMPO DEL TURNO DEL BOT
tiempo_turno = 0
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
    pv = True # pv = primera vez
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

def cuadricula_j():
    for i in range(len(TableroJugador)):
        print(TableroJugador[i])

    """
    EN LAS FUNCIONES ANTERIORES ENCONTRAMOS 4 PARÁMETROS, ABAJO ESTÁ LA EXPLICACIÓN
    size = tamaño del barco.
    posx = posición en x del barco.
    posy = posición en y del barco.
    modo/eje = eje del barco, si se encuentra horizontal o vertical.

    """
def crear_barcos(size, posx, posy, modo):
    if modo == 1:
        for i in range(1):
            for j in range(size):
                TableroJugador[posx][posy+j] = 1
    else:
        for i in range(size):
            for j in range(1):
                TableroJugador[posx+i][posy] = 1


def comprobar_barco(size, posx, posy, eje):
    valor = 0
    if eje == 1:
        for i in range(1):
            for j in range(size):
                if TableroJugador[posx][posy+j] == 1:
                    valor = 1
    else:
        for i in range(size):
            for j in range(1):
                if TableroJugador[posx+i][posy] == 1:
                    valor = 1
    return valor

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

#--------------------------PYGAME---------------------------------------
#Para encontrar cualquier imagen de manera efizcas.
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, 'img')
sound_path = os.path.join(current_path, 'sound')
sound_path2 = os.path.join(sound_path, 'effects')

pg.init() #INICIALIZO PYGAME

#-----------------------Cargar Imágenes-----------------------------------

icon = pygame.image.load(os.path.join(image_path, 'icon.png'))

main = pygame.image.load(os.path.join(image_path, 'main.png'))

fondo = pygame.image.load(os.path.join(image_path, 'fondo.png'))

# IMAGENES QUE SE MUESTRAS SI GANASTE O PERDISTE
fondo_game_over = pygame.image.load(os.path.join(image_path, 'game_over.jpeg'))

fondo_ganaste = pygame.image.load(os.path.join(image_path, 'ganaste.jpeg'))

# IMAGENES PARA SELECCIONAR 

icon_selection = pygame.image.load(os.path.join(image_path, 'icon_selection.png'))

icon_selection_boat = pygame.image.load(os.path.join(image_path, 'icon_selection_boat.png'))


# SPRITES DE LOS BARCOS (para la cuadricula)
barco1_h = pygame.image.load(os.path.join(image_path, 'barco1_h.png'))

#SPIRTES DE LOS BARCOS (para elegirlos)
barco1_selection = pygame.image.load(os.path.join(image_path, 'barco1_selection.png'))
barco2_selection = pygame.image.load(os.path.join(image_path, 'barco2_selection.png'))
barco3_selection = pygame.image.load(os.path.join(image_path, 'barco3_selection.png'))
barco4_selection = pygame.image.load(os.path.join(image_path, 'barco4_selection.png'))
barco5_selection = pygame.image.load(os.path.join(image_path, 'barco5_selection.png'))

#CARGAS SONIDOS

s_menu = pygame.mixer.Sound(os.path.join(sound_path2, 'effect1.wav'))

s_bomb = pygame.mixer.Sound(os.path.join(sound_path2, 'effect2.wav'))
s_bomb.set_volume(0.3) #El volumen del efecto será de 30%

s_presionar = pygame.mixer.Sound(os.path.join(sound_path2, 'effect3.wav'))

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
    global turnos, pos, ganar_jugador, comenzar
    """
        Acerca de la función: Esta función nos sirve para mostrar el ataque en la
        cuadricula, pero antes comprueba si el usuario al darle clic encuentra una
        flota enemigo, si es así muestra otro tipo de color.

    """
    if comenzar == 1:
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
                turnos = 0
                s_bomb.set_volume(0.15)
                s_bomb.play()
                ganar_jugador+=1

            elif TableroEnemigo[row][column] == 2 or TableroEnemigo[row][column] == 3: #Si lo destruye
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
    global RandomX, RandomY, ganar_bot
    RandomX = random.randint(0, 9)
    RandomY = random.randint(0, 9)
    if extremo == False:
        while True:              
            if TableroJugador[RandomX][RandomY] == 3 or TableroJugador[RandomX][RandomY] == 2:
                RandomX = random.randint(0, 9)
                RandomY = random.randint(0, 9)

            elif TableroJugador[RandomX][RandomY] == 1:
                TableroJugador[RandomX][RandomY] = 2
                ganar_bot+=1
                break
                    
            if TableroJugador[RandomX][RandomY] == 0:
                TableroJugador[RandomX][RandomY] = 3
                break       
    else:
        ataque = 0
        for row in range(10):
            for column in range(10):
                if TableroJugador[row][column] == 1:
                    TableroJugador[row][column] = 2 
                    ataque = 1
                    ganar_bot+=1
                    break
            if ataque == 1:
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




def coordenadas_numeros(valor = 0):
    incre = 0
    increx = 0
    increy = 0
    for _ in range(10):
        ASCII = chr(48+incre)
        if valor == 0:
            F_letras = helverica.render(f"{ASCII}",0, NEGRO)
            incre+=1 
            ventana.blit(F_letras, (8+increx, 330))
            ventana.blit(F_letras, (970+increx, 330))
            increx+=32
        else:
            F_letras = helverica.render(f"{ASCII}",0, NEGRO)
            ventana.blit(F_letras, (325, 4+increy))
            ventana.blit(F_letras, (325, 374+increy))
            ventana.blit(F_letras, (940, 4+increy))
            ventana.blit(F_letras, (940, 374+increy))
            incre+=1 
            increy+=32


def esperar_turno():
    global tiempo_turno
    if tiempo_turno >= 500:
        ataque_bot()



def transicion(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 150):
        fade.set_alpha(alpha)
        ventana.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

def crear_sprites_barcos():
    # POSICIONAMOS EL ICONO PARA SELECCIONAR EL BARCO EN X = 500, Y = 500

    # BARCO VALOR 2
    if poner_barcos[5] == 0:
        if poner_barcos[0] == 0:
            ventana.blit(barco1_selection, (370, 460))
        # BARCO VALOR 3
        if poner_barcos[1] == 0:
            ventana.blit(barco2_selection, (470, 460))
        # BARCO VALOR 4
        if poner_barcos[2] == 0:
            ventana.blit(barco4_selection, (570, 460))
        # BARCO VALOR 4 (SUBMARINO)
        if poner_barcos[3] == 0:
            ventana.blit(barco3_selection, (670, 460))
        # BARCO VALOR 5 (PORTA-AVIONES)
        if poner_barcos[4] == 0:
            ventana.blit(barco5_selection, (770, 460))

    seleccionar_barco()


def seleccionar_barco():
    global elegir_barco, poner_barcos
    if poner_barcos[5] == 0:
        if elegir_barco == 1:
            ventana.blit(icon_selection_boat, (390, 300))
        elif elegir_barco == 2:
            ventana.blit(icon_selection_boat, (490, 300))
        elif elegir_barco == 3:
            ventana.blit(icon_selection_boat, (590, 300))
        elif elegir_barco == 4:
            ventana.blit(icon_selection_boat, (690, 300))
        else:
            ventana.blit(icon_selection_boat, (790, 300))
    


#--------------------------------------FUNCIONES TKINTER------------------------------
def comprobar_nombre():
    if len(tusuario.get()) < 4:
        messagebox.showwarning("¡ERROR!","¡El usuario debe tener más de 4 caracteres!")
    elif len(tusuario.get()) > 12:
        messagebox.showwarning("¡ERROR!","¡El usuario no puede contener más de 12 caracteres!")
    else:
        raiz.destroy()

def mostrar_nombre():
    global extremo
    usuario = tusuario.get()
    if usuario == "raul":
        extremo = True
    F_usuario = helverica.render(f"Usuario: {usuario}",0, NEGRO)
    ventana.blit(F_usuario, (500,0))


def mostrar_mensaje():
    global tusuario, raiz, ComicFont
    raiz = tk.Tk()
    raiz.geometry("700x300")
    raiz.resizable(0, 0)
    raiz.title("Battleship")
    tusuario = tk.StringVar()
    ComicFont = font.Font(family="Comic Sans", size=12, weight="bold")
    tk.Label(raiz, text="¡Hola Usuario! ¿Cómo se encuentra? Bienvenido a BattleShip, primero", font=ComicFont).pack()
    tk.Label(raiz, text="que nada espero que hayas leido las reglas, quiero que ingreses tu", font=ComicFont).pack()
    tk.Label(raiz, text="nombre de usuario en el recuadro de abajo.", font=ComicFont).pack()
    tk.Entry(raiz, width = 30, textvariable=tusuario).pack()
    tk.Button(raiz, width=20, bd = 2, text="Aceptar nombre", command= comprobar_nombre ).pack()
    tk.Label(raiz, text="El usuario debe tener más de 4 caracteres y menos de 12 caracteres.", font=ComicFont).pack()
    raiz.mainloop()


def barcos_cuadricula():
    global poner_barcos, posx, posy, eje, raiz
    raiz = tk.Tk()

    # VARIABLES A USAR:
    posx = tk.IntVar()
    posy = tk.IntVar()
    eje  = tk.IntVar()

    #Propiedades de la ventana
    raiz.geometry("300x500")
    raiz.resizable(0, 0)
    raiz.title("Battleship")
    raiz.config(bg = "white")

    # FUENTE

    ComicFont = font.Font(family="Comic Sans", size=12, weight="bold")

    if elegir_barco == 1:
        tk.Label(raiz, text="NAVE [VALOR 2]",  font=ComicFont, bg = "white").pack(side = tk.TOP, pady = 15)
    elif elegir_barco == 2:
        tk.Label(raiz, text="BARCO [VALOR 3]",  font=ComicFont, bg = "white").pack(side = tk.TOP, pady = 15)
    elif elegir_barco == 3:
        tk.Label(raiz, text="SUBMARINO [VALOR 3]",  font=ComicFont, bg = "white").pack(side = tk.TOP, pady = 15)
    elif elegir_barco == 4:
        tk.Label(raiz, text="DESTROYER [VALOR 4]",  font=ComicFont, bg = "white").pack(side = tk.TOP, pady = 15)
    else:
        tk.Label(raiz, text="PORTA-AVIONES [VALOR 5]", font=ComicFont, bg = "white").pack(side = tk.TOP, pady = 15)

    Frame = tk.Frame(raiz, bg = "white")
    Frame.pack()    
    tk.Label(Frame, text="X: ", font=ComicFont, bg = "white").grid(row = 0, column = 0)
    tk.Entry(Frame, textvariable = posx, width = 12, font=ComicFont, bg = "white" ).grid(row = 0, column = 1)

    tk.Label(Frame, text="Y: ", font=ComicFont, bg = "white").grid(row = 1, column = 0, pady = 15)
    tk.Entry(Frame, textvariable = posy, width = 12, font=ComicFont, bg = "white" ).grid(row = 1, column = 1)
    
    tk.Radiobutton(Frame, text="Horizontal", value = 1, variable = eje, font=ComicFont, bg = "white" ).grid(row = 2, column = 0, pady = 15)
    tk.Radiobutton(Frame, text="Vertical", value = 2, variable = eje, font=ComicFont, bg = "white" ).grid(row = 2, column = 1)

    tk.Button(raiz, text = "Aceptar", command = colocar_barco, bg = "white", font = ComicFont).pack()
    raiz.mainloop()  


def colocar_barco():
    global posx, posy, eje, elegir_barco, barco_elegido
    if elegir_barco == 1:
        if eje.get() == 0:
            messagebox.showerror("¡ERROR!", "¡No especificaste el eje del barco!")
        if eje.get() == 1:
            if (posx.get() > 9 or posy.get() > 8) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 9 and posy.get() <= 8) and (posx.get() >= 0 and posy.get() >= 0):
                    if comprobar_barco(2, posx.get(), posy.get(), 1) == 1:
                        messagebox.showerror("¡ERROR!", "¡La posicion elegida contiene está ocupado por un barco!")
                    else:
                        crear_barcos(2, posx.get(), posy.get(), 1)
                        raiz.destroy()
                        poner_barcos[0] = 1
                        elegir_barco = 2
                        barco_elegido+=1
        if eje.get() == 2:
            if (posx.get() > 8 or posy.get() > 9) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 8 and posy.get() <= 9) and (posx.get() >= 0 and posy.get() >= 0):
                    if comprobar_barco(2, posx.get(), posy.get(), 2) == 1:
                        messagebox.showerror("¡ERROR!", "¡La posicion elegida contiene está ocupado por un barco!")
                    else:
                        crear_barcos(2, posx.get(), posy.get(), 2)
                        raiz.destroy()
                        poner_barcos[0] = 1
                        elegir_barco = 2
                        barco_elegido+=1

    elif elegir_barco == 2:
        if eje.get() == 0:
            messagebox.showerror("¡ERROR!", "¡No especificaste el eje del barco!")
        if eje.get() == 1:
            if (posx.get() > 9 or posy.get() > 7) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 9 and posy.get() <= 7) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(3, posx.get(), posy.get(), 1)
                    raiz.destroy()
                    poner_barcos[1] = 1
                    elegir_barco = 3
                    barco_elegido+=1

        if eje.get() == 2:
            if (posx.get() > 7 or posy.get() > 9) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 7 and posy.get() <= 9) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(3, posx.get(), posy.get(), 2)
                    raiz.destroy()
                    poner_barcos[1] = 1
                    elegir_barco = 3
                    barco_elegido+=1

    elif elegir_barco == 3:
        if eje.get() == 0:
            messagebox.showerror("¡ERROR!", "¡No especificaste el eje del barco!")
        if eje.get() == 1:
            if (posx.get() > 9 or posy.get() > 7) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 9 and posy.get() <= 7) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(3, posx.get(), posy.get(), 1)
                    raiz.destroy()
                    poner_barcos[2] = 1
                    elegir_barco = 4
                    barco_elegido+=1

        if eje.get() == 2:
            if (posx.get() > 7 or posy.get() > 9) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 7 and posy.get() <= 9) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(3, posx.get(), posy.get(), 2)
                    raiz.destroy()
                    poner_barcos[2] = 1
                    elegir_barco = 4
                    barco_elegido+=1


    elif elegir_barco == 4:
        if eje.get() == 0:
            messagebox.showerror("¡ERROR!", "¡No especificaste el eje del barco!")
        if eje.get() == 1:
            if (posx.get() > 9 or posy.get() > 6) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 9 and posy.get() <= 6) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(4, posx.get(), posy.get(), 1)
                    raiz.destroy()
                    poner_barcos[3] = 1
                    elegir_barco = 5
                    barco_elegido+=1
        if eje.get() == 2:
            if (posx.get() > 6 or posy.get() > 9) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 6 and posy.get() <= 9) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(4, posx.get(), posy.get(), 2)
                    raiz.destroy()
                    poner_barcos[3] = 1
                    elegir_barco = 5
                    barco_elegido+=1

    elif elegir_barco == 5:
        if eje.get() == 0:
            messagebox.showerror("¡ERROR!", "¡No especificaste el eje del barco!")
        if eje.get() == 1:
            if (posx.get() > 9 or posy.get() > 5) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 9 and posy.get() <= 5) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(5, posx.get(), posy.get(), 1)
                    raiz.destroy()
                    poner_barcos[4] = 1
                    elegir_barco = 1
                    barco_elegido+=1
        if eje.get() == 2:
            if (posx.get() > 5 or posy.get() > 9) or (posx.get() < 0 or posy.get() < 0):
                messagebox.showerror("¡ERROR!", "¡La posición elegida no puede ser usada porque se sale del rango!")
            elif (posx.get() <= 5 and posy.get() <= 9) and (posx.get() >= 0 and posy.get() >= 0):
                    crear_barcos(5, posx.get(), posy.get(), 2)
                    raiz.destroy()
                    poner_barcos[4] = 1
                    elegir_barco = 1
                    barco_elegido+=1

#----------------------------------FIN DE LAS FUNCIONES DE TKINTER-----------------
#BUCLE PRINCIPAL
while True:
    for evento in pygame.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
            pg.quit()
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #LLama la función atacar.
            if cambiar_escena == 1 and comenzar == 1:
                atacar()
                if turnos == 1:
                    ataque_bot()
        elif evento.type == pygame.KEYDOWN:
                if evento.key == pg.K_DOWN:
                    if cambiar_escena == 0:
                        menu+=1
                        if menu > 2:
                            menu = 0
                        s_menu.play()
                if evento.key == pg.K_UP:
                    if cambiar_escena == 0:
                        menu-=1
                        if menu < 0:
                            menu = 2
                        s_menu.play()
                if evento.key == 13:
                    if cambiar_escena == 0:
                        if menu == 0:
                            cambiar_escena = 1
                            s_presionar.play()
                            transicion(1280, 700)
                            mostrar_mensaje()
                        else:
                            sys.exit()
                            pg.quit()
                if evento.key == pg.K_LEFT:
                    if cambiar_escena == 1 and comenzar == 0 and barco_elegido <= 4:
                        elegir_barco-= 1
                        if elegir_barco < 1:
                            elegir_barco = 5
                if evento.key == pg.K_RIGHT:
                    if cambiar_escena == 1 and comenzar == 0 and barco_elegido <= 4:
                        elegir_barco+= 1
                        if elegir_barco > 5:
                            elegir_barco = 1
                if evento.key == pg.K_SPACE:
                    if cambiar_escena == 1 and comenzar == 0:
                        if poner_barcos[0] == 0 and elegir_barco == 1 and barco_elegido <= 4:
                            barcos_cuadricula()
                        elif poner_barcos[1] == 0 and elegir_barco == 2:
                            barcos_cuadricula()
                        elif poner_barcos[2] == 0 and elegir_barco == 3:
                            barcos_cuadricula()
                        elif poner_barcos[3] == 0 and elegir_barco == 4:
                            barcos_cuadricula()
                        elif poner_barcos[4] == 0 and elegir_barco == 5: 
                            barcos_cuadricula()
    

    ventana.fill(BLANCO)
    ventana.blit(fondo, (0, 0))

    if cambiar_escena == 1:
        #tiempo = int(pygame.time.get_ticks()/1000)
        #LLAMAMOS A LA CUADRICULA DEL ENEMIGO
        cuadricula_enemigo()

        #Llamamos a la cuadricula del jugador
        cuadricula_jugador()

        #Creamos otra cuadricula pero ahí es donde ataca el bot.
        cuadricula_jugador(960, 0, 1)

        #LLAMAMOS A LA CUADRIDCULA DEL ENEMIGO PERO ESTA VEZ NOS MOSTRARÁ LOS BARCOS
        #CUANDO ATAQUEMOS
        cuadricula_enemigo(960, 370, 1)

        #LLAMAMOS A LA FUNCION PARA RELLENAR LAS COORDENADAS DE LOS NUMEROS
        #PERO EN EL EJE HORIZONTAL
        coordenadas_numeros()
        #LLAMAMOS A LA FUNCION PARA RELLENAR LAS COORDENADAS DE LOS NUMEROS
        #PERO EN EL EJE VERTICAL
        coordenadas_numeros(1)

        mostrar_nombre()

        crear_sprites_barcos()

        if barco_elegido >= 5:#LO QUE HACE ES QUE NO SE USE EL PUNTERO
            poner_barcos[5] = 1
            comenzar = 1

        if ganar_bot == 16:
            print("Te gane tonto")
            ventana.blit(fondo_game_over, (0, 0))
        if ganar_jugador == 17:
            ventana.blit(fondo_ganaste, (0, 0))


    else:
        ventana.blit(main, (0, 0))
        
        if menu == 0:
            ventana.blit(icon_selection, (290, 305))
        elif menu == 1:
            ventana.blit(icon_selection, (210, 430))
        else:
            ventana.blit(icon_selection, (290, 540))

    pygame.display.flip()
    FPS.tick(60) #Se ajusta la velocidad de fotogramas per segundos a 60