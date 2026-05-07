import cv2
import numpy as np

def HoughCircle(img_bgr):
    resultado = img_bgr.copy()
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=45,
        param1=100,
        param2=28,
        minRadius=8,
        maxRadius=120
    )

    conteo = 0

    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)

        for (x, y, r) in circles:
            conteo += 1
            cv2.circle(resultado, (x, y), r, (0, 255, 0), 2)
            cv2.circle(resultado, (x, y), 2, (0, 0, 255), 3)

    return conteo, resultado