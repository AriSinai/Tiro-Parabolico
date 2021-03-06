
def printos(surface, text, x, y, color, font):
    text_in_lines = text.split('\n')
    for line in text_in_lines:
        new = font.render(line, 1, color)
        surface.blit(new, (x, y))
        y += new.get_height()
def tabla():
    for i in range (0,180 ,20):
        pygame.draw.line(screen,(67,97,241),(5,9+i),(350,9+i),2)
        pygame.draw.line(screen,(67,97,241),(5,9),(5,170),2)
        pygame.draw.line(screen, (67, 97, 241), (350, 9), (350, 170), 2)

def arrow(screen, color, x, y, ang):
    pygame.draw.line(screen, color, (x, y), (x + 20* math.cos(math.radians(ang + 150.0)), y - 20 * math.sin(math.radians(ang + 150.0))))
    pygame.draw.line(screen, color, (x, y),(x + 20 * math.cos(math.radians(ang + 210.0)), y - 20 * math.sin(math.radians(ang + 210.0))))


def vector(screen, color, x, y, ang):
    w, z = x + v0  * math.cos(math.radians(ang)), y - v0  * math.sin(math.radians(ang))
    x, y, w, z = int(x), int(y), int(w), int(z)
    arrow(screen, color, w, z, ang)
    pygame.draw.line(screen, blue, (x, y), (w, z))



import pygame, math
imagenDora = pygame.image.load("dorab.png")
pygame.init()

size = width, height = 1200, 700

black = (246, 90, 0)
blue = (230, 37, 37)
green = (246, 46, 126)
background = (250, 189, 76)



f = 62
x = 210
y = height - f

pygame.font.init()
font = pygame.font.Font(None, 25)

clock = pygame.time.Clock()

t = 0.0
dt = 0.2

v0 = 72.0
a = 9.81
ang = 45.0

vx = 0
vy = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SIMULACIÓN")

radio = 10
df=0
cont = 1
pygame.font.init()
font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()
lock = True
lock1 = False
second = False
first = True
h = 1

