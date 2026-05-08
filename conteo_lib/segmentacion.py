import cv2
import numpy as np

# Imagen original
#→ detectar colores celulares
#→ convertirlos en blanco
#→ convertir fondo en negro

def Otsu(img):
    # El valor 0 se ignora ya que THRESH_OTSU determina el valor crítico de forma estadística
    _, th = cv2.threshold(
        img,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return th

#Usameos HSV separa el color del brillo.
# En Rgb el brillo afecta a los valores de los canales, mientras que en HSV el canal de matiz (Hue) se mantiene relativamente constante para un color dado, independientemente de su luminosidad. Esto permite segmentar colores específicos con mayor precisión, incluso en condiciones de iluminación variables.

     # Segmentación por color mediante el modelo de color HSV
     # Aísla estructuras (células) basándose en rangos específicos de saturación y matiz
def ColorSegmentation(img_bgr):
    # Conversión a HSV para desacoplar la información de luminancia del color (croma)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)


#Aquí definimos colores azulados y morados que suelen aparecer en células microscópicas.
    # Definición de rangos para segmentar núcleos y membranas (azules y violetas)
    mask_blue = cv2.inRange(
        hsv,
        np.array([80, 20, 20]),
        np.array([145, 255, 255])
    )

#También se detectan tonos rosados y magenta para adaptarse a distintos tipos de imágenes.
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

#Aqui unimos todas las máscaras para obtener una sola imagen binaria con todas las posibles células.
    mask = mask_blue | mask_pink1 | mask_pink2

    # Kernel estructurante para procesos de morfología matemática
    kernel = np.ones((5, 5), np.uint8)

# Filtro de mediana para reducir el ruido pequeño que podría confundirse con células.
    mask = cv2.medianBlur(mask, 5)

#La apertura elimina pequeñas manchas.
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

# Operación de Cierre para rellenar huecos internos
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    return mask