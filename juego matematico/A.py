import pygame
import random
import sys
import math

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption("Juego Matemático")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Fuente y tamaño
font = pygame.font.Font(None, 36)

# Variables globales para la posición de la caja de entrada
input_box_x = width // 2 - 100
input_box_y = height // 2 + 50
input_box_w = 200
input_box_h = 32

# Imagen de los corazones
corazon_img = pygame.image.load("juego matematico/img/corazon.png")
corazon_img = pygame.transform.scale(corazon_img, (40, 40))

# Clase Personaje
class Personaje:
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida

personaje1 = Personaje("jugador", 1, 100)
def mostrar_info():
    # Mostrar información en la pantalla
    info_text = f"Nivel: {personaje1.nivel}"
    text = font.render(info_text, True, black)
    screen.blit(text, (10, 10))

def mostrar_vida():
    for i in range(personaje1.vida // 20):
        screen.blit(corazon_img, (width - 50 - i * 50, 10))

def mostrar_felicidades():
    felicidades_text = font.render("¡Felicidades! Has alcanzado el nivel 12.", True, (0, 255, 0))
    screen.blit(felicidades_text, (width // 2 - felicidades_text.get_width() // 2, height // 2 - felicidades_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Mostrar el mensaje de felicitaciones durante 2 segundos
    screen.fill(white)

def hacer_pregunta(operador):
    a = random.randint(1, 3 * personaje1.nivel)
    b = random.randint(1, 3 * personaje1.nivel)
    c = random.randint(1, 3 * personaje1.nivel)


    if operador == '+':
        respuesta_correcta = a + b
        pregunta = f"¿Cuánto es {a} + {b}?"
    elif operador == 'MH':
        respuesta_correcta = a + b
        pregunta = f"¿Cuánto es {a} + {b}?"
    elif operador == '-':
        respuesta_correcta = a - b
        pregunta = f"¿Cuánto es {a} - {b}?"
    elif operador == '*':
        respuesta_correcta = a * b
        pregunta = f"¿Cuánto es {a} * {b}?"

    elif operador == '/':
        respuesta_correcta = a
        pregunta = f"¿Cuánto es {a * b} / {b}?"

    elif operador == 'Funciones':
        respuesta_correcta = a*c+b
        pregunta = f"Si la función es f(x) = {a}x + {b}, ¿cuál es f({c})?"

    elif operador == 'Geometría':
        figura = random.choice(['cuadrado', 'círculo', 'triángulo'])
        medida = random.choice(['cm', 'm'])

        if figura == 'cuadrado':
            lado = random.randint(1, 10)
            respuesta_correcta = lado * lado
            pregunta = f"¿Cuál es el área de un cuadrado con lado {lado} {medida}?"

        elif figura == 'círculo':
            radio = random.randint(1, 10)
            respuesta_correcta = round(math.pi * radio ** 2, 2)
            pregunta = f"¿Cuál es el área de un círculo con radio {radio} {medida}?"

        elif figura == 'triángulo':
            base = random.randint(1, 10)
            altura = random.randint(1, 10)
            respuesta_correcta = (base * altura) / 2
            pregunta = f"¿Cuál es el área de un triángulo con base {base} {medida} y altura {altura} {medida}?"
    elif operador == 'Trigonometría':
        angulo = random.randint(0, 360)
        pregunt = random.choice(['seno','coseno','tangente'])

        if pregunt == 'seno':
            seno = math.sin(math.radians(angulo))
            respuesta_correcta = round(seno, 2)
            pregunta = f"Para un ángulo de {angulo} grados,¿Cuál es el seno? (Redondeado a 2 decimales)"

        elif pregunt == 'coseno':
            coseno = math.cos(math.radians(angulo))
            pregunta = f"Para un ángulo de {angulo} grados,¿Cuál es el coseno? (Redondeado a 2 decimales"
            respuesta_correcta = round(coseno, 2)

        elif pregunt == 'tangente':
            tangente = math.tan(math.radians(angulo))
            pregunta = f"Para un ángulo de {angulo} grados,¿Cuál es la tangente? (Redondeado a 2 decimales)"
            respuesta_correcta = round(tangente, 2)
    elif operador == 'Sucesiones':

        # Crear la sucesión (10 términos)
        sucesion = [a + i * b for i in range(10)]

        # Convertir la sucesión a texto para la pregunta
        sucesion_texto = ', '.join(map(str, sucesion))

        # Encontrar el término siguiente en la sucesión
        siguiente = a + 10 * b

        pregunta = f"Dada la sucesión: {sucesion_texto}, ¿cuál es el siguiente término?"
        respuesta_correcta = siguiente
    elif operador == 'Sumatorias':
        sumatoria = sum(range(a, b + 1))
        pregunta = f"Dada la sumatoria: ∑(n) desde {a} hasta {b}, ¿cuál es su resultado?"
        respuesta_correcta = sumatoria
    elif operador == 'Vectores':
        # Generar componentes aleatorias para dos vectores en 2D
        vector1 = (random.randint(-10, 10), random.randint(-10, 10))
        vector2 = (random.randint(-10, 10), random.randint(-10, 10))

        # Calcular la suma de los vectores
        suma_vectorial = (vector1[0] + vector2[0], vector1[1] + vector2[1])

        pregunta = f"Dados los vectores v1 = {vector1} y v2 = {vector2}, ¿cuál es v1 + v2?"
        respuesta_correcta = suma_vectorial
    elif operador == 'Matrices':
        # Generar matrices aleatorias 2x2
        matriz1 = [[random.randint(-5, 5) for _ in range(2)] for _ in range(2)]
        matriz2 = [[random.randint(-5, 5) for _ in range(2)] for _ in range(2)]

        # Calcular la suma de las matrices
        suma_matrices = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]

        pregunta = f"Dadas las matrices:{matriz1} y {matriz2}, ¿cuál es su suma?"
    
        respuesta_correcta = suma_matrices

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    input_box = pygame.Rect(input_box_x, input_box_y, input_box_w, input_box_h)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                    # Verificar si el operador no es 'MH'
                    
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if operador=='MH':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2 :
                                    hacer_pregunta('+') 
                                elif personaje1.nivel == 3 or personaje1.nivel == 4:
                                    hacer_pregunta('-') 
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('*')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('/')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Funciones')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Geometría')
                                elif personaje1.nivel == 13 or personaje1.nivel == 14 :
                                    hacer_pregunta('Trigonometría')
                                elif personaje1.nivel == 15 or personaje1.nivel == 16 :
                                    hacer_pregunta('Sucesiones')
                                elif personaje1.nivel == 17 or personaje1.nivel == 18 :
                                    hacer_pregunta('Sumatorias')
                                elif personaje1.nivel == 19 or personaje1.nivel == 20 :
                                    hacer_pregunta('Vectores')
                                elif personaje1.nivel == 21 or personaje1.nivel == 22 :
                                    hacer_pregunta('Matrices')
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='+':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('+')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('+')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('+')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('+')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('+')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('+')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  

                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

                if operador=='-':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('-')  # Cambiar a preguntas de resta en el nivel 2
        
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-2]
                    else:
                        text += event.unicode
                if operador=='/':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('/')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('/')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('/')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('/')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('/')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('/')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='-':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('-')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('-')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('-')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('-')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('-')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('-')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Funciones':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Funciones')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Funciones')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Funciones')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Funciones')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Funciones')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Funciones')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Geometría':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Geometría')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Geometría')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Geometría')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Geometría')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Geometría')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Geometría')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Trigonometría':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Trigonometría')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Trigonometría')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Trigonometría')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Trigonometría')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Trigonometría')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Trigonometría')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Sucesiones':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Sucesiones')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Sucesiones')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Sucesiones')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Sucesiones')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Sucesiones')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Sucesiones')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Sumatorias':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Sumatorias')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Sumatorias')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Sumatorias')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Sumatorias')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Sumatorias')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Sumatorias')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Vectores':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Vectores')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Vectores')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Vectores')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Vectores')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Vectores')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Vectores')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if operador=='Matrices':
                    if event.key == pygame.K_RETURN:
                        try:
                            respuesta_usuario = int(text)
                            if respuesta_usuario == respuesta_correcta:
                                mostrar_respuesta("¡Respuesta correcta!", True)
                                personaje1.nivel += 1
                                if personaje1.nivel == 2:
                                    hacer_pregunta('Matrices')  # Cambiar a preguntas de resta en el nivel 2
                                elif 3 <= personaje1.nivel <= 4:
                                    hacer_pregunta('Matrices')  # Volver a preguntas de suma en los niveles 3 y 4
                                elif personaje1.nivel == 5 or personaje1.nivel == 6:
                                    hacer_pregunta('Matrices')
                                elif personaje1.nivel == 7 or personaje1.nivel == 8:
                                    hacer_pregunta('Matrices')
                                elif personaje1.nivel == 9 or personaje1.nivel ==10:
                                    hacer_pregunta('Matrices')
                                elif personaje1.nivel == 11 or personaje1.nivel == 12 :
                                    hacer_pregunta('Matrices')
                                if personaje1.nivel >= 12:
                                    mostrar_felicidades()  # Mostrar mensaje de felicitaciones
                                    menu_principal()  
                            else:
                                mostrar_respuesta("Respuesta incorrecta :(", False)
                                quitar_vida()
                        except ValueError:
                            pass
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
                    

        screen.fill(white)
        mostrar_info()
        mostrar_vida()
        pygame.draw.rect(screen, color, input_box)
        txt_surface = font.render(text, True, black)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        text_pregunta = font.render(pregunta, True, black)
        screen.blit(text_pregunta, (width // 2 - text_pregunta.get_width() // 2, height // 2 - text_pregunta.get_height() // 2))
        pygame.display.flip()
        clock.tick(30)
        

def quitar_vida():
    personaje1.vida -= 20
    if personaje1.vida <= 0:
        personaje1.vida = 100
        personaje1.nivel = 1
        mostrar_respuesta("¡Te quedaste sin vida! Reiniciando al nivel 1", False)
    mostrar_vida()

def mostrar_respuesta(mensaje, es_correcta):
    color = (0, 255, 0) if es_correcta else (255, 0, 0)
    respuesta_text = font.render(mensaje, True, color)
    screen.blit(respuesta_text, (width // 2 - respuesta_text.get_width() // 2, height // 2 + 100))
    pygame.display.flip()
    pygame.time.wait(1000)  # Mostrar la respuesta durante 1 segundo
    screen.fill(white)  # Limpiar la pantalla después de mostrar la respuesta

def menu_principal():
    clock = pygame.time.Clock()
    menu_font = pygame.font.Font(None, 24)  # Ajustar el tamaño de la fuente
    opciones = ["Modo Historia", "Sumas", "Restas", "Multiplicación", "División", 
                "Funciones", "Geometría", "Trigonometría", "Sucesiones", 
                "Sumatorias", "Vectores", "Matrices"]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, opcion in enumerate(opciones):
                    if 300 <= x <= 500 and 100 + i * 60 <= y <= 150 + i * 60:
                        iniciar_juego(opcion)
        
        screen.fill(white)
        titulo_text = menu_font.render("Selecciona una opción:", True, black)
        screen.blit(titulo_text, (width // 2 - titulo_text.get_width() // 2, 50))

        for i, opcion in enumerate(opciones):
            pygame.draw.rect(screen, black, (300, 100 + i * 60, 200, 40), 2)
            opcion_text = menu_font.render(opcion, True, black)
            screen.blit(opcion_text, (350, 110 + i * 60))

        pygame.display.flip()
        clock.tick(30)

def iniciar_juego(opcion):
    if opcion == "Modo Historia":
        hacer_pregunta('MH')  # Comienza con preguntas de suma
    elif opcion == "Sumas":
        hacer_pregunta('+')  # Solo preguntas de suma
    elif opcion == "Restas":
        hacer_pregunta('-')  # Solo preguntas de resta
    elif opcion == "Multiplicación":
        hacer_pregunta('*')  # Solo preguntas de multiplicación
    elif opcion == "División":
        hacer_pregunta('/')  # Solo preguntas de división
    elif opcion == "Funciones":
        hacer_pregunta('Funciones')
    elif opcion == "Geometría":
        hacer_pregunta('Geometría')
    elif opcion == "Trigonometría":
        hacer_pregunta('Trigonometría')
    elif opcion == "Sucesiones":
        hacer_pregunta('Sucesiones')
    elif opcion == "Sumatorias":
        hacer_pregunta('Sumatorias')
    elif opcion == "Vectores":
        hacer_pregunta('Vectores')
    elif opcion == "Matrices":
        hacer_pregunta('Matrices')


# Iniciar el juego con el menú principal
menu_principal()