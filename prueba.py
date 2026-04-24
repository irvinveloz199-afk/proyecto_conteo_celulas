import cv2
import matplotlib.pyplot as plt
import numpy as np
# Importamos tus funciones de la carpeta que creaste
from conteo_lib.filtros import filtro_sobel

# 1. Cargar imagen
# ASEGÚRATE de tener una imagen llamada 'test.jpg' en tu carpeta
img = cv2.imread('test.jpg') 

if img is None:
    print("Error: No encontré 'test.jpg'. Pon una imagen con ese nombre en la carpeta.")
else:
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("Procesando imagen con Sobel manual... Ten paciencia.")
    bordes = filtro_sobel(gris)

    # Mostrar resultados
    plt.subplot(1,2,1), plt.imshow(gris, cmap='gray'), plt.title('Original')
    plt.subplot(1,2,2), plt.imshow(bordes, cmap='gray'), plt.title('Bordes Manuales')
    plt.show()