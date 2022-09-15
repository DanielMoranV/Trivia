import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
puntaje_general = []
print (RED+"Bienvenido a mi trivia sobre computación"+RESET)
print (YELLOW+"Pondremos a prueba tus conocimientos")
# Solicitamos el nombre al participante y lo guardamos en una variable
nombre = input("\nIngresa tu nombre: "+RESET)
for numero in range (3,0,-1) :
    print (numero)
    time.sleep(1)
print(GREEN+nombre.upper()," EMPEZEMOS..."+RESET)


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = [random.randint(0,10)]
    print("Puntaje inicial: ",puntaje)
    print("\nIntento número:", intentos)
    input("Presiona Enter para continuar")

    pregunta_1 = ["¿Quién fue el creador de windows?","Linus Torvalds","Bill Gates","Mark Zuckerberg","Dennis Ritchie"]
    pregunta_2 = ["¿Quién fue el fundador de Apple?","Linus Torvalds","Bill Gates","Mark Zuckerberg","Steve Jobs"]
    pregunta_3 = ["¿Quién fue el creador de phyton?","Guido van Rossum","Bill Gates","Mark Zuckerberg","Dennis Ritchie"]
    pregunta_bonnus = ["¿En que lenguaje se progamo Minecraft?","Python","Java","PHP","Assembly"]
    alternativas = ["a","b","c","d"]
    contador = 0
    print("Primera pregunta...")

    for i in pregunta_1 :
        if i == pregunta_1[0] :
            print(CYAN+i+RESET)
        else :
            print(alternativas[contador],") ",i)
            contador +=1
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_1 = input("\nTu respuesta: ")
    # Validamos que la respuesta del usuario se encuentre entre las alternativas de lo contrario se pedira ingresar una alternativa correcta
    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    print(BLUE+"Procesando la respuesta..."+RESET)
    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    # Comprobamos si la respuesta ingresada es la correcta
    if respuesta_1 == "b" :
        print (GREEN+"Muy bien Respuesta Correcta"+RESET)
        puntaje.append(random.randint(0,10))
    else :
        print ("Respuesta incorrecta")
        puntaje.append(-random.randint(0,10))
    print (YELLOW+"Puntaje Pregunta 1: ",puntaje[1])

    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    print(BLUE+"Seguimos jugando..."+RESET)
    time.sleep(1)
    contador = 0
    print ("Segunda Pregunta...")
    for i in pregunta_2 :
        if i == pregunta_2[0] :
            print(CYAN+i+RESET)
        else :
            print(alternativas[contador],") ",i)
            contador +=1
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_2 = input("\nTu respuesta: ")
    # Validamos que la respuesta del usuario se encuentre entre las alternativas de lo contrario se pedira ingresar una alternativa correcta
    while respuesta_2 not in ("a", "b", "c", "d","x"):
        respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    print(BLUE+"Procesando la respuesta..."+RESET)
    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    # Comprobamos si la respuesta ingresada es la correcta
    if respuesta_2 == "a" :
        print ("Incorrecto: Linus Torvalds es del fundador de kernel Linux")
        puntaje.append(-random.randint(0,10))
    elif respuesta_2 == "b":
        print ("Incorrecto: Bill Gates es del fundador de Windows")
        puntaje.append(-random.randint(0,10))
    elif respuesta_2 == "c":
        print ("Incorrecto: Mark Zuckerberg es del fundador de Facebook")
        puntaje.append(-random.randint(0,10))
    elif respuesta_2 == "x":
        print (MAGENTA+"Clave secreta ingresada ¡Bonus +1000!"+RESET)
        puntaje.append(1000)
    else :
        print (GREEN+"Muy bien Respuesta Correcta"+RESET)
        puntaje.append(random.randint(0,10))
    print (YELLOW+"Puntaje Pregunta 2: ",puntaje[2])
    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    print(BLUE+"Seguimos jugando..."+RESET)
    time.sleep(1)

    contador = 0
    print ("Tercera Pregunta...")
    for i in pregunta_3 :
        if i == pregunta_3[0] :
            print(CYAN+i+RESET)
        else :
            print(alternativas[contador],") ",i)
            contador +=1
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_3 = input("\nTu respuesta: ")
    # Validamos que la respuesta del usuario se encuentre entre las alternativas de lo contrario se pedira ingresar una alternativa correcta
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    print(BLUE+"Procesando la respuesta..."+RESET)
    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    # Comprobamos si la respuesta ingresada es la correcta
    if respuesta_3 == "a" :
        print (GREEN+"Muy bien Respuesta Correcta"+RESET)
        puntaje.append(random.randint(0,10))
    else :
        print ("Respuesta incorrecta")
        puntaje.append(-random.randint(0,10))
    print (YELLOW+"Puntaje Pregunta 3: ",puntaje[3])

    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    print(BLUE+"Seguimos jugando..."+RESET)
    time.sleep(1)
    contador = 0

    print ("Pregunta BONUS...")
    for i in pregunta_bonnus :
        if i == pregunta_bonnus[0] :
            print(CYAN+i+RESET)
        else :
            print(alternativas[contador],") ",i)
            contador +=1
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_4 = input("\nTu respuesta: ")
    # Validamos que la respuesta del usuario se encuentre entre las alternativas de lo contrario se pedira ingresar una alternativa correcta
    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    print(BLUE+"Procesando la respuesta..."+RESET)
    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    # Comprobamos si la respuesta ingresada es la correcta
    if respuesta_4 == "a":
        print ("Totalmente incorrecto! ...")
        puntaje.append(sum(puntaje)/2)
    elif respuesta_4 == "d":
        print ("...")
        puntaje.append(sum(puntaje)+5)
    elif respuesta_4 == "c":
        print ("Incorrecto! ...")
        puntaje.append(sum(puntaje)-5)
    else:
        print ("Correcto! ...")
        puntaje.append(sum(puntaje)*2)
    print (YELLOW+"Puntaje Pregunta Bonnus: ",puntaje[4])
    time.sleep(1) # para ayudarnos a imaginar que vamos jugando
    print(BLUE+"Terminamos Calculando Puntaje..."+RESET)
    time.sleep(3)

    n=0
    k=0
    for i in puntaje :
        n += 1
        if n == 1 :
            print("Puntaje Inicial: ",i)
        else :
            print("Pregunta ",n-1,": ",i)
    print(GREEN+"Excelente, has obtenido", sum(puntaje), "puntos"+RESET)
    puntaje_general.append(sum(puntaje))

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

    if repetir_trivia != "si":  # != significa "distinto"
        print("\nEspero ",nombre," que lo hayas pasado bien, hasta pronto!")
        for i in puntaje_general :
            k += 1
            print("Punjate Intento: ",k," = ",i)
        print(GREEN+"Mayor puntaje: ",max(puntaje_general))
        print(RED+"Menor Puntaje: ",min(puntaje_general),RESET)
        iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
