import cv2
import numpy as np

# Segmentación binarizada mediante el método de umbralización global de Otsu
# Calcula automáticamente el umbral óptimo minimizando la varianza intraclase
def Otsu(img):
    # El valor 0 se ignora ya que THRESH_OTSU determina el valor crítico de forma estadística
    _, th = cv2.threshold(
        img,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return th


# Segmentación por color mediante el modelo de color HSV
# Aísla estructuras (células) basándose en rangos específicos de saturación y matiz
def ColorSegmentation(img_bgr):
    # Conversión a HSV para desacoplar la información de luminancia del color (croma)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # Definición de rangos para segmentar núcleos y membranas (azules y violetas)
    mask_blue = cv2.inRange(
        hsv,
        np.array([80, 20, 20]),
        np.array([145, 255, 255])
    )

    # Definición de rangos para tonos magenta y rojizos (citoplasmas)
    mask_pink1 = cv2.inRange(
        hsv,
        np.array([135, 20, 30]),
        np.array([179, 255, 255])
    )

    # Segundo rango para tonos rojos (debido a la circularidad del canal Hue en HSV)
    mask_pink2 = cv2.inRange(
        hsv,
        np.array([0, 20, 30]),
        np.array([15, 255, 255])
    )

    # Unión lógica (OR) de todas las máscaras de color generadas
    mask = mask_blue | mask_pink1 | mask_pink2

    # Kernel estructurante para procesos de morfología matemática
    kernel = np.ones((5, 5), np.uint8)

    # Filtro de mediana para eliminación de ruido tipo sal y pimienta
    mask = cv2.medianBlur(mask, 5)

    # Operación de Apertura (Erosión seguida de Dilatación) para eliminar objetos pequeños
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # Operación de Cierre (Dilatación seguida de Erosión) para rellenar huecos internos
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    return mask