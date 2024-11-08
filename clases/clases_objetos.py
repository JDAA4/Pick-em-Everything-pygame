import pygame
class objetos():
    def __init__(self, loc):
        self.loc = loc

    def mostrar(self, surf, scroll,objetos_index,bff_cont_objetos):
        surf.blit(objetos_index[bff_cont_objetos], (self.loc[0]-scroll[0], self.loc[1]-scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 8, 9)

    def colision_test(self, rect):
        objeto_rect = self.get_rect()
        return objeto_rect.colliderect(rect)

def obj_clase(lista_objetos,display,scroll,objetos_index1,player_rect,cont,bff_cont_objetos):
    for objeto in lista_objetos:
        objeto.mostrar(display,scroll,objetos_index1,bff_cont_objetos)
        if objeto.colision_test(player_rect):
            cont +=1
            lista_objetos.remove(objeto)
    return cont,lista_objetos