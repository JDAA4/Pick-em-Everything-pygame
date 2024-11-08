
def cargar_mapa(camino):
    f=open(camino +".txt","r")
    dato=f.read()
    f.close()
    dato=dato.split("\n")
    mapa_juego=[]
    for fila in dato:
        mapa_juego.append(list(fila))
    return mapa_juego