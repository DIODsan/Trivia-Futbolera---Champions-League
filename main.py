BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import time
import random

puntaje = random.randint(0, 33)
iniciar_trivia = True
intentos = 0

print(CYAN + 'Bienvenido a la Trivia Futbolera' + RESET)
print('¿Cuánto sabes acerca de la Champions League?')
print('Tienes', puntaje, 'puntos')

nombre = input(YELLOW + 'Ingresa tu nombre:' + RESET)

for numero_carga in range(5, 0, -1):
    print(numero_carga)
    time.sleep(1)

print(
    '\nHola', nombre,
    'qué bueno tenerte por aquí, por favor, ecribe la letra de la alternativa de tu elección y luego presiona Enter para enviar tu respuesta, respeta las minúsculas:\n'
)

time.sleep(5)

while iniciar_trivia == True:
    intentos += 1
    puntaje = 0

    print('\nIntento número:', intentos)
    input('Presiona Enter para continuar')

    print(
        CYAN +
        '\n1. ¿Qué club tiene más títulos de Champions League en su palmarés?'
        + RESET)
    print('a) Milan')
    print('b) Bayern Munich')
    print('c) Liverpool')
    print('d) Real Madrid')

    respuesta_1 = input(GREEN + '\nTu respuesta es:' + RESET)
    while respuesta_1 not in ('a', 'b', 'c', 'd', 'f'):
        respuesta_1 = input(
            '\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')
    if respuesta_1 == 'a':
        puntaje -= 15
        print(RED + '\n¡Incorrecto!', nombre,
              'El Milan solamente tiene 7 Champions' + RESET)
    elif respuesta_1 == 'b':
        puntaje -= 15
        print(RED + '\nMal ahí', nombre,
              'El Bayern Munich solamente tiene 6 champions')
    elif respuesta_1 == 'c':
        puntaje -= 15
        print(RED + '\n¡Incorrecto!', nombre,
              'El liverpool solamente tiene 6 champions' + RESET)
    elif respuesta_1 == 'd':
        puntaje += 33
        print(
            MAGENTA + '\n¡Excelente!', nombre,
            'El Real Madrid tiene 14 títulos a fecha actual, obtuvo el último en el 2022 enfrentando al Liverpool en la final.'
            + RESET)
    else:
        puntaje -= 50
        print(
            '\n¿Por qué pusiste la f? ¿te quivocaste? ¿te caíste de cabeza de chiquito? ja ja ja pues te quito 50 puntos por bobi, mal ahí',
            nombre,
        )
    print('\nTienes', puntaje, 'puntos por ahora, ¡Vamos, tú puedes!')

    time.sleep(3)

    print(
        CYAN +
        '\n2. ¿Quién es el jugador que tiene más títulos ganados de Champions League   de todos los tiempos?'
        + RESET)
    print('a) Cristiano Ronaldo')
    print('b) Francisco Gento')
    print('c) Alfredo Di Stéfano')
    print('d) Paolo Maldini')

    respuesta_2 = input(GREEN + '\nTu respuesta es:' + RESET)
    while respuesta_2 not in ('a', 'b', 'c', 'd'):
        respuesta_2 = input(
            'Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')
    if respuesta_2 == 'a':
        puntaje -= 15
        print(
            RED + '\n¡Fallaste!', nombre,
            'Cristiano Ronaldo está cerca, pero solo tiene 5 Champions.' +
            RESET)
    elif respuesta_2 == 'c':
        puntaje -= 15
        print(
            RED + '\n¡Incorrecto!', nombre,
            'Alfredo Di Stéfano solo consiguió 5 champions en toda su carrera.'
            + RESET)
    elif respuesta_2 == 'd':
        puntaje -= 15
        print(
            RED + '\n¡Incorrecto!', nombre,
            'Paolo Maldini solo pudo obtener 5 champions en su carrera.' +
            RESET)
    else:
        puntaje += random.randint(0, 10)
        puntaje += 33
        print(
            MAGENTA +
            '\n¡Correcto! Francisco Gento consiguió 6 título de Copa de Europa o Champions League con el Real Madrid.'
            + RESET)
    print('\nAhora tienes', puntaje, 'puntos, dale dale dalee')

    time.sleep(3)

    print(
        CYAN +
        '\n3. ¿Quién es el máximo goleador de la historia de la Champions League?'
        + RESET)
    print('a) Lionel Messi')
    print('b) Robert Lewandowski')
    print('c) Cristiano Ronaldo')
    print('d) Karim Benzema')

    respuesta_3 = input(GREEN + '\nTu respuesta es:' + RESET)
    while respuesta_3 not in ('a', 'b', 'c', 'd'):
        respuesta_3 = input(
            'Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')
    if respuesta_3 == 'a':
        puntaje -= 15
        print(
            RED + '\n¡Fallaste!', nombre,
            'Lionel Messi está cerca, pero solo tiene 125 anotaciones en esta competición por el momento.'
            + RESET)
    elif respuesta_3 == 'b':
        puntaje -= 15
        print(
            RED + '\n¡Incorrecto!', nombre,
            'Robert Lewandowski solo tiene 89 anotaciones hasta ahora.' +
            RESET)
    elif respuesta_3 == 'd':
        puntaje -= random.randint(0, 50)
        puntaje -= 15
        print(
            RED + '\n¡Nada que ver!', nombre,
            'Karim Benzema cuenta solo con 86 goles anotados por el momento.' +
            RESET)
    else:
        puntaje += 34
        print(
            MAGENTA + '\n¡Siuuuuu!', nombre,
            'Así es, el bicho tiene 140 goles registrados en esta competición hasta la fecha.'
            + RESET)

    print('\nTe mantienes en la lucha con', puntaje,
          'puntos, solo una más, ¡vamos!')

    time.sleep(3)

    print(
        CYAN +
        '\n4. ¿Cuál es el gol más rápido en la historia de la Champions League?'
        + RESET)
    print('a) Roy Makaay, 10,12 segundos')
    print('b) Jonas, 10,90 segundos')
    print('c) Gilberto Silva, 20,00 segundos')
    print('d) Alessandro Del Piero, 20,10 segundos')

    respuesta_4 = input(GREEN + '\nTu respuesta es:' + RESET)
    while respuesta_4 not in ('a', 'b', 'c', 'd'):
        respuesta_4 = input(
            'Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')
    if respuesta_4 == 'b':
        puntaje = puntaje + 5
        print(
            RED + '\n¡Muy cerca!', nombre,
            'pero no, El gol de Jonas en el Valencia vs Bayern Leverkusen en el 2012 no es el más rápido.'
            + RESET)
    elif respuesta_4 == 'c':
        puntaje = puntaje - 10
        print(
            RED + '\n¡Meh!', nombre,
            'El gol de Gilberto Silva en el Arsenal vs PSV del 2002 no es tan rápido.'
            + RESET)
    elif respuesta_4 == 'd':
        puntaje -= random.randint(0, 10)
        puntaje = puntaje / 2
        print(
            RED + '\n¡Nada que ver!', nombre,
            'Es engañoso, lo sé, pero el gol de Alessandro Del Piero en el Juventus vs Manchester United del 1997 es el más lento de las opciones.'
            + RESET)
    else:
        puntaje = puntaje * 1.5
        print(
            MAGENTA + '\n¡Esooooo!', nombre,
            'Acertado, Roy Makaay posee este récord desde el 7 de marzo de 2007 tras anotar el 1 a 0 jugando en el Bayern Munich contra el Real Madrid.'
            + RESET)

    print(YELLOW + '\nBuen trabajo', nombre, 'has obtenido', puntaje,
          'puntazos.' + RESET)

    print('\n¿Deseas una nueva oportunidad?')
    repetir_trivia = input(
        'Ingresa si para repetir, o cualquier otra tecla para finalizar:'
    ).lower()

    if repetir_trivia != 'si':
        print(
            '\n', nombre,
            'Espero que te haya gustado la trivia y hayas pasado un agradable momento, ¡nos vemos en una próxima oportunidad!'
        )
        iniciar_trivia = False
