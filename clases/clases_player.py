import pygame

verdadero_scroll=[0,0]

def scrolling(player_rect):
    verdadero_scroll[0] +=(player_rect.x-verdadero_scroll[0]-150)/5
    verdadero_scroll[1]+=(player_rect.y-verdadero_scroll[1]-100)/5
    scroll=verdadero_scroll.copy()
    scroll[0]=int(scroll[0])
    scroll[1]=int(scroll[1])
    return scroll

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def salto(collisions,air_timer,player_y_momentum):
    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1
    return air_timer,player_y_momentum

def player_movimiento(moving_right,moving_left,player_y_momentum):
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3
    return player_movement,player_y_momentum

def cargar_animacion(camino,frame_duracion,animacion_frames):
    animacion_nombre = camino.split('/')[-1]
    animacion_frame_data = []
    n = 0
    for frame in frame_duracion:
        animacion_frame_id = animacion_nombre + '_' + str(n)
        img_loc = camino + '/' + animacion_frame_id + '.png'
        animacion_image = pygame.image.load(img_loc)
        animacion_image.set_colorkey((0,0,0))
        animacion_frames[animacion_frame_id] = animacion_image.copy()
        for i in range(frame):
            animacion_frame_data.append(animacion_frame_id)
        n += 1
    return animacion_frame_data,animacion_frames

def invertir(accion_var,frame,nuevo_valor):
    if accion_var!=nuevo_valor:
        accion_var=nuevo_valor
        frame =0
    return accion_var,frame

def poner_animacion(player_movement,player_accion,player_flip,player_frame,animacion_database,animacion_frames,player_img_id,player_img):
    if player_movement[0] == 0:
        player_accion,player_frame = invertir(player_accion,player_frame,'idle')
    if player_movement[0] > 0:
        player_flip = False
        player_accion,player_frame = invertir(player_accion,player_frame,'caminar')
    if player_movement[0] < 0:
        player_flip = True
        player_accion,player_frame = invertir(player_accion,player_frame,'caminar')
    player_frame +=1
    if player_frame >= len(animacion_database[player_accion]):
        player_frame = 0
    player_img_id = animacion_database[player_accion][player_frame]
    player_img = animacion_frames[player_img_id]
    return player_flip,player_frame,player_accion,player_img_id,player_img