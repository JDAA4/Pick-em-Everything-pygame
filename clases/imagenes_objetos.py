import pygame
#Globales
clock = pygame.time.Clock() # iniciamos nuestro reloj
picos_image=pygame.image.load("objetos/tileset/picos.png")
picos_image=pygame.transform.scale(picos_image,(21,21))
barrera=pygame.image.load("objetos/tileset/Barrera.png")
player_image=pygame.image.load("animaciones/idle/idle_0.png")
player_image=pygame.transform.scale(player_image,(18,22))
bolsa_img=pygame.image.load("objetos/Bolsa.png")
bolsa_img.set_colorkey((0,0,0))
bolsa_img=pygame.transform.scale(bolsa_img,(12,12))
cafe_img=pygame.image.load("objetos/Cafe.png")
cafe_img.set_colorkey((0,0,0))
cafe_img=pygame.transform.scale(cafe_img,(16,18))
lata1_img=pygame.image.load("objetos/Lata1.png")
lata1_img.set_colorkey((0,0,0))
lata1_img=pygame.transform.scale(lata1_img,(16,16))
papas_img=pygame.image.load("objetos/Papas.png")
papas_img.set_colorkey((0,0,0))
papas_img=pygame.transform.scale(papas_img,(16,16))
reciclaje=pygame.image.load("objetos/BoteReciclaje.png")
reciclaje.set_colorkey((0,0,0))
reciclaje_bote_img=pygame.transform.scale(reciclaje,(22,28))
pantalla_muerte=pygame.image.load("objetos/fondos/perdiste.png")
pantalla_muerte=pygame.transform.scale(pantalla_muerte,(300,200))
pantalla_victoria=pygame.image.load("objetos/fondos/victoria.png")
pantalla_victoria=pygame.transform.scale(pantalla_victoria,(300,200))
reloj_img=pygame.image.load("objetos/reloj.png")
reloj_img.set_colorkey((0,0,0))
camion_img=pygame.image.load("objetos/Camion.png")
camion_img.set_colorkey((0,0,0))
victory_screen = pygame.image.load("objetos/fondos/winning.png")
victory_screen = pygame.transform.scale(victory_screen,(300,200))
lose_screen = pygame.image.load("objetos/fondos/gameover.png")
lose_screen = pygame.transform.scale(lose_screen,(300,200))

#Nivel 1 y nivel 3
fondo=pygame.image.load("objetos/fondos/fondo.png")
tierra_image = pygame.image.load('objetos/tileset/dirtu.png')
tierra_image=pygame.transform.scale(tierra_image,(21,21))
tierra_pasto_image = pygame.image.load('objetos/tileset/1.png')
tierra_pasto_image=pygame.transform.scale(tierra_pasto_image,(21,21))
tierra_1_image= pygame.image.load("objetos/tileset/dirt2.png")
tierra_1_image=pygame.transform.scale(tierra_1_image,(21,21))
sol_image=pygame.image.load("objetos/sol.png")
arbol2_image= pygame.image.load("objetos/Arbol2.png")
tronco_img=pygame.image.load("objetos/Tronco.png")
tronco_img.set_colorkey((0,0,0))
tronco_img=pygame.transform.scale(tronco_img,(12,18))
objetos_index1={1:bolsa_img,
                2:cafe_img,
                3:lata1_img,
                4:papas_img,
                5:tronco_img}

#Nivel 2
fondo2=pygame.image.load("objetos/fondos/CITY.png")
fondo2=pygame.transform.scale(fondo2,(300,200))
ladrillo_image1=pygame.image.load("objetos/tileset/ladrillo.png")
ladrillo_image1=pygame.transform.scale(ladrillo_image1,(21,21))
ladrillo_image2=pygame.image.load("objetos/tileset/ladrillo2.png")
ladrillo_image2=pygame.transform.scale(ladrillo_image2,(21,21))
ladrillo_image3=pygame.image.load("objetos/tileset/ladrillo3.png")
ladrillo_image3=pygame.transform.scale(ladrillo_image3,(21,21))
ladrillo_image4=pygame.image.load("objetos/tileset/ladrillo4.png")
ladrillo_image4=pygame.transform.scale(ladrillo_image4,(21,21))
objetos_index2={1:bolsa_img,
                2:cafe_img,
                3:lata1_img,
                4:papas_img}