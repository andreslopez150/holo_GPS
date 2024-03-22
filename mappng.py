import cv2
import matplotlib.pyplot as plt
import time 
from luma.core.interface.serial import i2c
from luma.oled.device import sh1107
from PIL import Image

#serial = i2c(port=1, address=0x3C)

# Inicializar la pantalla OLED SH1107
#device = sh1107(serial, rotate=0) 

# Dimensiones de la imagen
sizeX = 3996
sizeY = 3436

# Coordenadas de la esquina superior izquierda y esquina inferior derecha
x1 = -3.90940805846654
y1 = 38.9974780467993
y0 = 38.9688989737754
x0 = -3.95215840741489

# Tamaño del área a recortar
area_size = 128

# Resolución del mapa en términos de píxeles por longitud y píxeles por latitud
map_resolution = 256 

# Ancho y alto del mapa en grados
ancho_x = abs(x1 - x0)
alto_y = abs(y1 - y0)

# Píxeles por grado en X e Y
pixel_por_grado_x = sizeX / ancho_x
pixel_por_grado_y = sizeY / alto_y

# Lista de coordenadas a iterar
coordenadas = [
    [-3.927655, 38.995411],
[-3.927592, 38.99573],
[-3.927676, 38.995855],
[-3.927767, 38.995905],
[-3.927653, 38.995977],
[-3.927645, 38.996067],
[-3.927728, 38.996145],
[-3.927828, 38.996158],
[-3.927962, 38.996069],
[-3.927944, 38.995962],
[-3.92787, 38.995913],
[-3.927991, 38.995757],
[-3.928005, 38.995682],
[-3.92782, 38.995162],
[-3.927885, 38.99443],
[-3.927954, 38.992465],
[-3.928056, 38.99133]
]

# Abrir la imagen con OpenCV
image_path = "imagen_procesada.png"
image = cv2.imread(image_path)

# Color del punto en formato BGR (azul, verde, rojo)
color = (0, 0, 255)  # Rojo en este caso
thickness = -1  # Para rellenar el círculo

# Crear una única figura y eje
fig, ax = plt.subplots()

# Iterar sobre las coordenadas y realizar la operación en cada posición
for coord in coordenadas:
    x, y = coord

    # Diferencia en coordenadas X e Y
    diferencia_x = abs(x - x0)
    diferencia_y = abs(y1 - y)

    # Conversión de coordenadas geográficas a coordenadas en píxeles
    px = int(diferencia_x * pixel_por_grado_x)
    py = int(diferencia_y * pixel_por_grado_y)  # Invertir el eje Y

    # Calcular límites del área a recortar
    top_left_x = px - area_size // 2
    top_left_y = py - area_size // 2
    bottom_right_x = px + area_size // 2
    bottom_right_y = py + area_size // 2

    # Asegurarse de que los límites estén dentro de los límites de la imagen
    top_left_x = max(0, top_left_x)
    top_left_y = max(0, top_left_y)
    bottom_right_x = min(sizeX, bottom_right_x)
    bottom_right_y = min(sizeY, bottom_right_y)

    # Dibujar el punto en la imagen
    cv2.circle(image, (px, py), 3, color, thickness)

    # Recortar el área de interés de la imagen
    area_recortada = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    # Mostrar el área recortada
    cv2.imshow('Frame completo', area_recortada)
    
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    """ax.imshow(cv2.cvtColor(area_recortada, cv2.COLOR_BGR2RGB))
    ax.set_title(f"Coordenada: ({x}, {y})")
    plt.draw()  # Actualizar la ventana de visualización
    plt.pause(1)  # Pausa la ejecución durante 1 segundo
    ax.clear()  # Limpiar el eje para la próxima iteración
    
plt.close()"""  # Cerrar la ventana después de completar todas las iteraciones
    
    
    #imagen_pil = Image.fromarray(cv2.cvtColor(area_recortada, cv2.COLOR_BGR2RGB))
    #imagen_pil.show()
    # Mostrar la imagen en la pantalla OLED
    #device.display(imagen_pil)
    
    time.sleep(1)
cv2.destroyAllWindows()