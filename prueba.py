import cv2
import matplotlib.pyplot as plt

from conteo_lib.conteo import Pipeline_Celulas
from conteo_lib.hough import HoughCircle
from conteo_lib.filtros import Sobel, Canny, BandPass, Logarithmic


img = cv2.imread("test.jpg")

if img is None:
    print("No se encontró test.jpg")

else:
    # Pipeline principal de conteo
    total, resultado, sobel, canny, mask_blue, otsu = Pipeline_Celulas(img)

    # Hough
    total_hough, img_hough = HoughCircle(img)

    # Imagen gris para técnicas adicionales
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Filtrado en frecuencia
    bandpass = BandPass(gray, freq=30, dist=20)

    # Transformación de intensidad
    log_img = Logarithmic(gray, c=1)

    print("Células detectadas:", total)
    print("Círculos Hough detectados:", total_hough)

    plt.figure(figsize=(16, 10))

    # Conteo final
    plt.subplot(2, 4, 1)
    plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
    plt.title(f"Conteo final: {total}")
    plt.axis("off")

    # Segmentación azul
    plt.subplot(2, 4, 2)
    plt.imshow(mask_blue, cmap="gray")
    plt.title("Segmentación azul")
    plt.axis("off")

    # Imagen original
    plt.subplot(2, 4, 3)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
    plt.axis("off")

    # Hough
    plt.subplot(2, 4, 4)
    plt.imshow(cv2.cvtColor(img_hough, cv2.COLOR_BGR2RGB))
    plt.title("Hough")
    plt.axis("off")

    # Sobel
    plt.subplot(2, 4, 5)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel")
    plt.axis("off")

    # Canny
    plt.subplot(2, 4, 6)
    plt.imshow(canny, cmap="gray")
    plt.title("Canny")
    plt.axis("off")

    # BandPass
    plt.subplot(2, 4, 7)
    plt.imshow(bandpass, cmap="gray")
    plt.title("Filtro en frecuencia")
    plt.axis("off")

    # Logarítmica
    plt.subplot(2, 4, 8)
    plt.imshow(log_img, cmap="gray")
    plt.title("Transformación log")
    plt.axis("off")

    plt.tight_layout()
    plt.show()