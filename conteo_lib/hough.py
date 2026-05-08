import cv2
import numpy as np

# Algoritmo de supresión para eliminar círculos redundantes o solapados
# Utiliza un criterio de proximidad basado en el radio para seleccionar la mejor detección
def filtrar_circulos(circulos):
    if len(circulos) == 0:
        return []

    # Ordenamiento descendente por radio para priorizar estructuras de mayor escala
    circulos = sorted(circulos, key=lambda c: c[2], reverse=True)

    filtrados = []

    for (x, y, r) in circulos:
        repetido = False

        # Comparación mediante distancia euclidiana entre centros de círculos
        for (xf, yf, rf) in filtrados:
            distancia = np.sqrt((x - xf) ** 2 + (y - yf) ** 2)

            # Criterio de umbral: si el centro está dentro del 65% del radio de un círculo ya aceptado
            if distancia < rf * 0.65:
                repetido = True
                break

        if not repetido:
            filtrados.append((x, y, r))

    return filtrados


# Detección de estructuras circulares mediante la Transformada de Hough (Gradiente)
# Implementa un enfoque multiescala para capturar células de diversos diámetros
def HoughCircle(img_bgr):
    # Generación de lienzos para visualización y segmentación binaria
    resultado = img_bgr.copy()
    mask = np.zeros(img_bgr.shape[:2], dtype=np.uint8)

    # Preprocesamiento: conversión a grises y suavizado Gaussiano para reducir falsos gradientes
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 2)

    # Cálculo de métricas proporcionales al tamaño de la imagen de entrada
    alto, ancho = gray.shape
    min_dim = min(alto, ancho)

    candidatos = []

    # Diccionarios de hiperparámetros para tres escalas: Pequeña, Mediana y Grande
    # param2 es el umbral del acumulador: valores más altos exigen formas más circulares
    configuraciones = [
        {
            "minDist": 25,
            "param1": 100,
            "param2": 34,
            "minRadius": max(6, int(min_dim * 0.025)),
            "maxRadius": max(20, int(min_dim * 0.10))
        },
        {
            "minDist": 45,
            "param1": 100,
            "param2": 36,
            "minRadius": max(18, int(min_dim * 0.08)),
            "maxRadius": max(50, int(min_dim * 0.22))
        },
        {
            "minDist": 70,
            "param1": 100,
            "param2": 40,
            "minRadius": max(40, int(min_dim * 0.18)),
            "maxRadius": max(80, int(min_dim * 0.35))
        }
    ]

    # Iteración sobre las escalas para poblar el espacio de búsqueda
    for cfg in configuraciones:
        circles = cv2.HoughCircles(
            blur,
            cv2.HOUGH_GRADIENT,
            dp=1.2, # Resolución del acumulador (inversa)
            minDist=cfg["minDist"],
            param1=cfg["param1"],
            param2=cfg["param2"],
            minRadius=cfg["minRadius"],
            maxRadius=cfg["maxRadius"]
        )

        if circles is not None:
            circles = np.round(circles[0, :]).astype(int)

            for (x, y, r) in circles:
                # Validación de fronteras para evitar errores de indexación
                if 0 <= x < ancho and 0 <= y < alto:
                    candidatos.append((x, y, r))

    # Ejecución de la lógica de filtrado para consolidar detecciones únicas
    circulos = filtrar_circulos(candidatos)

    conteo = 0

    # Marcado gráfico de las detecciones validadas
    for (x, y, r) in circulos:
        conteo += 1

        # Representación de la circunferencia estimada
        cv2.circle(resultado, (x, y), r, (0, 255, 0), 2)

        # Representación del centroide de la célula
        cv2.circle(resultado, (x, y), 2, (0, 0, 255), 3)

        # Generación de máscara de segmentación (relleno sólido)
        cv2.circle(mask, (x, y), r, 255, -1)

    return conteo, resultado, mask