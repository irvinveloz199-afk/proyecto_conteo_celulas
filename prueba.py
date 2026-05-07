import cv2
import matplotlib.pyplot as plt

from conteo_lib.conteo import Pipeline_Celulas
from conteo_lib.hough import HoughCircle

img = cv2.imread("test.jpg")

if img is None:
    print("No se encontró test.jpg")
else:
    total, resultado, sobel, canny, mask_blue, otsu = Pipeline_Celulas(img)

    total_hough, img_hough = HoughCircle(img)

    print("Células detectadas:", total)
    print("Círculos Hough detectados:", total_hough)

    plt.figure(figsize=(16, 9))

    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
    plt.title(f"Conteo final: {total}")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(mask_blue, cmap="gray")
    plt.title("Segmentación azul")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(canny, cmap="gray")
    plt.title("Canny")
    plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.imshow(cv2.cvtColor(img_hough, cv2.COLOR_BGR2RGB))
    plt.title("Hough")
    plt.axis("off")

    plt.tight_layout()
    plt.show()