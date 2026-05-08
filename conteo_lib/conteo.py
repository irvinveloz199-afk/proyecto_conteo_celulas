import cv2
import numpy as np

from .filtros import grey, Sobel, Canny
from .segmentacion import ColorSegmentation, Otsu
from .hough import HoughCircle

# Aqui lo que hacemos es filtrar objetos por área, relación de aspecto y ubicación de centroides
def CountCells(img_bgr, mask):
    # Obtención de estadísticas de la máscara binaria
    # Retorna: cantidad de etiquetas, mapa de etiquetas, estadísticas de bounding box y centroides
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, 8)

    # Lienzo para la representación gráfica de las detecciones validadas
    resultado = img_bgr.copy()

    conteo = 0

    # Dimensiones de referencia para normalización de filtros de área
    h_img, w_img = mask.shape

    # Umbral de área mínima (0.008%) para discriminación de ruido impulsivo
    area_min = int(0.00008 * h_img * w_img)

    # Umbral de área máxima (35%) para evitar falsos positivos por regiones de fondo o artefactos
    area_max = int(0.35 * h_img * w_img)

    # Iteración sobre los componentes detectados (omitiendo la etiqueta 0, que es el fondo)
    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]

        # Filtro de densidad: descarta objetos por debajo del umbral de resolución
        if area < area_min:
            continue

        # Filtro de saturación: descarta masas excesivamente grandes que no corresponden a células
        if area > area_max:
            continue

        # Cálculo del ratio de aspecto (Bounding Box Aspect Ratio)
        # Permite evaluar la excentricidad de la forma detectada
        ratio = w / h if h != 0 else 0

        # Filtro morfológico: acepta objetos con formas compactas, circulares u ovaladas
        if 0.20 < ratio < 5.0:
            conteo += 1

            # Recuperación del centroide calculado estadísticamente
            cx, cy = centroids[i]

            # Representación del Bounding Box (Rectángulo contenedor)
            cv2.rectangle(resultado, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Representación del centroide calculado (Punto de anclaje)
            cv2.circle(resultado, (int(cx), int(cy)), 3, (0, 0, 255), -1)

            # Etiquetado numérico secuencial en el plano de salida
            cv2.putText(
                resultado,
                str(conteo),
                (x, max(y - 5, 15)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1
            )

    return conteo, resultado


# Implementa una lógica de conmutación basada en la calidad de la segmentación
def Pipeline_Celulas(img_bgr):
    # Etapa 1: Preprocesamiento y extracción de características (Bordes)
    gray = grey(img_bgr, mode=1)
    sobel = Sobel(gray)
    canny = Canny(gray)

    # Etapa 2: Segmentación por croma (HSV) y análisis de componentes conectados
    mask_color = ColorSegmentation(img_bgr)
    total_color, resultado_color = CountCells(img_bgr, mask_color)

    # Etapa 3: Detección geométrica mediante Transformada de Hough
    total_hough, resultado_hough, mask_hough = HoughCircle(img_bgr)

    # Etapa 4: Análisis de ocupación espacial de la máscara de color
    h, w = mask_color.shape
    area_blanca = np.sum(mask_color == 255) / (h * w)

    # Etapa 5: Lógica de decisión heurística
    # Se prioriza la segmentación por color si el conteo es significativo y la densidad es lógica
    # De lo contrario, se recurre a la robustez geométrica de la Transformada de Hough
    if total_color >= 5 and area_blanca < 0.28:
        total = total_color
        resultado = resultado_color
        mask = mask_color
    else:
        total = total_hough
        resultado = resultado_hough
        mask = mask_hough

    # Etapa 6: Generación de evidencia de umbralización global (Otsu)
    otsu = Otsu(gray)

    return total, resultado, sobel, canny, mask, otsu