'''
# La simulacion se hace 3 veces
# 3 casos para la simulacion, el primero para la distancia maxima, el segundo para el angulo que debe de estar la maquina para
# pegar al objetivo el tercero es el mismo que el segundo pero con angulo complementario
# Presionar Y despues de cada simulacion para el siguiente
# Se tuvo que cambiar la velocidad de 720m/s a 72m/s para que no se saliera del simulador, por lo que se cambio el display de estos datos'''
def hello():
    import pygame, math

    pygame.init()

    size = width, height = 1200, 700

    black = (246, 90, 0)
    blue = (230, 37, 37)
    green = (246, 46, 126)
    background = (250, 189, 76)

    f = 62
    x = 210
    y = height - f

    pygame.font.init()
    font = pygame.font.Font(None, 30)

    clock = pygame.time.Clock()

    t = 0.0
    dt = 0.2

    v0 = 72.0
    a = 9.81
    ang = 45.0

    vx = 0
    vy = 0
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("SIMULACIÓN")

    radio = 10

    df = 0
    cont = 1
    pygame.font.init()
    font = pygame.font.Font(None, 30)

    df=0
    lock=True
    lock1 = False
    second = False
    first = True
    h = 1
    while (df == 0):
        screen.fill(background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        teclado = pygame.key.get_pressed()
        printos(screen, "1) Simulacion libre", 30, 60, black, font)
        printos(screen, "2) Simulacion de caso", 30, 90, black, font)
        printos(screen, "3) Salir", 30, 120, black, font)
        if (teclado[pygame.K_1]):
            df = 1
        if (teclado[pygame.K_3]):
            df = 0
            break
        elif (teclado[pygame.K_2]):
            df = 2
        pygame.display.flip()
        clock.tick(40)
    while df == 1:

        screen.fill(background)
        screen.blit(imagenDora, (10, 630))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        teclado = pygame.key.get_pressed()
        if (tuple(set(teclado)) == (0, 1) and lock):
            if (teclado[pygame.K_UP]):
                ang += 1
                if (ang >= 90):
                    ang = 90
            if (teclado[pygame.K_DOWN]):
                ang -= 1
                if (ang < 0):
                    ang = 0
            if (teclado[pygame.K_RIGHT] and v0 < 100):
                v0 += 1
            if (teclado[pygame.K_LEFT] and v0 > 1):
                v0 -= 1
            if (teclado[pygame.K_SPACE]):
                lock = False
                lock1 = True
                vy0 = v0 * math.sin(math.radians(ang))
        if (teclado[pygame.K_ESCAPE]):
            break
        vx0 = v0 * math.cos(math.radians(ang))
        vy0 = v0 * math.sin(math.radians(ang))
        if (lock1):
            y = (height - f) - vy0 * t + .5 * a * (t ** 2)
            x = 210 + vx0 * t
            t += dt

            if (y > (height - f)):
                y = height - f

                lock1 = False
                second = True
                lock = False
        tMax = t * 10 / 2

        yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))
        if (second):
            printos(screen, "Continuar usando el simulador? Y/N", 10, 200, blue, font)
            if (teclado[pygame.K_y]):
                lock = True
                second = False
                hello()
                df = 0
                f = 62
                x = 210
            elif (teclado[pygame.K_n]):
                break
        tabla()
        printos(screen, "Desplazamineto en X = %d m" % ((x - 210) * 100), 10, 10, black, font)
        printos(screen, "Desplazamiento en Y = %d m" % ((height - f - y) * 100), 10, 31, black, font)
        printos(screen, "θ = %d grados" % (ang), 10, 51, black, font)
        printos(screen, "Velocidad inicial = %d m/s" % (v0 * 10), 10, 71, black, font)
        printos(screen, "Vx = %d m/s" % (vx0 * 10), 10, 91, black, font)
        printos(screen, "Vy = %d m/s" % (vy0 * 10), 10, 111, black, font)
        printos(screen, "t = %d s" % (t * 10), 10, 131, black, font)
        printos(screen, "Altura máxima = %d m" % (yMax), 10, 151, black, font)

        pygame.draw.circle(screen, blue, (int(x), int(y)), radio)
        vector(screen, blue, x, y, ang)

        pygame.display.flip()
        clock.tick(50)
    while (df == 2):
        dt = 0.2
        screen.fill(background)
        screen.blit(imagenDora, (10, 630))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        teclado = pygame.key.get_pressed()

        if (cont == 1 and lock):
            printos(screen, "1) Simulación: Desplazamiento maximo en X utilizando θ = 45°", 300, 250, (67, 97, 241),
                    font)

            v0 = 72
            f = 62
            ang = 45
            vy0 = v0 * math.sin(math.radians(ang))
            vx0 = v0 * math.cos(math.radians(ang))
            y = ((height - f) - vy0 * t + .5 * a * (t ** 2))
            x = (210 + vx0 * t)
            radio = 10
            tMax = t * 10 / 2
            yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))

            if (t < 2):
                vector(screen, blue, x, y, ang)

            t += dt
            if (lock1):
                y = (height - f) - vy0 * t + .5 * a * (t ** 2)
                x = 210 + vx0 * t
                t += dt

                if (y > (height - f)):
                    y = height - f

                    lock1 = False
                    second = True
                    lock = False

            if (y > (height - f)):
                y = height - f
                lock1 = False
                second = True
                lock = False

        if (cont == 2 and lock):
            printos(screen, "2)Simulación: Alcanzar objetivo del problema utilizando uno de los ángulos posibles", 250,
                    250, (67, 97, 241), font)
            v0 = 72
            ang = 14.1
            f = 62

            y = ((height - f) - vy0 * t + .5 * a * (t ** 2))
            x = (210 + vx0 * t)

            vy0 = v0 * math.sin(math.radians(ang))
            vx0 = v0 * math.cos(math.radians(ang))

            tMax = t * 10 / 2
            yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))  # if(t<2):
            # vector(screen, blue, x, y, ang)

            t += dt

            if (y > (height - f)):
                y = height - f

                lock1 = False
                second = True
                lock = False

        if (cont == 3 and lock):
            printos(screen,
                    "3)Simulación: Alcanzar objetivo del problema utilizando el siguiente de los ángulos posibles",
                    200, 250, (67, 97, 241), font)
            v0 = 72
            ang = 75.9
            f = 62

            y = ((height - f) - vy0 * t + .5 * a * (t ** 2))
            x = (210 + vx0 * t)

            vy0 = v0 * math.sin(math.radians(ang))

            vx0 = v0 * math.cos(math.radians(ang))
            tMax = t * 10 / 2
            yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))

            # if(t<2):
            # vector(screen, blue, x, y, ang)

            t += dt

            if (y > (height - f)):
                y = height - f
                lock1 = False
                second = True
                lock = False
                cont = 0
        if (second):
            printos(screen, "Continuar? Y/N", 10, 200, blue, font)
            if (teclado[pygame.K_y]):
                lock = True
                second = False
                x = 210
                cont += 1
                t = 0
            elif (teclado[pygame.K_n]):
                df = 0
                hello()

        tabla()
        printos(screen, "Desplazamineto en X = %d m" % ((x - 210) * 100), 10, 10, black, font)
        printos(screen, "Desplazamiento en Y = %d m" % ((height - f - y) * 100), 10, 31, black, font)
        printos(screen, "θ = %d grados" % (ang), 10, 51, black, font)
        printos(screen, "Velocidad inicial = %d m/s" % (v0 * 10), 10, 71, black, font)
        printos(screen, "Vx = %d m/s" % (vx0 * 10), 10, 91, black, font)
        printos(screen, "Vy = %d m/s" % (vy0 * 10), 10, 111, black, font)
        printos(screen, "t = %d s" % (t * 10), 10, 131, black, font)
        printos(screen, "Altura máxima = %d m" % (yMax), 10, 151, black, font)

        clock.tick(40)
        pygame.draw.circle(screen, blue, (int(x), int(y)), radio)
        vector(screen, blue, x, y, ang)
        pygame.display.flip()


