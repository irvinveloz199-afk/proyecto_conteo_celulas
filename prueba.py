import cv2
import matplotlib.pyplot as plt

from conteo_lib.conteo import Pipeline_Celulas
from conteo_lib.hough import HoughCircle
from conteo_lib.filtros import BandPass, Logarithmic

# Aqui seleccionamos la imagen que queremos usar 
imagen = "test1.jpg"
# imagen = "test2.jpg"
# imagen = "test3.jpg"
# imagen = "test4.jpg"
# imagen = "test5.jpg"

# Carga de matriz de imagen en espacio de color BGR
img = cv2.imread(imagen)

# Validación de integridad del archivo de entrada
if img is None:
    print(f"No se encontró la imagen: {imagen}")

else:
    # Ejecución del núcleo de procesamiento (Pipeline modular)
    total, resultado, sobel, canny, mask, otsu = Pipeline_Celulas(img)

    # Evidencia técnica: Ejecución de la Transformada de Hough por separado
    total_hough, img_hough, mask_hough = HoughCircle(img)

    # Generación de evidencias para dominio de frecuencia y transformaciones de punto
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Filtrado Pasa-Banda en frecuencia (Análisis espectral)
    bandpass = BandPass(gray, freq=30, dist=20)

    # Mejora de contraste mediante mapeo logarítmico
    log_img = Logarithmic(gray, c=1)

    # Reporte de métricas en la consola de salida
    print("Imagen utilizada:", imagen)
    print("Células detectadas:", total)
    print("Círculos Hough detectados:", total_hough)

    # Configuración de la interfaz gráfica de visualización (Matplotlib)
    plt.figure(figsize=(16, 10))

    # Panel 1: Salida final con Bounding Boxes y conteo estadístico
    plt.subplot(2, 4, 1)
    plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
    plt.title(f"Conteo final: {total}")
    plt.axis("off")

    # Panel 2: Máscara binaria resultante del proceso de segmentación
    plt.subplot(2, 4, 2)
    plt.imshow(mask, cmap="gray")
    plt.title("Segmentación / Máscara")
    plt.axis("off")

    # Panel 3: Imagen original en espacio de color RGB
    plt.subplot(2, 4, 3)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f"Imagen original: {imagen}")
    plt.axis("off")

    # Panel 4: Representación de la geometría detectada por Hough
    plt.subplot(2, 4, 4)
    plt.imshow(cv2.cvtColor(img_hough, cv2.COLOR_BGR2RGB))
    plt.title("Hough")
    plt.axis("off")

    # Panel 5: Magnitud del gradiente calculada mediante Sobel
    plt.subplot(2, 4, 5)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel")
    plt.axis("off")

    # Panel 6: Mapa de bordes obtenido mediante el detector de Canny
    plt.subplot(2, 4, 6)
    plt.imshow(canny, cmap="gray")
    plt.title("Canny")
    plt.axis("off")

    # Panel 7: Reconstrucción espacial tras el filtrado en frecuencia
    plt.subplot(2, 4, 7)
    plt.imshow(bandpass, cmap="gray")
    plt.title("Filtro en frecuencia")
    plt.axis("off")

    # Panel 8: Resultado del realce de brillo logarítmico
    plt.subplot(2, 4, 8)
    plt.imshow(log_img, cmap="gray")
    plt.title("Transformación log")
    plt.axis("off")

    # Optimización de la distribución de la cuadrícula de gráficas
    plt.tight_layout()
    plt.show()