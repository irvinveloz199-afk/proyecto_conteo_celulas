import cv2
import numpy as np

from .filtros import grey, Sobel, Canny
from .segmentacion import BlueSegmentation, Otsu

def CountBlueCells(img_bgr, mask, area_min=40, area_max=60000):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, 8)

    resultado = img_bgr.copy()
    conteo = 0

    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]

        if area < area_min or area > area_max:
            continue

        ratio = w / h if h != 0 else 0

        # Acepta células circulares y parcialmente cortadas
        if 0.25 < ratio < 4.0:
            conteo += 1

            cx, cy = centroids[i]

            cv2.rectangle(resultado, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(resultado, (int(cx), int(cy)), 3, (0, 0, 255), -1)
            cv2.putText(
                resultado,
                str(conteo),
                (x, y-5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1
            )

    return conteo, resultado

def Pipeline_Celulas(img_bgr):
    gray = grey(img_bgr, mode=1)

    sobel = Sobel(gray)
    canny = Canny(gray)

    mask_blue = BlueSegmentation(img_bgr)

    otsu = Otsu(gray)

    total, resultado = CountBlueCells(
        img_bgr,
        mask_blue,
        area_min=40,
        area_max=60000
    )

    return total, resultado, sobel, canny, mask_blue, otsu