while (df==0):
       screen.fill(background)

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               exit()
       teclado = pygame.key.get_pressed()
       printos(screen, "1) Simulacion libre", 30, 60, black, font)
       printos(screen, "2) Simulacion de caso", 30, 90, black, font)
       printos(screen, "3) Salir", 30, 120, black, font)
       if (teclado[pygame.K_1]):
           df = 1
       if (teclado[pygame.K_3]):
           df=0
           break
       elif (teclado[pygame.K_2]):
           df = 2
       pygame.display.flip()
       clock.tick(40)
while df==1:


    screen.fill(background)
    screen.blit(imagenDora, (10, 630))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    teclado = pygame.key.get_pressed()
    if (tuple(set(teclado)) == (0, 1) and lock):
        if (teclado[pygame.K_UP]):
            ang += 1
            if (ang >= 90):
                ang = 90
        if (teclado[pygame.K_DOWN]):
            ang -= 1
            if (ang < 0):
                ang = 0
        if (teclado[pygame.K_RIGHT] and v0 < 100):
            v0 += 1
        if (teclado[pygame.K_LEFT] and v0 > 1):
            v0 -= 1
        if (teclado[pygame.K_SPACE]):
            lock = False
            lock1 = True
            vy0 = v0 * math.sin(math.radians(ang))
    if (teclado[pygame.K_ESCAPE]):
        break
    vx0 = v0 * math.cos(math.radians(ang))
    vy0 =  v0 * math.sin(math.radians(ang))
    if (lock1):
        y = (height - f) - vy0 * t + .5 * a * (t ** 2)
        x = 210 + vx0 * t
        t += dt

        if (y > (height - f)):
            y = height - f

            lock1 = False
            second = True
            lock = False
    tMax = t*10 / 2

    yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))
    if (second):
        printos(screen, "Continuar usando el simulador? Y/N", 10, 200, blue, font)
        if (teclado[pygame.K_y]):
            lock = True
            second = False
            hello()
            df=0
            f = 62
            x = 210
        elif (teclado[pygame.K_n]):
            break
    tabla()
    printos(screen, "Desplazamineto en X = %d m" % ((x - 210) * 100), 10, 10, black, font)
    printos(screen, "Desplazamiento en Y = %d m" % ((height - f - y) * 100), 10, 31, black, font)
    printos(screen, "θ = %d grados" % (ang), 10, 51, black, font)
    printos(screen, "Velocidad inicial = %d m/s" % (v0 * 10), 10, 71, black, font)
    printos(screen, "Vx = %d m/s" % (vx0 * 10), 10, 91, black, font)
    printos(screen, "Vy = %d m/s" % (vy0 * 10), 10, 111, black, font)
    printos(screen, "t = %d s" % (t * 10), 10, 131, black, font)
    printos(screen, "Altura máxima = %d m" % (yMax), 10, 151, black, font)

    pygame.draw.circle(screen, blue, (int(x), int(y)), radio)
    vector(screen, blue, x, y, ang)

    pygame.display.flip()
    clock.tick(50)
