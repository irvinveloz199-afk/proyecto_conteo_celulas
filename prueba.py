import cv2
import matplotlib.pyplot as plt
from conteo_lib.filtros import filtro_sobel
from conteo_lib.segmentacion import umbral_manual

# 1. Cargar imagen
img = cv2.imread('test.jpg')
if img is None:
    print("Error: No encontré test.jpg")
else:
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Detectar bordes con tu función Sobel
    print("Procesando bordes...")
    bordes = filtro_sobel(gris)

    # 3. Convertir a Blanco y Negro Puro
    # Si ves que sale muy negra, baja el 100 a 50. Si sale muy blanca, súbelo.
    print("Segmentando...")
    binaria = umbral_manual(bordes, 100) 

    # 4. Mostrar resultados
    plt.figure(figsize=(12, 5))
    plt.subplot(1,3,1), plt.imshow(gris, cmap='gray'), plt.title('Original (Gris)')
    plt.subplot(1,3,2), plt.imshow(bordes, cmap='gray'), plt.title('Bordes Detectados')
    plt.subplot(1,3,3), plt.imshow(binaria, cmap='gray'), plt.title('Imagen Binaria')
    plt.show()