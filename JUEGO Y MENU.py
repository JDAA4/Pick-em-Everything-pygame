import random
import pygame
import sys
import button

from pygame.locals import *


class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0,255,100))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 50 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 120
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 20.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:

    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones, creditos):
        
        resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
        quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
        video_img = pygame.image.load('images/button_video.png').convert_alpha()
        audio_img = pygame.image.load('images/button_audio1.png').convert_alpha()
        keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
        back_img = pygame.image.load('images/button_back.png').convert_alpha()


        resume_button = button.Button(304, 300, resume_img, 1)
        quit_button = button.Button(336, 490, quit_img, 1)
        video_button = button.Button(226, 75, video_img, 1)
        audio_button = button.Button(225, 200, audio_img, 1)
        keys_button = button.Button(246, 325, keys_img, 1)
        back_button = button.Button(332, 450, back_img, 1)

        self.opciones = []
        fuente = pygame.font.Font('Comic Kings.otf', 30)
        x = -10
        y = 1000
        paridad = 1000

        self.cursor = Cursor(x +100, y, 51)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 50
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)





def enter():

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("PICK EM' EVERITHING")

    menuBg = pygame.image.load("images/escena.jpg").convert_alpha()


    ################## Menu
    play_img = pygame.image.load("images/button_jugar.png").convert_alpha()
    play_button = button.Button(300, 300, play_img, 1)

    credits_img = pygame.image.load("images/button_credits.png").convert_alpha()
    credits_button = button.Button(30, 400, credits_img, 1)

    settings_img = pygame.image.load('images/button_optionsesp.png')
    settings_button = button.Button(30, 500, settings_img,1)

    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    quit_button = button.Button(630, 500, quit_img, 1)

    ################## Back
    back_img = pygame.image.load('images/button_back.png').convert_alpha()
    back_button = button.Button(332, 470, back_img, 1)

    ################## Ajustes
    audio_img = pygame.image.load("images/button_audio1.png").convert_alpha()
    audio_button = button.Button(225, 200, audio_img, 1)
    video_img = pygame.image.load('images/lenguague.png').convert_alpha()
    video_button = button.Button(226, 75, video_img, 1)

    def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      screen.blit(menuBg, (0, 0))






    run = True
    while run:

      screen.blit(menuBg, (0, 0))

      #check if game is paused
      menu_state = "enter"

        #check if the options menu is open
      if menu_state == "enter":

          #draw the different options buttons

        if play_button.draw(screen):
            SCREEN_WIDTH = 400
            SCREEN_HEIGHT = 150

            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            pygame.display.set_caption("PICK EM' EVERITHING")

            #FONDO
            menuBg = pygame.image.load("images/menunivelesesp.jpg").convert_alpha()


            menu_game = False
            game_play = False
            game_paused = False
            menu_state = "main"


            level1_img = pygame.image.load('images/button_nivel1.png').convert_alpha()
            level2_img = pygame.image.load('images/button_nivel2.png').convert_alpha()
            level3_img = pygame.image.load("images/button_nivel3.png").convert_alpha()
            back_img = pygame.image.load('images/button_back.png').convert_alpha()

            level1_button = button.Button(50, 50, level1_img, 1)
            level2_button = button.Button(50, 195, level2_img, 1)
            level3_button = button.Button(50, 340, level3_img, 1)
            back_button = button.Button(340, 510, back_img, 1)

            def draw_text(text, font, text_col, x, y):
                img = font.render(text, True, text_col)
                screen.blit(menuBg, (0, 0))


            run = True
            while run:
              screen.blit(menuBg, (0, 0))

              #CAMBIA A OPCIONES
              menu_state = "options"

                #COMPRUEBA QUE ESTES EN OPCIONES
              if menu_state == "options":
                  #BOTONES
                if level1_button.draw(screen):
                    SCREEN_WIDTH = 800
                    SCREEN_HEIGHT = 600

                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                    pygame.display.set_caption("PICK EM' EVERITHING")

                    #FONDO
                    menuBg = pygame.image.load("images/controles.jpg").convert_alpha()


                    menu_game = False
                    game_play = False
                    game_paused = False
                    menu_state = "main"
                        

                    def draw_text(text, font, text_col, x, y):
                      img = font.render(text, True, text_col)
                      screen.blit(menuBg, (0, 0))



                    #Loop Juegp
                    menu_niveles = True
                    while menu_niveles:
                      screen.blit(menuBg, (0, 0))

                      #CAMBIA A OPCIONES
                      menu_state = "options"


                      #event handler
                      for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                          if event.key == pygame.K_SPACE:
                            from clases.clases_mapa import cargar_mapa
                            from clases.imagenes_objetos import clock,fondo,tierra_image,tierra_pasto_image,tierra_1_image,picos_image,sol_image,barrera,player_image,pantalla_muerte,reloj_img,camion_img,pantalla_victoria
                            from clases.clases_player import scrolling,move,salto,player_movimiento,cargar_animacion,poner_animacion
                            from clases.clases_objetos import objetos,obj_clase
                            from  clases.imagenes_objetos import objetos_index1,reciclaje_bote_img
                            pygame.display.set_caption('PICK EM´ EVERITHING') # Nombre de la ventana
                            display = pygame.Surface((300, 200))
                            W,H=1200,700
                            WINDOW_SIZE = (1200,700) # Tamaño de la ventana
                            screen = pygame.display.set_mode((W,H)) 

                            movimiento_fondo=0
                            moving_right = False
                            moving_left = False
                            muerte=False
                            victoria=False

                            cont_camion=0
                            cont_picos=0
                            cont_objeto1=0
                            cont_objeto2=0
                            cont_objeto3=0
                            cont_objeto4=0
                            cont_objeto5=0
                            cont=0

                            bff_cont_objetos1=1
                            bff_cont_objetos2=2
                            bff_cont_objetos3=3
                            bff_cont_objetos4=4
                            bff_cont_objetos5=5

                            player_img={}
                            player_img_id={}

                            player_accion = 'idle'
                            player_frame = 0
                            player_flip = False
                            animacion_frames={}
                            animacion_database = {}

                            animacion_database['caminar'],animacion_frames = cargar_animacion('animaciones/caminar',[7,7],animacion_frames)
                            animacion_database['idle'],animacion_frames = cargar_animacion('animaciones/idle',[7,7,40],animacion_frames)

                            mapa_juego1=cargar_mapa("mapas/mapa1")

                            #temporizador
                            timer, text = 120,'3'.rjust(3)
                            pygame.time.set_timer(pygame.USEREVENT,1000)
                            font = pygame.font.SysFont("DAYTONA",56)
                            font2=pygame.font.SysFont("DAYTONA",35)
                            timer_final =300

                            lista_objetos1=[]
                            lista_objetos2=[]
                            lista_objetos3=[]
                            lista_objetos4=[]
                            lista_objetos5=[]
                            lista_picos=[]
                            lista_camion=[]

                            def poner_mapa(mapa,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion):
                                TILE_SIZE=16
                                tile_rects = []
                                y = 0
                                for fila in mapa:
                                    x = 0
                                    for tile in fila:
                                        if tile == '1':
                                            display.blit(tierra_pasto_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                        if tile == '2':
                                            display.blit(tierra_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                        if tile == '3':
                                            display.blit(tierra_1_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                        if tile=="4":
                                            display.blit(picos_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if cont_picos<41:    
                                                lista_picos.append(objetos((x*TILE_SIZE+10,y*TILE_SIZE-1)))
                                                cont_picos +=1
                                        if tile=="5":
                                            display.blit(barrera, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
                                        if tile=="+":
                                            if cont_objeto1<2:
                                                lista_objetos1.append(objetos((x*TILE_SIZE,y*TILE_SIZE+5)))
                                                cont_objeto1 +=1
                                        if tile=="*":
                                            if cont_objeto2<2:
                                                lista_objetos2.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                cont_objeto2 +=1
                                        if tile=="@":
                                            if cont_objeto3<2:
                                                lista_objetos3.append(objetos((x*TILE_SIZE,y*TILE_SIZE+3)))
                                                cont_objeto3 +=1
                                        if tile=="#":
                                            if cont_objeto4<2:
                                                lista_objetos4.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                cont_objeto4 +=1
                                        if tile=="&":
                                            if cont_objeto5<2:
                                                lista_objetos5.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                cont_objeto5 +=1
                                        if tile=="$":
                                            display.blit(camion_img,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]-15))
                                            lista_camion.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))  
                                        if tile == '1':
                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                        if tile == '2':
                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                        if tile == '3':
                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                        if tile == '4':
                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                        if tile == '5':
                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                        
                                        x += 1
                                    y += 1
                                return tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion
                                
                            def movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum):
                                if event.type == KEYDOWN:
                                        if event.key == K_RIGHT:
                                            moving_right = True
                                        if event.key == K_LEFT:
                                            moving_left = True
                                        if event.key == K_UP:
                                            if air_timer < 4:
                                                player_y_momentum = -5
                                if event.type == KEYUP:
                                        if event.key == K_RIGHT:
                                            moving_right = False
                                        if event.key == K_LEFT:
                                            moving_left = False
                                return moving_right,moving_left,player_y_momentum

                            def fondo_mivimiento(scroll):
                                 x_relativa = (scroll[0]/20) % fondo.get_rect().width
                                 display.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
                                 if x_relativa < W:
                                     display.blit(fondo, (x_relativa, 0))
                                 
                                 
                            player_y_momentum = 0
                            air_timer = 0

                            player_rect = pygame.Rect(250, 180, player_image.get_width(), player_image.get_height())
                            n1=True
                            while n1: # Bucle del juego
                                if muerte:
                                    display.blit(pantalla_muerte,(0,0))
                                    back_button = button.Button(600, 550, back_img, 1)

                                    if back_button.draw(screen):
                                        screen=pygame.display.set_mode((800,600))
                                        return Menu


                                      #even handler
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                          if event.key == pygame.K_SPACE:
                                            game_paused = False
                                        if event.type == pygame.QUIT:
                                          run = False

                                    pygame.display.update()
                                    

                                    if timer_final<0:
                                        display.blit(pantalla_muerte,(0,0))
                                        back_button = button.Button(600, 550, back_img, 1)

                                        if back_button.draw(screen):
                                            screen=pygame.display.set_mode((800,600))
                                            return Menu


                                          #even handler
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                              if event.key == pygame.K_SPACE:
                                                game_paused = False
                                            if event.type == pygame.QUIT:
                                              run = False
                                              
                                        pygame.display.update()


                                elif victoria:
                                    if cont<6:
                                        display.blit(pantalla_muerte,(0,0))
                                        display.blit(font2.render(str(cont),True,(255,255,255)),(140,155))
                                        if timer_final<0:
                                            display.blit(pantalla_muerte,(0,0))
                                            back_button = button.Button(600, 550, back_img, 1)

                                            if back_button.draw(screen):
                                                screen=pygame.display.set_mode((800,600))
                                                return Menu


                                              #even handler
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                  if event.key == pygame.K_SPACE:
                                                    game_paused = False
                                                if event.type == pygame.QUIT:
                                                  run = False
                                                  
                                            pygame.display.update()
                                    else:
                                        timer_final -=1
                                        display.blit(pantalla_victoria,(0,0))
                                        display.blit(font2.render(str(cont),True,(255,255,255)),(226,110))
                                        back_button = button.Button(100, 550, back_img, 1)

                                        if back_button.draw(screen):
                                            screen=pygame.display.set_mode((800,600))
                                            return Menu


                                          #even handler
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                              if event.key == pygame.K_SPACE:
                                                game_paused = False
                                            if event.type == pygame.QUIT:
                                              run = False
                                              
                                        pygame.display.update()

                                        if timer_final<0:
                                            display.blit(pantalla_muerte,(0,0))
                                            back_button = button.Button(600, 550, back_img, 1)

                                            if back_button.draw(screen):
                                                screen=pygame.display.set_mode((800,600))
                                                return Menu


                                              #even handler
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                  if event.key == pygame.K_SPACE:
                                                    game_paused = False
                                                if event.type == pygame.QUIT:
                                                  run = False
                                                  
                                            pygame.display.update()
                                else:
                                    scroll=scrolling(player_rect)
                                    fondo_mivimiento(scroll)
                                    tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion=poner_mapa(mapa_juego1,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion)
                                    player_movement,player_y_momentum=player_movimiento(moving_right,moving_left,player_y_momentum)
                                    player_rect, collisions = move(player_rect, player_movement, tile_rects)
                                    air_timer,player_y_momentum=salto(collisions,air_timer,player_y_momentum)
                                    player_flip,player_frame,player_accion,player_img_id,player_img=poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img)
                                    cont,lista_objetos1=obj_clase(lista_objetos1,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos1)
                                    cont,lista_objetos2=obj_clase(lista_objetos2,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos2)
                                    cont,lista_objetos3=obj_clase(lista_objetos3,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos3)
                                    cont,lista_objetos4=obj_clase(lista_objetos4,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos4)
                                    cont,lista_objetos5=obj_clase(lista_objetos5,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos5)
                                    for picos in lista_picos:
                                        if picos.colision_test(player_rect):
                                            muerte=True
                                    for camion in lista_camion:
                                        if camion.colision_test(player_rect):
                                            victoria=True
                                    display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
                                    display.blit(sol_image,(265,5))
                                    display.blit(reciclaje_bote_img,(220,0))
                                    display.blit(reloj_img,(5,5))
                                for event in pygame.event.get():
                                    if event.type==QUIT:
                                     pygame.quit()
                                     sys.exit()
                                    if event.type == pygame.USEREVENT:
                                        timer -=1
                                        text = str(timer).rjust(3)
                                    if timer <0:
                                        muerte=True
                                    moving_right,moving_left,player_y_momentum=movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum)
                                  
                                surf = pygame.transform.scale(display, WINDOW_SIZE)
                                screen.blit(surf, (0, 0))
                                if timer>0:
                                    if victoria==False:
                                        if muerte==False:
                                            screen.blit(font.render(str(timer),True,(0,0,0)),(120,45))
                                            screen.blit(font.render(str(cont),True,(0,0,0)),(980,30))
                                            screen.blit(font.render(str("/10"),True,(0,0,0)),(1020,30))
                                pygame.display.update() # actualizamos nuestra pantalla
                                clock.tick(60) # Ponemos el juego a 60 fps

                        if event.type == pygame.QUIT:
                          run = False

                      pygame.display.update()

                    #pygame.quit()

                if level2_button.draw(screen):
                    SCREEN_WIDTH = 800
                    SCREEN_HEIGHT = 600

                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                    pygame.display.set_caption("PICK EM' EVERITHING")

                    #FONDO
                    menuBg = pygame.image.load("images/controls.jpg").convert_alpha()


                    menu_game = False
                    game_play = False
                    game_paused = False
                    menu_state = "main"
                        

                    def draw_text(text, font, text_col, x, y):
                      img = font.render(text, True, text_col)
                      screen.blit(menuBg, (0, 0))



                    #Loop Juegp
                    menu_niveles = True
                    while menu_niveles:
                      screen.blit(menuBg, (0, 0))

                      #CAMBIA A OPCIONES
                      menu_state = "options"


                      #event handler
                      for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                from clases.clases_mapa import cargar_mapa
                                from clases.imagenes_objetos import clock,fondo2,picos_image,sol_image,barrera,player_image,pantalla_muerte,reloj_img,camion_img,pantalla_victoria,ladrillo_image2,ladrillo_image4,ladrillo_image3,objetos_index2,reciclaje_bote_img,ladrillo_image1
                                from clases.clases_player import scrolling,move,salto,player_movimiento,cargar_animacion,poner_animacion
                                from clases.clases_objetos import objetos,obj_clase

                                pygame.init() # inicializamos pygame
                                pygame.display.set_caption('Pick Em All') # Nombre de la ventana
                                display = pygame.Surface((300, 200))
                                W,H=1200,700
                                WINDOW_SIZE = (1200,700) # Tamaño de la ventana
                                screen = pygame.display.set_mode((W,H)) 

                                movimiento_fondo=0
                                moving_right = False
                                moving_left = False
                                muerte=False
                                victoria=False

                                cont_camion=0
                                cont_picos=0
                                cont_objeto1=0
                                cont_objeto2=0
                                cont_objeto3=0
                                cont_objeto4=0
                                cont=0

                                bff_cont_objetos1=1
                                bff_cont_objetos2=2
                                bff_cont_objetos3=3
                                bff_cont_objetos4=4

                                player_img={}
                                player_img_id={}

                                player_accion = 'idle'
                                player_frame = 0
                                player_flip = False
                                animacion_frames={}
                                animacion_database = {}

                                animacion_database['caminar'],animacion_frames = cargar_animacion('animaciones/caminar',[7,7],animacion_frames)
                                animacion_database['idle'],animacion_frames = cargar_animacion('animaciones/idle',[7,7,40],animacion_frames)

                                mapa_juego1=cargar_mapa("mapas/mapa2")

                                #temporizador
                                timer, text = 120,'3'.rjust(3)
                                pygame.time.set_timer(pygame.USEREVENT,1000)
                                font = pygame.font.SysFont("DAYTONA",56)
                                font2=pygame.font.SysFont("DAYTONA",35)
                                timer_final =300

                                lista_objetos1=[]
                                lista_objetos2=[]
                                lista_objetos3=[]
                                lista_objetos4=[]
                                lista_picos=[]
                                lista_camion=[]

                                def poner_mapa(mapa,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion):
                                    TILE_SIZE=16
                                    tile_rects = []
                                    y = 0
                                    for fila in mapa:
                                        x = 0
                                        for tile in fila:
                                            if tile == '1':
                                                display.blit(ladrillo_image3, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if tile == '2':
                                                display.blit(ladrillo_image2, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if tile == '3':
                                                display.blit(ladrillo_image1, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if tile=="4":
                                                display.blit(picos_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                if cont_picos<64:    
                                                    lista_picos.append(objetos((x*TILE_SIZE+10,y*TILE_SIZE-1)))
                                                    cont_picos +=1
                                            if tile=="5":
                                                display.blit(barrera, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
                                            if tile=="6":
                                                display.blit(ladrillo_image4,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]))
                                            if tile=="+":
                                                if cont_objeto1<2:
                                                    lista_objetos1.append(objetos((x*TILE_SIZE,y*TILE_SIZE+5)))
                                                    cont_objeto1 +=1
                                            if tile=="*":
                                                if cont_objeto2<3:
                                                    lista_objetos2.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                    cont_objeto2 +=1
                                            if tile=="@":
                                                if cont_objeto3<2:
                                                    lista_objetos3.append(objetos((x*TILE_SIZE,y*TILE_SIZE+3)))
                                                    cont_objeto3 +=1
                                            if tile=="#":
                                                if cont_objeto4<3:
                                                    lista_objetos4.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                    cont_objeto4 +=1
                                            if tile=="$":
                                                display.blit(camion_img,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]-15))
                                                lista_camion.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))  
                                            if tile == '1':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '2':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '3':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '4':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '5':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile=="6":
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            
                                            x += 1
                                        y += 1
                                    return tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion
                                    
                                def movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum):
                                    if event.type == KEYDOWN:
                                            if event.key == K_RIGHT:
                                                moving_right = True
                                            if event.key == K_LEFT:
                                                moving_left = True
                                            if event.key == K_UP:
                                                if air_timer < 4:
                                                    player_y_momentum = -5
                                    if event.type == KEYUP:
                                            if event.key == K_RIGHT:
                                                moving_right = False
                                            if event.key == K_LEFT:
                                                moving_left = False
                                    return moving_right,moving_left,player_y_momentum

                                def fondo_mivimiento(scroll):
                                     x_relativa = (scroll[0]/20) % fondo2.get_rect().width
                                     display.blit(fondo2, (x_relativa - fondo2.get_rect().width, 0))
                                     if x_relativa < W:
                                         display.blit(fondo2, (x_relativa, 0))
                                     
                                player_y_momentum = 0
                                air_timer = 0

                                player_rect = pygame.Rect(280, 180, player_image.get_width(), player_image.get_height())

                                while True: # Bucle del juego
                                    if muerte:
                                        display.blit(pantalla_muerte,(0,0))
                                        back_button = button.Button(600, 550, back_img, 1)

                                        if back_button.draw(screen):
                                            screen=pygame.display.set_mode((800,600))
                                            return Menu


                                          #even handler
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                              if event.key == pygame.K_SPACE:
                                                game_paused = False
                                            if event.type == pygame.QUIT:
                                              run = False

                                        pygame.display.update()


                                          #even handler
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                              if event.key == pygame.K_SPACE:
                                                game_paused = False
                                            if event.type == pygame.QUIT:
                                              run = FalseZ
                                        pygame.display.update()

                                    elif victoria:
                                        if cont<6:
                                            timer_final -=1
                                            display.blit(pantalla_muerte,(0,0))
                                            display.blit(font2.render(str(cont),True,(255,255,255)),(140,155))
                                            if timer_final<0:
                                                pygame.quit()
                                                sys.exit()
                                        else:
                                            timer_final -=1
                                            display.blit(pantalla_victoria,(0,0))
                                            display.blit(font2.render(str(cont),True,(255,255,255)),(226,110))
                                            if timer_final<0:
                                                pygame.quit()
                                                sys.exit()
                                    else:
                                        scroll=scrolling(player_rect)
                                        fondo_mivimiento(scroll)
                                        tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion=poner_mapa(mapa_juego1,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion)
                                        player_movement,player_y_momentum=player_movimiento(moving_right,moving_left,player_y_momentum)
                                        player_rect, collisions = move(player_rect, player_movement, tile_rects)
                                        air_timer,player_y_momentum=salto(collisions,air_timer,player_y_momentum)
                                        player_flip,player_frame,player_accion,player_img_id,player_img=poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img)
                                        cont,lista_objetos1=obj_clase(lista_objetos1,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos1)
                                        cont,lista_objetos2=obj_clase(lista_objetos2,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos2)
                                        cont,lista_objetos3=obj_clase(lista_objetos3,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos3)
                                        cont,lista_objetos4=obj_clase(lista_objetos4,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos4)
                                        for picos in lista_picos:
                                            if picos.colision_test(player_rect):
                                                muerte=True
                                        for camion in lista_camion:
                                            if camion.colision_test(player_rect):
                                                victoria=True
                                        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
                                        display.blit(sol_image,(265,5))
                                        display.blit(reciclaje_bote_img,(220,0))
                                        display.blit(reloj_img,(5,5))
                                    for event in pygame.event.get():
                                        if event.type==QUIT:
                                         pygame.quit()
                                         sys.exit()
                                        if event.type == pygame.USEREVENT:
                                            timer -=1
                                            text = str(timer).rjust(3)
                                        if timer <0:
                                            muerte=True
                                        moving_right,moving_left,player_y_momentum=movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum)
                                      
                                    surf = pygame.transform.scale(display, WINDOW_SIZE)
                                    screen.blit(surf, (0, 0))
                                    if timer>0:
                                        if victoria==False:
                                            if muerte==False:
                                                screen.blit(font.render(str(timer),True,(0,0,0)),(120,45))
                                                screen.blit(font.render(str(cont),True,(0,0,0)),(980,30))
                                                screen.blit(font.render(str("/10"),True,(0,0,0)),(1020,30))
                                    pygame.display.update() # actualizamos nuestra pantalla
                                    clock.tick(60) # Ponemos el juego a 60 fps

                        if event.type == pygame.QUIT:
                           run = False

                        pygame.display.update()

                        
                if level3_button.draw(screen):

                    SCREEN_WIDTH = 800
                    SCREEN_HEIGHT = 600

                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                    pygame.display.set_caption("PICK EM' EVERITHING")

                    #FONDO
                    menuBg = pygame.image.load("images/controls.jpg").convert_alpha()


                    menu_game = False
                    game_play = False
                    game_paused = False
                    menu_state = "main"
                        

                    def draw_text(text, font, text_col, x, y):
                      img = font.render(text, True, text_col)
                      screen.blit(menuBg, (0, 0))



                    #Loop Juegp
                    menu_niveles = True
                    while menu_niveles:
                      screen.blit(menuBg, (0, 0))

                      #CAMBIA A OPCIONES
                      menu_state = "options"


                      #event handler
                      for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                from clases.clases_mapa import cargar_mapa
                                from clases.imagenes_objetos import clock,fondo,tierra_image,tierra_pasto_image,tierra_1_image,picos_image,sol_image,barrera,player_image,pantalla_muerte,reloj_img,camion_img,pantalla_victoria
                                from clases.clases_player import scrolling,move,salto,player_movimiento,cargar_animacion,poner_animacion
                                from clases.clases_objetos import objetos,obj_clase
                                from  clases.imagenes_objetos import objetos_index1,reciclaje_bote_img

                                pygame.display.set_caption('Pick Em All') # Nombre de la ventana
                                display = pygame.Surface((300, 200))
                                W,H=1200,700
                                WINDOW_SIZE = (1200,700) # Tamaño de la ventana
                                screen = pygame.display.set_mode((W,H)) 

                                movimiento_fondo=0
                                moving_right = False
                                moving_left = False
                                muerte=False
                                victoria=False

                                cont_camion=0
                                cont_picos=0
                                cont_objeto1=0
                                cont_objeto2=0
                                cont_objeto3=0
                                cont_objeto4=0
                                cont_objeto5=0
                                cont=0

                                bff_cont_objetos1=1
                                bff_cont_objetos2=2
                                bff_cont_objetos3=3
                                bff_cont_objetos4=4
                                bff_cont_objetos5=5

                                player_img={}
                                player_img_id={}

                                player_accion = 'idle'
                                player_frame = 0
                                player_flip = False
                                animacion_frames={}
                                animacion_database = {}

                                animacion_database['caminar'],animacion_frames = cargar_animacion('animaciones/caminar',[7,7],animacion_frames)
                                animacion_database['idle'],animacion_frames = cargar_animacion('animaciones/idle',[7,7,40],animacion_frames)

                                mapa_juego1=cargar_mapa("mapas/mapa3")

                                #temporizador
                                timer, text = 120,'3'.rjust(3)
                                pygame.time.set_timer(pygame.USEREVENT,1000)
                                font = pygame.font.SysFont("DAYTONA",56)
                                font2=pygame.font.SysFont("DAYTONA",35)
                                timer_final =300

                                lista_objetos1=[]
                                lista_objetos2=[]
                                lista_objetos3=[]
                                lista_objetos4=[]
                                lista_objetos5=[]
                                lista_picos=[]
                                lista_camion=[]

                                def poner_mapa(mapa,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion):
                                    TILE_SIZE=16
                                    tile_rects = []
                                    y = 0
                                    for fila in mapa:
                                        x = 0
                                        for tile in fila:
                                            if tile == '1':
                                                display.blit(tierra_pasto_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if tile == '2':
                                                display.blit(tierra_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if tile == '3':
                                                display.blit(tierra_1_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                            if tile=="4":
                                                display.blit(picos_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                if cont_picos<141:    
                                                    lista_picos.append(objetos((x*TILE_SIZE+10,y*TILE_SIZE-1)))
                                                    cont_picos +=1
                                            if tile=="5":
                                                display.blit(barrera, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
                                            if tile=="+":
                                                if cont_objeto1<3:
                                                    lista_objetos1.append(objetos((x*TILE_SIZE,y*TILE_SIZE+5)))
                                                    cont_objeto1 +=1
                                            if tile=="*":
                                                if cont_objeto2<2:
                                                    lista_objetos2.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                    cont_objeto2 +=1
                                            if tile=="@":
                                                if cont_objeto3<2:
                                                    lista_objetos3.append(objetos((x*TILE_SIZE,y*TILE_SIZE+3)))
                                                    cont_objeto3 +=1
                                            if tile=="#":
                                                if cont_objeto4<3:
                                                    lista_objetos4.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                    cont_objeto4 +=1
                                            if tile=="&":
                                                if cont_objeto5<2:
                                                    lista_objetos5.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                    cont_objeto5 +=1
                                            if tile=="$":
                                                display.blit(camion_img,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]-15))
                                                lista_camion.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))  
                                            if tile == '1':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '2':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '3':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '4':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            if tile == '5':
                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                            
                                            x += 1
                                        y += 1
                                    return tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion
                                    
                                def movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum):
                                    if event.type == KEYDOWN:
                                            if event.key == K_RIGHT:
                                                moving_right = True
                                            if event.key == K_LEFT:
                                                moving_left = True
                                            if event.key == K_UP:
                                                if air_timer < 4:
                                                    player_y_momentum = -5
                                    if event.type == KEYUP:
                                            if event.key == K_RIGHT:
                                                moving_right = False
                                            if event.key == K_LEFT:
                                                moving_left = False
                                    return moving_right,moving_left,player_y_momentum

                                def fondo_mivimiento(scroll):
                                     x_relativa = (scroll[0]/20) % fondo.get_rect().width
                                     display.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
                                     if x_relativa < W:
                                         display.blit(fondo, (x_relativa, 0))
                                     
                                player_y_momentum = 0
                                air_timer = 0

                                player_rect = pygame.Rect(250, 180, player_image.get_width(), player_image.get_height())

                                while True: # Bucle del juego
                                    if muerte:
                                        display.blit(pantalla_muerte,(0,0))
                                        back_button = button.Button(600, 550, back_img, 1)

                                        if back_button.draw(screen):
                                            screen=pygame.display.set_mode((800,600))
                                            return Menu


                                          #even handler
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                              if event.key == pygame.K_SPACE:
                                                game_paused = False
                                            if event.type == pygame.QUIT:
                                              run = False

                                        pygame.display.update()


                                          #even handler
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                              if event.key == pygame.K_SPACE:
                                                game_paused = False
                                            if event.type == pygame.QUIT:
                                              run = False

                                        pygame.display.update()

                                    elif victoria:
                                        if cont<10:
                                            timer_final -=1
                                            display.blit(pantalla_muerte,(0,0))
                                            display.blit(font2.render(str(cont),True,(255,255,255)),(140,155))
                                            if timer_final<0:
                                                pygame.quit()
                                                sys.exit()
                                        else:
                                            timer_final -=1
                                            display.blit(pantalla_victoria,(0,0))
                                            display.blit(font2.render(str(cont),True,(255,255,255)),(226,110))
                                            if timer_final<0:
                                                pygame.quit()
                                                sys.exit()
                                    else:
                                        scroll=scrolling(player_rect)
                                        fondo_mivimiento(scroll)
                                        tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion=poner_mapa(mapa_juego1,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion)
                                        player_movement,player_y_momentum=player_movimiento(moving_right,moving_left,player_y_momentum)
                                        player_rect, collisions = move(player_rect, player_movement, tile_rects)
                                        air_timer,player_y_momentum=salto(collisions,air_timer,player_y_momentum)
                                        player_flip,player_frame,player_accion,player_img_id,player_img=poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img)
                                        cont,lista_objetos1=obj_clase(lista_objetos1,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos1)
                                        cont,lista_objetos2=obj_clase(lista_objetos2,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos2)
                                        cont,lista_objetos3=obj_clase(lista_objetos3,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos3)
                                        cont,lista_objetos4=obj_clase(lista_objetos4,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos4)
                                        cont,lista_objetos5=obj_clase(lista_objetos5,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos5)
                                        for picos in lista_picos:
                                            if picos.colision_test(player_rect):
                                                muerte=True
                                        for camion in lista_camion:
                                            if camion.colision_test(player_rect):
                                                victoria=True
                                        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
                                        display.blit(sol_image,(265,5))
                                        display.blit(reciclaje_bote_img,(220,0))
                                        display.blit(reloj_img,(5,5))
                                    for event in pygame.event.get():
                                        if event.type==QUIT:
                                         pygame.quit()
                                         sys.exit()
                                        if event.type == pygame.USEREVENT:
                                            timer -=1
                                            text = str(timer).rjust(3)
                                        if timer <0:
                                            muerte=True
                                        moving_right,moving_left,player_y_momentum=movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum)
                                      
                                    surf = pygame.transform.scale(display, WINDOW_SIZE)
                                    screen.blit(surf, (0, 0))
                                    if timer>0:
                                        if victoria==False:
                                            if muerte==False:
                                                screen.blit(font.render(str(timer),True,(0,0,0)),(120,45))
                                                screen.blit(font.render(str(cont),True,(0,0,0)),(980,30))
                                                screen.blit(font.render(str("/12"),True,(0,0,0)),(1020,30))
                                    pygame.display.update() # actualizamos nuestra pantalla
                                    clock.tick(60) # Ponemos el juego a 60 fps

                        if event.type == pygame.QUIT:
                            run = False

                        pygame.display.update()

                    

                if back_button.draw(screen):
                    return "enter"
              else:
                draw_text("Press SPACE to pause", font, TEXT_COL, 10, 10)


              #event handler
              for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                    game_paused = False
                if event.type == pygame.QUIT:
                  run = False

              pygame.display.update()

            pygame.quit()


          #event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_paused = False
                    if event.type == pygame.QUIT:
                        run = False

                pygame.display.update()
                pygame.quit()

        if credits_button.draw(screen):
            SCREEN_WIDTH = 800
            SCREEN_HEIGHT = 600

            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            pygame.display.set_caption("PICK EM' EVERITHING")

            menuBg = pygame.image.load("creditos.jpg").convert_alpha()


            font = pygame.font.SysFont("cartoon.tff", 40)

            TEXT_COL = (255, 255, 255)
            

            back_img = pygame.image.load('images/button_back.png').convert_alpha()
            back_button = button.Button(332, 465, back_img, 1)


            def draw_text(text, font, text_col, x, y):
              img = font.render(text, True, text_col)
              screen.blit(menuBg, (0, 0))
            run = True
            while run:

              screen.blit(menuBg, (0, 0))

              #check if game is paused
              menu_state = "creditos"

                #check if the options menu is open
              if menu_state == "creditos":
                  #draw the different options buttons
                if back_button.draw(screen):
                    return Menu


              #event handler
              for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                    game_paused = False
                if event.type == pygame.QUIT:
                  run = False

              pygame.display.update()

            pygame.quit()


        if settings_button.draw(screen):
            SCREEN_WIDTH = 800
            SCREEN_HEIGHT = 600

            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            pygame.display.set_caption("PICK EM' EVERITHING")

            #FONDO
            menuBg = pygame.image.load("images/escena1.jpg").convert_alpha()
            menuBg1 = pygame.image.load("images/escena.jpg").convert_alpha()


            menu_game = False
            game_play = False
            game_paused = False
            menu_state = "main"


            video_img = pygame.image.load('images/lenguagueing.png').convert_alpha()
            back_img = pygame.image.load('images/button_back.png').convert_alpha()

            video_button = button.Button(226, 75, video_img, 1)
            audio_button = button.Button(225, 200, audio_img, 1)
            back_button = button.Button(332, 450, back_img, 1)
            

            audio_img = pygame.image.load("images/button_audioplay.png").convert_alpha()
            audio_button = button.Button(225, 200, audio_img, 1)
            audio1_img = pygame.image.load("images/button_audiopause.png").convert_alpha()
            audio1_button = button.Button(225, 325, audio1_img, 1)

            def draw_text(text, font, text_col, x, y):
                img = font.render(text, True, text_col)
                screen.blit(menuBg, (0, 0))
                
            volumen_bol=False
            run = True
            while run:
              screen.blit(menuBg, (0, 0))

              #CAMBIA A OPCIONES
              menu_state = "options"

                #COMPRUEBA QUE ESTES EN OPCIONES
              if menu_state == "options":
                  #BOTONES
                if audio_button.draw(screen):
                    pygame.mixer.music.play()

                if audio1_button.draw(screen):
                    pygame.mixer.music.pause()


                if video_button.draw(screen):
                    SCREEN_WIDTH = 800
                    SCREEN_HEIGHT = 600

                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                    pygame.display.set_caption("PICK EM' EVERITHING")

                    menuBg = pygame.image.load("images/escena.jpg").convert_alpha()


                    ################## Menu
                    play_img = pygame.image.load("images/button_play.png").convert_alpha()
                    play_button = button.Button(300, 300, play_img, 1)

                    credits_img = pygame.image.load("images/button_credits.png").convert_alpha()
                    credits_button = button.Button(30, 400, credits_img, 1)

                    settings_img = pygame.image.load('images/button_optionseng.png')
                    settings_button = button.Button(30, 500, settings_img,1)

                    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
                    quit_button = button.Button(630, 500, quit_img, 1)

                    ################## Back
                    back_img = pygame.image.load('images/button_back.png').convert_alpha()
                    back_button = button.Button(332, 470, back_img, 1)

                    ################## Ajustes
                    video_img = pygame.image.load('images/lenguague.png').convert_alpha()
                    video_button = button.Button(226, 75, video_img, 1)
                    audio_img = pygame.image.load("images/button_audioplay.png").convert_alpha()
                    audio_button = button.Button(225, 200, audio_img, 1)
                    audio1_img = pygame.image.load("images/button_audiopause.png").convert_alpha()
                    audio1_button = button.Button(225, 325, audio1_img, 1)

                    def draw_text(text, font, text_col, x, y):
                      img = font.render(text, True, text_col)
                      screen.blit(menuBg, (0, 0))


                    run1 = True
                    while run1:

                      screen.blit(menuBg, (0, 0))

                      #check if game is paused
                      menu_state = "enter"

                        #check if the options menu is open
                      if menu_state == "enter":

                          #draw the different options buttons

                        if play_button.draw(screen):
                            SCREEN_WIDTH = 800
                            SCREEN_HEIGHT = 600

                            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                            pygame.display.set_caption("PICK EM' EVERITHING")

                            #FONDO
                            menuBg = pygame.image.load("images/menunivelesing.jpg").convert_alpha()


                            menu_game = False
                            game_play = False
                            game_paused = False
                            menu_state = "main"


                            level1_img = pygame.image.load('images/button_level1.png').convert_alpha()
                            level2_img = pygame.image.load('images/button_level2.png').convert_alpha()
                            level3_img = pygame.image.load("images/button_level3.png").convert_alpha()
                            back_img = pygame.image.load('images/button_back.png').convert_alpha()

                            level1_button = button.Button(50, 50, level1_img, 1)
                            level2_button = button.Button(50, 195, level2_img, 1)
                            level3_button = button.Button(50, 340, level3_img, 1)
                            back_button = button.Button(340, 510, back_img, 1)

                            def draw_text(text, font, text_col, x, y):
                                img = font.render(text, True, text_col)
                                screen.blit(menuBg, (0, 0))


                            run1 = True
                            while run1:
                              screen.blit(menuBg, (0, 0))

                              #CAMBIA A OPCIONES
                              menu_state = "options"

                                #COMPRUEBA QUE ESTES EN OPCIONES
                              if menu_state == "options":
                                  


                                  #NIVELES
                                if level1_button.draw(screen):
                                    SCREEN_WIDTH = 800
                                    SCREEN_HEIGHT = 600

                                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                                    pygame.display.set_caption("PICK EM' EVERITHING")

                                    #FONDO
                                    menuBg = pygame.image.load("images/controls.jpg").convert_alpha()


                                    menu_game = False
                                    game_play = False
                                    game_paused = False
                                    menu_state = "main"
                                        

                                    def draw_text(text, font, text_col, x, y):
                                      img = font.render(text, True, text_col)
                                      screen.blit(menuBg, (0, 0))



                                    #Loop Juegp
                                    menu_niveles = True
                                    while menu_niveles:
                                      screen.blit(menuBg, (0, 0))

                                      #CAMBIA A OPCIONES
                                      menu_state = "options"


                                      #event handler
                                      for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                          if event.key == pygame.K_SPACE:
                                            from clases.clases_mapa import cargar_mapa
                                            from clases.imagenes_objetos import clock,fondo,tierra_image,tierra_pasto_image,tierra_1_image,picos_image,sol_image,barrera,player_image,pantalla_muerte,reloj_img,camion_img,pantalla_victoria
                                            from clases.clases_player import scrolling,move,salto,player_movimiento,cargar_animacion,poner_animacion
                                            from clases.clases_objetos import objetos,obj_clase
                                            from  clases.imagenes_objetos import objetos_index1,reciclaje_bote_img
                                            pygame.display.set_caption('PICK EM´ EVERITHING') # Nombre de la ventana
                                            display = pygame.Surface((300, 200))
                                            W,H=1200,700
                                            WINDOW_SIZE = (1200,700) # Tamaño de la ventana
                                            screen = pygame.display.set_mode((W,H)) 

                                            movimiento_fondo=0
                                            moving_right = False
                                            moving_left = False
                                            muerte=False
                                            victoria=False

                                            cont_camion=0
                                            cont_picos=0
                                            cont_objeto1=0
                                            cont_objeto2=0
                                            cont_objeto3=0
                                            cont_objeto4=0
                                            cont_objeto5=0
                                            cont=0

                                            bff_cont_objetos1=1
                                            bff_cont_objetos2=2
                                            bff_cont_objetos3=3
                                            bff_cont_objetos4=4
                                            bff_cont_objetos5=5

                                            player_img={}
                                            player_img_id={}

                                            player_accion = 'idle'
                                            player_frame = 0
                                            player_flip = False
                                            animacion_frames={}
                                            animacion_database = {}

                                            animacion_database['caminar'],animacion_frames = cargar_animacion('animaciones/caminar',[7,7],animacion_frames)
                                            animacion_database['idle'],animacion_frames = cargar_animacion('animaciones/idle',[7,7,40],animacion_frames)

                                            mapa_juego1=cargar_mapa("mapas/mapa1")

                                            #temporizador
                                            timer, text = 120,'3'.rjust(3)
                                            pygame.time.set_timer(pygame.USEREVENT,1000)
                                            font = pygame.font.SysFont("DAYTONA",56)
                                            font2=pygame.font.SysFont("DAYTONA",35)
                                            timer_final =300

                                            lista_objetos1=[]
                                            lista_objetos2=[]
                                            lista_objetos3=[]
                                            lista_objetos4=[]
                                            lista_objetos5=[]
                                            lista_picos=[]
                                            lista_camion=[]

                                            def poner_mapa(mapa,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion):
                                                TILE_SIZE=16
                                                tile_rects = []
                                                y = 0
                                                for fila in mapa:
                                                    x = 0
                                                    for tile in fila:
                                                        if tile == '1':
                                                            display.blit(tierra_pasto_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                        if tile == '2':
                                                            display.blit(tierra_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                        if tile == '3':
                                                            display.blit(tierra_1_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                        if tile=="4":
                                                            display.blit(picos_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if cont_picos<41:    
                                                                lista_picos.append(objetos((x*TILE_SIZE+10,y*TILE_SIZE-1)))
                                                                cont_picos +=1
                                                        if tile=="5":
                                                            display.blit(barrera, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
                                                        if tile=="+":
                                                            if cont_objeto1<2:
                                                                lista_objetos1.append(objetos((x*TILE_SIZE,y*TILE_SIZE+5)))
                                                                cont_objeto1 +=1
                                                        if tile=="*":
                                                            if cont_objeto2<2:
                                                                lista_objetos2.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                cont_objeto2 +=1
                                                        if tile=="@":
                                                            if cont_objeto3<2:
                                                                lista_objetos3.append(objetos((x*TILE_SIZE,y*TILE_SIZE+3)))
                                                                cont_objeto3 +=1
                                                        if tile=="#":
                                                            if cont_objeto4<2:
                                                                lista_objetos4.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                cont_objeto4 +=1
                                                        if tile=="&":
                                                            if cont_objeto5<2:
                                                                lista_objetos5.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                cont_objeto5 +=1
                                                        if tile=="$":
                                                            display.blit(camion_img,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]-15))
                                                            lista_camion.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))  
                                                        if tile == '1':
                                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                        if tile == '2':
                                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                        if tile == '3':
                                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                        if tile == '4':
                                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                        if tile == '5':
                                                            tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                        
                                                        x += 1
                                                    y += 1
                                                return tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion
                                                
                                            def movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum):
                                                if event.type == KEYDOWN:
                                                        if event.key == K_RIGHT:
                                                            moving_right = True
                                                        if event.key == K_LEFT:
                                                            moving_left = True
                                                        if event.key == K_UP:
                                                            if air_timer < 4:
                                                                player_y_momentum = -5
                                                if event.type == KEYUP:
                                                        if event.key == K_RIGHT:
                                                            moving_right = False
                                                        if event.key == K_LEFT:
                                                            moving_left = False
                                                return moving_right,moving_left,player_y_momentum

                                            def fondo_mivimiento(scroll):
                                                 x_relativa = (scroll[0]/20) % fondo.get_rect().width
                                                 display.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
                                                 if x_relativa < W:
                                                     display.blit(fondo, (x_relativa, 0))
                                                 
                                                 
                                            player_y_momentum = 0
                                            air_timer = 0

                                            player_rect = pygame.Rect(250, 180, player_image.get_width(), player_image.get_height())
                                            n1=True
                                            while n1: # Bucle del juego
                                                if muerte:
                                                    display.blit(pantalla_muerte,(0,0))
                                                    back_button = button.Button(600, 550, back_img, 1)

                                                    if back_button.draw(screen):
                                                        screen=pygame.display.set_mode((800,600))
                                                        return Menu


                                                      #even handler
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.KEYDOWN:
                                                          if event.key == pygame.K_SPACE:
                                                            game_paused = False
                                                        if event.type == pygame.QUIT:
                                                          run = False

                                                    pygame.display.update()
                                                    

                                                    if timer_final<0:
                                                        display.blit(pantalla_muerte,(0,0))
                                                        back_button = button.Button(600, 550, back_img, 1)

                                                        if back_button.draw(screen):
                                                            screen=pygame.display.set_mode((800,600))
                                                            return Menu


                                                          #even handler
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                              if event.key == pygame.K_SPACE:
                                                                game_paused = False
                                                            if event.type == pygame.QUIT:
                                                              run = False
                                                              
                                                        pygame.display.update()


                                                elif victoria:
                                                    if cont<6:
                                                        display.blit(pantalla_muerte,(0,0))
                                                        display.blit(font2.render(str(cont),True,(255,255,255)),(140,155))
                                                        if timer_final<0:
                                                            display.blit(pantalla_muerte,(0,0))
                                                            back_button = button.Button(600, 550, back_img, 1)

                                                            if back_button.draw(screen):
                                                                screen=pygame.display.set_mode((800,600))
                                                                return Menu


                                                              #even handler
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.KEYDOWN:
                                                                  if event.key == pygame.K_SPACE:
                                                                    game_paused = False
                                                                if event.type == pygame.QUIT:
                                                                  run = False
                                                                  
                                                            pygame.display.update()
                                                    else:
                                                        timer_final -=1
                                                        display.blit(pantalla_victoria,(0,0))
                                                        display.blit(font2.render(str(cont),True,(255,255,255)),(226,110))
                                                        back_button = button.Button(100, 550, back_img, 1)

                                                        if back_button.draw(screen):
                                                            screen=pygame.display.set_mode((800,600))
                                                            return Menu


                                                          #even handler
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                              if event.key == pygame.K_SPACE:
                                                                game_paused = False
                                                            if event.type == pygame.QUIT:
                                                              run = False
                                                              
                                                        pygame.display.update()

                                                        if timer_final<0:
                                                            display.blit(pantalla_muerte,(0,0))
                                                            back_button = button.Button(600, 550, back_img, 1)

                                                            if back_button.draw(screen):
                                                                screen=pygame.display.set_mode((800,600))
                                                                return Menu


                                                              #even handler
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.KEYDOWN:
                                                                  if event.key == pygame.K_SPACE:
                                                                    game_paused = False
                                                                if event.type == pygame.QUIT:
                                                                  run = False
                                                                  
                                                            pygame.display.update()
                                                else:
                                                    scroll=scrolling(player_rect)
                                                    fondo_mivimiento(scroll)
                                                    tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion=poner_mapa(mapa_juego1,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion)
                                                    player_movement,player_y_momentum=player_movimiento(moving_right,moving_left,player_y_momentum)
                                                    player_rect, collisions = move(player_rect, player_movement, tile_rects)
                                                    air_timer,player_y_momentum=salto(collisions,air_timer,player_y_momentum)
                                                    player_flip,player_frame,player_accion,player_img_id,player_img=poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img)
                                                    cont,lista_objetos1=obj_clase(lista_objetos1,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos1)
                                                    cont,lista_objetos2=obj_clase(lista_objetos2,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos2)
                                                    cont,lista_objetos3=obj_clase(lista_objetos3,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos3)
                                                    cont,lista_objetos4=obj_clase(lista_objetos4,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos4)
                                                    cont,lista_objetos5=obj_clase(lista_objetos5,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos5)
                                                    for picos in lista_picos:
                                                        if picos.colision_test(player_rect):
                                                            muerte=True
                                                    for camion in lista_camion:
                                                        if camion.colision_test(player_rect):
                                                            victoria=True
                                                    display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
                                                    display.blit(sol_image,(265,5))
                                                    display.blit(reciclaje_bote_img,(220,0))
                                                    display.blit(reloj_img,(5,5))
                                                for event in pygame.event.get():
                                                    if event.type==QUIT:
                                                     pygame.quit()
                                                     sys.exit()
                                                    if event.type == pygame.USEREVENT:
                                                        timer -=1
                                                        text = str(timer).rjust(3)
                                                    if timer <0:
                                                        muerte=True
                                                    moving_right,moving_left,player_y_momentum=movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum)
                                                  
                                                surf = pygame.transform.scale(display, WINDOW_SIZE)
                                                screen.blit(surf, (0, 0))
                                                if timer>0:
                                                    if victoria==False:
                                                        if muerte==False:
                                                            screen.blit(font.render(str(timer),True,(0,0,0)),(120,45))
                                                            screen.blit(font.render(str(cont),True,(0,0,0)),(980,30))
                                                            screen.blit(font.render(str("/10"),True,(0,0,0)),(1020,30))
                                                pygame.display.update() # actualizamos nuestra pantalla
                                                clock.tick(60) # Ponemos el juego a 60 fps

                                        if event.type == pygame.QUIT:
                                          run = False

                                      pygame.display.update()

                                    #pygame.quit()

                                if level2_button.draw(screen):
                                    SCREEN_WIDTH = 800
                                    SCREEN_HEIGHT = 600

                                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                                    pygame.display.set_caption("PICK EM' EVERITHING")

                                    #FONDO
                                    menuBg = pygame.image.load("images/controls.jpg").convert_alpha()


                                    menu_game = False
                                    game_play = False
                                    game_paused = False
                                    menu_state = "main"
                                        

                                    def draw_text(text, font, text_col, x, y):
                                      img = font.render(text, True, text_col)
                                      screen.blit(menuBg, (0, 0))



                                    #Loop Juegp
                                    menu_niveles = True
                                    while menu_niveles:
                                      screen.blit(menuBg, (0, 0))

                                      #CAMBIA A OPCIONES
                                      menu_state = "options"


                                      #event handler
                                      for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_SPACE:
                                                from clases.clases_mapa import cargar_mapa
                                                from clases.imagenes_objetos import clock,fondo2,picos_image,sol_image,barrera,player_image,pantalla_muerte,reloj_img,camion_img,pantalla_victoria,ladrillo_image2,ladrillo_image4,ladrillo_image3,objetos_index2,reciclaje_bote_img,ladrillo_image1
                                                from clases.clases_player import scrolling,move,salto,player_movimiento,cargar_animacion,poner_animacion
                                                from clases.clases_objetos import objetos,obj_clase

                                                pygame.init() # inicializamos pygame
                                                pygame.display.set_caption('Pick Em All') # Nombre de la ventana
                                                display = pygame.Surface((300, 200))
                                                W,H=1200,700
                                                WINDOW_SIZE = (1200,700) # Tamaño de la ventana
                                                screen = pygame.display.set_mode((W,H)) 

                                                movimiento_fondo=0
                                                moving_right = False
                                                moving_left = False
                                                muerte=False
                                                victoria=False

                                                cont_camion=0
                                                cont_picos=0
                                                cont_objeto1=0
                                                cont_objeto2=0
                                                cont_objeto3=0
                                                cont_objeto4=0
                                                cont=0

                                                bff_cont_objetos1=1
                                                bff_cont_objetos2=2
                                                bff_cont_objetos3=3
                                                bff_cont_objetos4=4

                                                player_img={}
                                                player_img_id={}

                                                player_accion = 'idle'
                                                player_frame = 0
                                                player_flip = False
                                                animacion_frames={}
                                                animacion_database = {}

                                                animacion_database['caminar'],animacion_frames = cargar_animacion('animaciones/caminar',[7,7],animacion_frames)
                                                animacion_database['idle'],animacion_frames = cargar_animacion('animaciones/idle',[7,7,40],animacion_frames)

                                                mapa_juego1=cargar_mapa("mapas/mapa2")

                                                #temporizador
                                                timer, text = 120,'3'.rjust(3)
                                                pygame.time.set_timer(pygame.USEREVENT,1000)
                                                font = pygame.font.SysFont("DAYTONA",56)
                                                font2=pygame.font.SysFont("DAYTONA",35)
                                                timer_final =300

                                                lista_objetos1=[]
                                                lista_objetos2=[]
                                                lista_objetos3=[]
                                                lista_objetos4=[]
                                                lista_picos=[]
                                                lista_camion=[]

                                                def poner_mapa(mapa,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion):
                                                    TILE_SIZE=16
                                                    tile_rects = []
                                                    y = 0
                                                    for fila in mapa:
                                                        x = 0
                                                        for tile in fila:
                                                            if tile == '1':
                                                                display.blit(ladrillo_image3, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if tile == '2':
                                                                display.blit(ladrillo_image2, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if tile == '3':
                                                                display.blit(ladrillo_image1, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if tile=="4":
                                                                display.blit(picos_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                                if cont_picos<64:    
                                                                    lista_picos.append(objetos((x*TILE_SIZE+10,y*TILE_SIZE-1)))
                                                                    cont_picos +=1
                                                            if tile=="5":
                                                                display.blit(barrera, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
                                                            if tile=="6":
                                                                display.blit(ladrillo_image4,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]))
                                                            if tile=="+":
                                                                if cont_objeto1<2:
                                                                    lista_objetos1.append(objetos((x*TILE_SIZE,y*TILE_SIZE+5)))
                                                                    cont_objeto1 +=1
                                                            if tile=="*":
                                                                if cont_objeto2<3:
                                                                    lista_objetos2.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                    cont_objeto2 +=1
                                                            if tile=="@":
                                                                if cont_objeto3<2:
                                                                    lista_objetos3.append(objetos((x*TILE_SIZE,y*TILE_SIZE+3)))
                                                                    cont_objeto3 +=1
                                                            if tile=="#":
                                                                if cont_objeto4<3:
                                                                    lista_objetos4.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                    cont_objeto4 +=1
                                                            if tile=="$":
                                                                display.blit(camion_img,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]-15))
                                                                lista_camion.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))  
                                                            if tile == '1':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '2':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '3':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '4':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '5':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile=="6":
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            
                                                            x += 1
                                                        y += 1
                                                    return tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion
                                                    
                                                def movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum):
                                                    if event.type == KEYDOWN:
                                                            if event.key == K_RIGHT:
                                                                moving_right = True
                                                            if event.key == K_LEFT:
                                                                moving_left = True
                                                            if event.key == K_UP:
                                                                if air_timer < 4:
                                                                    player_y_momentum = -5
                                                    if event.type == KEYUP:
                                                            if event.key == K_RIGHT:
                                                                moving_right = False
                                                            if event.key == K_LEFT:
                                                                moving_left = False
                                                    return moving_right,moving_left,player_y_momentum

                                                def fondo_mivimiento(scroll):
                                                     x_relativa = (scroll[0]/20) % fondo2.get_rect().width
                                                     display.blit(fondo2, (x_relativa - fondo2.get_rect().width, 0))
                                                     if x_relativa < W:
                                                         display.blit(fondo2, (x_relativa, 0))
                                                     
                                                player_y_momentum = 0
                                                air_timer = 0

                                                player_rect = pygame.Rect(280, 180, player_image.get_width(), player_image.get_height())

                                                while True: # Bucle del juego
                                                    if muerte:
                                                        display.blit(pantalla_muerte,(0,0))
                                                        back_button = button.Button(600, 550, back_img, 1)

                                                        if back_button.draw(screen):
                                                            screen=pygame.display.set_mode((800,600))
                                                            return Menu


                                                          #even handler
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                              if event.key == pygame.K_SPACE:
                                                                game_paused = False
                                                            if event.type == pygame.QUIT:
                                                              run = False

                                                        pygame.display.update()


                                                          #even handler
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                              if event.key == pygame.K_SPACE:
                                                                game_paused = False
                                                            if event.type == pygame.QUIT:
                                                              run = FalseZ
                                                        pygame.display.update()

                                                    elif victoria:
                                                        if cont<6:
                                                            timer_final -=1
                                                            display.blit(pantalla_muerte,(0,0))
                                                            display.blit(font2.render(str(cont),True,(255,255,255)),(140,155))
                                                            if timer_final<0:
                                                                pygame.quit()
                                                                sys.exit()
                                                        else:
                                                            timer_final -=1
                                                            display.blit(pantalla_victoria,(0,0))
                                                            display.blit(font2.render(str(cont),True,(255,255,255)),(226,110))
                                                            if timer_final<0:
                                                                pygame.quit()
                                                                sys.exit()
                                                    else:
                                                        scroll=scrolling(player_rect)
                                                        fondo_mivimiento(scroll)
                                                        tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion=poner_mapa(mapa_juego1,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_picos,cont_camion)
                                                        player_movement,player_y_momentum=player_movimiento(moving_right,moving_left,player_y_momentum)
                                                        player_rect, collisions = move(player_rect, player_movement, tile_rects)
                                                        air_timer,player_y_momentum=salto(collisions,air_timer,player_y_momentum)
                                                        player_flip,player_frame,player_accion,player_img_id,player_img=poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img)
                                                        cont,lista_objetos1=obj_clase(lista_objetos1,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos1)
                                                        cont,lista_objetos2=obj_clase(lista_objetos2,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos2)
                                                        cont,lista_objetos3=obj_clase(lista_objetos3,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos3)
                                                        cont,lista_objetos4=obj_clase(lista_objetos4,display,scroll,objetos_index2,player_rect,cont,bff_cont_objetos4)
                                                        for picos in lista_picos:
                                                            if picos.colision_test(player_rect):
                                                                muerte=True
                                                        for camion in lista_camion:
                                                            if camion.colision_test(player_rect):
                                                                victoria=True
                                                        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
                                                        display.blit(sol_image,(265,5))
                                                        display.blit(reciclaje_bote_img,(220,0))
                                                        display.blit(reloj_img,(5,5))
                                                    for event in pygame.event.get():
                                                        if event.type==QUIT:
                                                         pygame.quit()
                                                         sys.exit()
                                                        if event.type == pygame.USEREVENT:
                                                            timer -=1
                                                            text = str(timer).rjust(3)
                                                        if timer <0:
                                                            muerte=True
                                                        moving_right,moving_left,player_y_momentum=movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum)
                                                      
                                                    surf = pygame.transform.scale(display, WINDOW_SIZE)
                                                    screen.blit(surf, (0, 0))
                                                    if timer>0:
                                                        if victoria==False:
                                                            if muerte==False:
                                                                screen.blit(font.render(str(timer),True,(0,0,0)),(120,45))
                                                                screen.blit(font.render(str(cont),True,(0,0,0)),(980,30))
                                                                screen.blit(font.render(str("/10"),True,(0,0,0)),(1020,30))
                                                    pygame.display.update() # actualizamos nuestra pantalla
                                                    clock.tick(60) # Ponemos el juego a 60 fps

                                            if event.type == pygame.QUIT:
                                                run = False

                                      pygame.display.update()

                                if level3_button.draw(screen):
                                    SCREEN_WIDTH = 800
                                    SCREEN_HEIGHT = 600

                                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                                    pygame.display.set_caption("PICK EM' EVERITHING")

                                    #FONDO
                                    menuBg = pygame.image.load("images/controls.jpg").convert_alpha()


                                    menu_game = False
                                    game_play = False
                                    game_paused = False
                                    menu_state = "main"
                                        

                                    def draw_text(text, font, text_col, x, y):
                                      img = font.render(text, True, text_col)
                                      screen.blit(menuBg, (0, 0))



                                    #Loop Juegp
                                    menu_niveles = True
                                    while menu_niveles:
                                      screen.blit(menuBg, (0, 0))

                                      #CAMBIA A OPCIONES
                                      menu_state = "options"


                                      #event handler
                                      for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_SPACE:
                                                from clases.clases_mapa import cargar_mapa
                                                from clases.imagenes_objetos import clock,fondo,tierra_image,tierra_pasto_image,tierra_1_image,picos_image,sol_image,barrera,player_image,pantalla_muerte,reloj_img,camion_img,pantalla_victoria
                                                from clases.clases_player import scrolling,move,salto,player_movimiento,cargar_animacion,poner_animacion
                                                from clases.clases_objetos import objetos,obj_clase
                                                from  clases.imagenes_objetos import objetos_index1,reciclaje_bote_img

                                                pygame.display.set_caption('Pick Em All') # Nombre de la ventana
                                                display = pygame.Surface((300, 200))
                                                W,H=1200,700
                                                WINDOW_SIZE = (1200,700) # Tamaño de la ventana
                                                screen = pygame.display.set_mode((W,H)) 

                                                movimiento_fondo=0
                                                moving_right = False
                                                moving_left = False
                                                muerte=False
                                                victoria=False

                                                cont_camion=0
                                                cont_picos=0
                                                cont_objeto1=0
                                                cont_objeto2=0
                                                cont_objeto3=0
                                                cont_objeto4=0
                                                cont_objeto5=0
                                                cont=0

                                                bff_cont_objetos1=1
                                                bff_cont_objetos2=2
                                                bff_cont_objetos3=3
                                                bff_cont_objetos4=4
                                                bff_cont_objetos5=5

                                                player_img={}
                                                player_img_id={}

                                                player_accion = 'idle'
                                                player_frame = 0
                                                player_flip = False
                                                animacion_frames={}
                                                animacion_database = {}

                                                animacion_database['caminar'],animacion_frames = cargar_animacion('animaciones/caminar',[7,7],animacion_frames)
                                                animacion_database['idle'],animacion_frames = cargar_animacion('animaciones/idle',[7,7,40],animacion_frames)

                                                mapa_juego1=cargar_mapa("mapas/mapa3")

                                                #temporizador
                                                timer, text = 120,'3'.rjust(3)
                                                pygame.time.set_timer(pygame.USEREVENT,1000)
                                                font = pygame.font.SysFont("DAYTONA",56)
                                                font2=pygame.font.SysFont("DAYTONA",35)
                                                timer_final =300

                                                lista_objetos1=[]
                                                lista_objetos2=[]
                                                lista_objetos3=[]
                                                lista_objetos4=[]
                                                lista_objetos5=[]
                                                lista_picos=[]
                                                lista_camion=[]

                                                def poner_mapa(mapa,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion):
                                                    TILE_SIZE=16
                                                    tile_rects = []
                                                    y = 0
                                                    for fila in mapa:
                                                        x = 0
                                                        for tile in fila:
                                                            if tile == '1':
                                                                display.blit(tierra_pasto_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if tile == '2':
                                                                display.blit(tierra_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if tile == '3':
                                                                display.blit(tierra_1_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                            if tile=="4":
                                                                display.blit(picos_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                                                                if cont_picos<141:    
                                                                    lista_picos.append(objetos((x*TILE_SIZE+10,y*TILE_SIZE-1)))
                                                                    cont_picos +=1
                                                            if tile=="5":
                                                                display.blit(barrera, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
                                                            if tile=="+":
                                                                if cont_objeto1<3:
                                                                    lista_objetos1.append(objetos((x*TILE_SIZE,y*TILE_SIZE+5)))
                                                                    cont_objeto1 +=1
                                                            if tile=="*":
                                                                if cont_objeto2<2:
                                                                    lista_objetos2.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                    cont_objeto2 +=1
                                                            if tile=="@":
                                                                if cont_objeto3<2:
                                                                    lista_objetos3.append(objetos((x*TILE_SIZE,y*TILE_SIZE+3)))
                                                                    cont_objeto3 +=1
                                                            if tile=="#":
                                                                if cont_objeto4<3:
                                                                    lista_objetos4.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                    cont_objeto4 +=1
                                                            if tile=="&":
                                                                if cont_objeto5<2:
                                                                    lista_objetos5.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))
                                                                    cont_objeto5 +=1
                                                            if tile=="$":
                                                                display.blit(camion_img,(x*TILE_SIZE-scroll[0],y*TILE_SIZE-scroll[1]-15))
                                                                lista_camion.append(objetos((x*TILE_SIZE,y*TILE_SIZE)))  
                                                            if tile == '1':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '2':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '3':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '4':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            if tile == '5':
                                                                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                                                            
                                                            x += 1
                                                        y += 1
                                                    return tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion
                                                    
                                                def movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum):
                                                    if event.type == KEYDOWN:
                                                            if event.key == K_RIGHT:
                                                                moving_right = True
                                                            if event.key == K_LEFT:
                                                                moving_left = True
                                                            if event.key == K_UP:
                                                                if air_timer < 4:
                                                                    player_y_momentum = -5
                                                    if event.type == KEYUP:
                                                            if event.key == K_RIGHT:
                                                                moving_right = False
                                                            if event.key == K_LEFT:
                                                                moving_left = False
                                                    return moving_right,moving_left,player_y_momentum

                                                def fondo_mivimiento(scroll):
                                                     x_relativa = (scroll[0]/20) % fondo.get_rect().width
                                                     display.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
                                                     if x_relativa < W:
                                                         display.blit(fondo, (x_relativa, 0))
                                                     
                                                player_y_momentum = 0
                                                air_timer = 0

                                                player_rect = pygame.Rect(250, 180, player_image.get_width(), player_image.get_height())

                                                while True: # Bucle del juego
                                                    if muerte:
                                                        display.blit(pantalla_muerte,(0,0))
                                                        back_button = button.Button(600, 550, back_img, 1)

                                                        if back_button.draw(screen):
                                                            screen=pygame.display.set_mode((800,600))
                                                            return Menu


                                                          #even handler
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                              if event.key == pygame.K_SPACE:
                                                                game_paused = False
                                                            if event.type == pygame.QUIT:
                                                              run = False

                                                        pygame.display.update()


                                                          #even handler
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                              if event.key == pygame.K_SPACE:
                                                                game_paused = False
                                                            if event.type == pygame.QUIT:
                                                              run = False

                                                        pygame.display.update()

                                                    elif victoria:
                                                        if cont<10:
                                                            timer_final -=1
                                                            display.blit(pantalla_muerte,(0,0))
                                                            display.blit(font2.render(str(cont),True,(255,255,255)),(140,155))
                                                            if timer_final<0:
                                                                pygame.quit()
                                                                sys.exit()
                                                        else:
                                                            timer_final -=1
                                                            display.blit(pantalla_victoria,(0,0))
                                                            display.blit(font2.render(str(cont),True,(255,255,255)),(226,110))
                                                            if timer_final<0:
                                                                pygame.quit()
                                                                sys.exit()
                                                    else:
                                                        scroll=scrolling(player_rect)
                                                        fondo_mivimiento(scroll)
                                                        tile_rects,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion=poner_mapa(mapa_juego1,cont_objeto1,cont_objeto2,cont_objeto3,cont_objeto4,cont_objeto5,cont_picos,cont_camion)
                                                        player_movement,player_y_momentum=player_movimiento(moving_right,moving_left,player_y_momentum)
                                                        player_rect, collisions = move(player_rect, player_movement, tile_rects)
                                                        air_timer,player_y_momentum=salto(collisions,air_timer,player_y_momentum)
                                                        player_flip,player_frame,player_accion,player_img_id,player_img=poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img)
                                                        cont,lista_objetos1=obj_clase(lista_objetos1,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos1)
                                                        cont,lista_objetos2=obj_clase(lista_objetos2,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos2)
                                                        cont,lista_objetos3=obj_clase(lista_objetos3,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos3)
                                                        cont,lista_objetos4=obj_clase(lista_objetos4,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos4)
                                                        cont,lista_objetos5=obj_clase(lista_objetos5,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos5)
                                                        for picos in lista_picos:
                                                            if picos.colision_test(player_rect):
                                                                muerte=True
                                                        for camion in lista_camion:
                                                            if camion.colision_test(player_rect):
                                                                victoria=True
                                                        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
                                                        display.blit(sol_image,(265,5))
                                                        display.blit(reciclaje_bote_img,(220,0))
                                                        display.blit(reloj_img,(5,5))
                                                    for event in pygame.event.get():
                                                        if event.type==QUIT:
                                                         pygame.quit()
                                                         sys.exit()
                                                        if event.type == pygame.USEREVENT:
                                                            timer -=1
                                                            text = str(timer).rjust(3)
                                                        if timer <0:
                                                            muerte=True
                                                        moving_right,moving_left,player_y_momentum=movimiento_teclas(event,moving_right,moving_left,air_timer,player_y_momentum)
                                                      
                                                    surf = pygame.transform.scale(display, WINDOW_SIZE)
                                                    screen.blit(surf, (0, 0))
                                                    if timer>0:
                                                        if victoria==False:
                                                            if muerte==False:
                                                                screen.blit(font.render(str(timer),True,(0,0,0)),(120,45))
                                                                screen.blit(font.render(str(cont),True,(0,0,0)),(980,30))
                                                                screen.blit(font.render(str("/12"),True,(0,0,0)),(1020,30))
                                                    pygame.display.update() # actualizamos nuestra pantalla
                                                    clock.tick(60) # Ponemos el juego a 60 fps
                                     
                                        if event.type == pygame.QUIT:
                                            run = False

                                        pygame.display.update()


                                if back_button.draw(screen):
                                    return "enter1"
                              else:
                                draw_text("Press SPACE to pause", font, TEXT_COL, 10, 10)


                              #event handler
                              for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                  if event.key == pygame.K_SPACE:
                                    game_paused = False
                                if event.type == pygame.QUIT:
                                  sys.exit(0)

                              pygame.display.update()

                            pygame.quit()


                          #event handler
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        game_paused = False
                                    if event.type == pygame.QUIT:
                                        sys.exit(0)

                                pygame.display.update()
                                pygame.quit()

                        if credits_button.draw(screen):
                            SCREEN_WIDTH = 800
                            SCREEN_HEIGHT = 600

                            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                            pygame.display.set_caption("PICK EM' EVERITHING")

                            menuBg = pygame.image.load("credits.jpg").convert_alpha()


                            font = pygame.font.SysFont("cartoon.tff", 40)

                            TEXT_COL = (255, 255, 255)
                            

                            back_img = pygame.image.load('images/button_back.png').convert_alpha()
                            back_button = button.Button(332, 465, back_img, 1)


                            def draw_text(text, font, text_col, x, y):
                              img = font.render(text, True, text_col)
                              screen.blit(menuBg, (0, 0))
                            run = True
                            while run:

                              screen.blit(menuBg, (0, 0))

                              #check if game is paused
                              menu_state = "creditos"

                                #check if the options menu is open
                              if menu_state == "creditos":
                                  #draw the different options buttons
                                if back_button.draw(screen):
                                    return Menu1


                              #event handler
                              for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                  if event.key == pygame.K_SPACE:
                                    game_paused = False
                                if event.type == pygame.QUIT:
                                  run = False

                              pygame.display.update()

                            pygame.quit()


                        if settings_button.draw(screen):
                            SCREEN_WIDTH = 800
                            SCREEN_HEIGHT = 600

                            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                            pygame.display.set_caption("PICK EM' EVERITHING")

                            #FONDO
                            menuBg = pygame.image.load("images/escena1.jpg").convert_alpha()
                            menuBg1 = pygame.image.load("images/escena.jpg").convert_alpha()


                            menu_game = False
                            game_play = False
                            game_paused = False
                            menu_state = "main"


                            video_img = pygame.image.load('images/lenguagueesp.png').convert_alpha()
                            video_button = button.Button(226, 75, video_img, 1)
                            back_img = pygame.image.load('images/button_back.png').convert_alpha()
                            back_button = button.Button(332, 450, back_img, 1)
                            audio_img = pygame.image.load("images/button_audioplay.png").convert_alpha()
                            audio_button = button.Button(225, 200, audio_img, 1)
                            audio1_img = pygame.image.load("images/button_audiopause.png").convert_alpha()
                            audio1_button = button.Button(225, 315, audio1_img, 1)
                                

                            def draw_text(text, font, text_col, x, y):
                                img = font.render(text, True, text_col)
                                screen.blit(menuBg, (0, 0))



                            run1 = True
                            while run1:
                              screen.blit(menuBg, (0, 0))

                              #CAMBIA A OPCIONES
                              menu_state = "options"

                                #COMPRUEBA QUE ESTES EN OPCIONES
                              if menu_state == "options":
                                  #BOTONES
                                if video_button.draw(screen):
                                    return Menu
                                if audio_button.draw(screen):
                                    pygame.mixer.music.play()
                                if audio1_button.draw(screen):
                                    pygame.mixer.music.pause()
                                    

                                if back_button.draw(screen):
                                    return "enter1"
                              else:
                                draw_text("Press SPACE to pause", font, TEXT_COL, 10, 10)


                              #event handler
                              for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                  if event.key == pygame.K_SPACE:
                                    game_paused = False
                                if event.type == pygame.QUIT:
                                    sys.exit(0)

                              pygame.display.update()

                            pygame.quit()


                          #event handler
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        game_paused = False
                                    if event.type == pygame.QUIT:
                                        sys.exit(0)

                                pygame.display.update()
                                pygame.quit()


                        if quit_button.draw(screen):
                            print (" Gracias por jugar este juego ;D")
                            sys.exit(0)


                      #event handler
                      for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                          if event.key == pygame.K_SPACE:
                            game_paused = False
                        if event.type == pygame.QUIT:
                            sys.exit(0)

                      pygame.display.update()

                    pygame.quit()

                    if quit_button.draw(screen):
                        print (" Gracias por jugar este juego ;D")
                        sys.exit(0)


                        pygame.display.update()

                        pygame.quit()

                    

                if back_button.draw(screen):
                    return enter
              else:
                draw_text("Press SPACE to pause", font, TEXT_COL, 10, 10)


              #event handler
              for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                    game_paused = False
                if event.type == pygame.QUIT:
                  run = False

              pygame.display.update()

            pygame.quit()


          #event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_paused = False
                    if event.type == pygame.QUIT:
                        run = False

                pygame.display.update()
                pygame.quit()


        if quit_button.draw(screen):
            print (" Gracias por jugar este juego ;D")
            sys.exit(0)


      #event handler
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            game_paused = False
        if event.type == pygame.QUIT:
          run = False

      pygame.display.update()

    pygame.quit()

    if quit_button.draw(screen):
        print (" Gracias por jugar este juego ;D")
        sys.exit(0)


        pygame.display.update()

        pygame.quit()


def comenzar_nuevo_juego():

    print("juego presenta")

def mostrar_opciones():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("PICK EM' EVERITHING")

    #FONDO
    menuBg = pygame.image.load("images/escena1.jpg").convert_alpha()
    menuBg1 = pygame.image.load("images/escena.jpg").convert_alpha()


    menu_game = False
    game_play = False
    game_paused = False
    menu_state = "main"

    resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    options_img = pygame.image.load("images/button_options.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    video_img = pygame.image.load('images/lenguague.png').convert_alpha()
    audio_img = pygame.image.load('images/button_audio1.png').convert_alpha()
    keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()
    audio_img1 = pygame.image.load('images/button_audio1.png').convert_alpha()



    resume_button = button.Button(304, 300, resume_img, 1)
    options_button = button.Button(297, 390, options_img, 1)
    quit_button = button.Button(336, 490, quit_img, 1)
    video_button = button.Button(226, 75, video_img, 1)
    audio_button = button.Button(225, 200, audio_img, 1)
    keys_button = button.Button(246, 325, keys_img, 1)
    back_button = button.Button(332, 450, back_img, 1)
        

    def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      screen.blit(menuBg, (0, 0))



    #Loop Juegp
    run = True
    while run:
      screen.blit(menuBg, (0, 0))

      #CAMBIA A OPCIONES
      menu_state = "options"

        #COMPRUEBA QUE ESTES EN OPCIONES
      if menu_state == "options":
          #BOTONES
        if audio_button.draw(screen):
            print("Quitar musica")
        if video_button.draw(screen):
            print("En ingles")
            

        if back_button.draw(screen):
            return enter
      else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 10, 10)


      #event handler
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            game_paused = False
        if event.type == pygame.QUIT:
          run = False

      pygame.display.update()

    pygame.quit()

def creditos():

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("PICK EM' EVERITHING")

    menuBg = pygame.image.load("creditos.jpg").convert_alpha()


    font = pygame.font.SysFont("cartoon.tff", 40)

    TEXT_COL = (255, 255, 255)
    

    back_img = pygame.image.load('images/button_back.png').convert_alpha()
    back_button = button.Button(332, 465, back_img, 1)


    def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      screen.blit(menuBg, (0, 0))
    run = True
    while run:

      screen.blit(menuBg, (0, 0))

      #check if game is paused
      menu_state = "creditos"

        #check if the options menu is open
      if menu_state == "creditos":
          #draw the different options buttons
        if back_button.draw(screen):
            return Menu


      #event handler
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            game_paused = False
        if event.type == pygame.QUIT:
          run = False

      pygame.display.update()

    pygame.quit()


        
def salir_del_programa():
    print (" Gracias por jugar este juego ;D")
    sys.exit(0)





salir = False
menu = False
menu_state = "main"

opciones = [
    ("\n\n\n\n\n\n\n", enter)
    ]

pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("PICK EM' EVERITHING")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

pygame.mixer.music.load("sonidos/Musica.mp3")
pygame.mixer.music.play(-1)

menu_state = False
credits_state = False

run = True
while run:

    menu_state = True
    if menu_state == True:
        screen = pygame.display.set_mode((800, 600))
        fondo = pygame.image.load("fondoenter.jpg").convert()
        menu = Menu(opciones, creditos)

        while not salir:
            for e in pygame.event.get():
                if e.type == QUIT:
                    salir = True
                    run = False

            screen.blit(fondo, (0, 0))
            menu.actualizar()
            menu.imprimir(screen)

            pygame.display.flip()
            pygame.time.delay(10)