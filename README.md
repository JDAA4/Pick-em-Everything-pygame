# *Pick-em-Everything-pygame*

## Descripción

Pick-em-Everything es un juego desarrollado con Pygame donde el jugador debe recoger objetos y evitar obstáculos en diferentes niveles. El juego incluye un menú principal, opciones de configuración y una pantalla de créditos.

![Demo del menu](/assets/pygame1.gif)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

![Demo del juego](/assets/pygame2.gif)

## Instalación
Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/Pick-em-Everything-pygame.git
```
Navega al directorio del proyecto:
```bash
cd Pick-em-Everything-pygame
```
Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución
Para ejecutar el juego, simplemente corre el archivo JUEGO Y MENU.py
```bash
python JUEGO Y MENU.py
```

## Estructura del Proyecto
pycache/ animaciones/ caminar/ idle/ button.py clases/ pycache/ clases_mapa.py clases_objetos.py clases_player.py enemigos.py imagenes_objetos.py Comic Kings.otf images/ JUEGO Y MENU.py mapas/ mapa1.txt mapa2.txt mapa3.txt objetos/ fondos/ tileset/ README.md sonidos/


### Archivos y Directorios Principales

- `JUEGO Y MENU.py`: Archivo principal que maneja la lógica del juego y el menú.
- `clases/`: Contiene las clases y funciones auxiliares para el juego.
  - `clases_mapa.py`: Funciones para cargar y manejar los mapas del juego.
  - `clases_objetos.py`: Clases y funciones para manejar los objetos del juego.
  - `clases_player.py`: Funciones para manejar el movimiento y las animaciones del jugador.
  - `enemigos.py`: Archivo para manejar los enemigos del juego.
  - `imagenes_objetos.py`: Contiene las imágenes y objetos utilizados en el juego.
- `animaciones/`: Directorio que contiene las animaciones del jugador.
- `images/`: Directorio que contiene las imágenes utilizadas en el juego.
- `mapas/`: Directorio que contiene los archivos de texto con los mapas del juego.
- `objetos/`: Directorio que contiene los fondos y tilesets del juego.
- `sonidos/`: Directorio que contiene los sonidos utilizados en el juego.
- `button.py`: Archivo que maneja los botones del menú.