while (df == 2):
     dt=0.2
     screen.fill(background)
     screen.blit(imagenDora, (10, 630))
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
     teclado = pygame.key.get_pressed()

     if (cont == 1 and lock):
            printos(screen, "1) Simulación: Desplazamiento maximo en X utilizando θ = 45°", 300, 250, (67,97,241), font)

            v0 = 72
            f = 62
            ang = 45
            vy0 = v0 * math.sin(math.radians(ang))
            vx0 = v0 * math.cos(math.radians(ang))
            y = ((height - f) - vy0 * t + .5 * a * (t ** 2))
            x = (210 + vx0 * t)
            radio=10
            tMax = t * 10 / 2
            yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))

            if (t < 2):
                vector(screen, blue, x, y, ang)

            t += dt
            if (lock1):
                y = (height - f) - vy0 * t + .5 * a * (t ** 2)
                x = 210 + vx0 * t
                t += dt

                if (y > (height - f)):
                    y = height - f

                    lock1 = False
                    second = True
                    lock = False


            if (y > (height - f)):
                y = height - f
                lock1 = False
                second = True
                lock = False

     if (cont == 2 and lock):
         printos(screen, "2)Simulación: Alcanzar objetivo del problema utilizando uno de los ángulos posibles",250, 250, (67,97,241), font)
         v0 = 72
         ang = 14.1
         f=62

         y = ((height - f) - vy0 * t + .5 * a * (t ** 2))
         x = (210 + vx0 * t)

         vy0 = v0 * math.sin(math.radians(ang))
         vx0 = v0 * math.cos(math.radians(ang))

         tMax = t * 10 / 2
         yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))         # if(t<2):
         # vector(screen, blue, x, y, ang)

         t += dt

         if (y > (height - f)):
             y = height - f

             lock1 = False
             second = True
             lock = False

     if (cont == 3 and lock):
         printos(screen,
                 "3)Simulación: Alcanzar objetivo del problema utilizando el siguiente de los ángulos posibles",
                 200, 250, (67,97,241), font)
         v0 = 72
         ang = 75.9
         f=62

         y = ((height - f) - vy0 * t + .5 * a * (t ** 2))
         x = (210 + vx0 * t)

         vy0 = v0 * math.sin(math.radians(ang))

         vx0 = v0 * math.cos(math.radians(ang))
         tMax = t * 10 / 2
         yMax = ((height - radio) + (vy0 * 10 * tMax) - (a / 2 * (tMax ** 2)))


         # if(t<2):
         # vector(screen, blue, x, y, ang)

         t += dt

         if (y > (height - f)):
             y = height - f
             lock1 = False
             second = True
             lock = False
             cont = 0
     if (second):
         printos(screen, "Continuar? Y/N", 10, 200, blue, font)
         if (teclado[pygame.K_y]):
             lock = True
             second = False
             x = 210
             cont += 1
             t = 0
         elif (teclado[pygame.K_n]):
             df=0
             hello()

     tabla()
     printos(screen, "Desplazamineto en X = %d m" % ((x - 210) * 100), 10, 10, black, font)
     printos(screen, "Desplazamiento en Y = %d m" % ((height - f - y) * 100), 10, 31, black, font)
     printos(screen, "θ = %d grados" % (ang), 10, 51, black, font)
     printos(screen, "Velocidad inicial = %d m/s" % (v0 * 10), 10, 71, black, font)
     printos(screen, "Vx = %d m/s" % (vx0 * 10), 10, 91, black, font)
     printos(screen, "Vy = %d m/s" % (vy0 * 10), 10, 111, black, font)
     printos(screen, "t = %d s" % (t * 10), 10, 131, black, font)
     printos(screen, "Altura máxima = %d m" % (yMax), 10, 151, black, font)

     clock.tick(40)
     pygame.draw.circle(screen, blue, (int(x), int(y)), radio)
     vector(screen, blue, x, y, ang)
     pygame.display.flip()

