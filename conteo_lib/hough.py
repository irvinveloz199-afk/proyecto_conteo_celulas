import cv2
import numpy as np
#Aqui usamos el hough para detectar círculos.
#La imagen se convierte a escala de grises porque Hough detecta formas a partir de intensidad y bordes.

# Esta función recibe todos los círculos detectados por Hough y elimina los que están repetidos o demasiado 
# cerca de otro círculo ya aceptado. Esto evita contar dos veces la misma célula.”
def filtrar_circulos(circulos):
    if len(circulos) == 0:
        return []

    # Ordenamiento descendente por radio para priorizar estructuras de mayor escala
    circulos = sorted(circulos, key=lambda c: c[2], reverse=True)

    filtrados = []

    for (x, y, r) in circulos:
        repetido = False

        # Comparación mediante distancia entre centros de círculos
        for (xf, yf, rf) in filtrados:
            distancia = np.sqrt((x - xf) ** 2 + (y - yf) ** 2)

            # Criterio de umbral: si el centro está dentro del 65% del radio de un círculo ya aceptado
            if distancia < rf * 0.65:
                repetido = True
                break

        if not repetido:
            filtrados.append((x, y, r))

    return filtrados


#Esta función implementa la Transformada de Hough para detectar células con forma aproximadamente circular.
def HoughCircle(img_bgr):
#Creamaos los resultados junto con la mascara 
#Creamos una copia de la imagen original para visualizar las detecciones 
# y una máscara binaria para representar las células detectadas.
    resultado = img_bgr.copy()
    mask = np.zeros(img_bgr.shape[:2], dtype=np.uint8)

#Aqui aplicamos un suavizado Gaussiano para reducir ruido antes de ejecutar Hough.
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 2)

    # Cálculo de métricas proporcionales al tamaño de la imagen de entrada
    alto, ancho = gray.shape
    min_dim = min(alto, ancho)
#Aquí se almacenamos temporalmente todas las detecciones circulares.
    candidatos = []

#Implementamos una estrategia multiescala para detectar distintos tamaños celulares.
    configuraciones = [
        {
            "minDist": 25,#Controla la distancia mínima entre centros de círculos.
            "param1": 100,#Controla la intensidad de los bordes usados para detectar círculos
            "param2": 34,#param2 controla la sensibilidad de la detección circular
            "minRadius": max(6, int(min_dim * 0.025)),#Definimos un tamaño minimo Para evitar ruido 
            "maxRadius": max(20, int(min_dim * 0.10))# y aqui el maximo para evitar falsos positivos.
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

#Aqui ejecutamos el algoritmo Hough múltiples veces para detectar distintos tamaños celulares.
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
    circulos = filtrar_circulos(candidatos)#Las detecciones válidas se almacenan como candidatos para su posterior filtrado.

    conteo = 0

# Marcado gráfico de las detecciones validadas
    for (x, y, r) in circulos:
        conteo += 1

#Se dibuja una circunferencia verde para visualizar la detección celular.
        cv2.circle(resultado, (x, y), r, (0, 255, 0), 2)

#También se marca el centro de cada célula detectada.
        cv2.circle(resultado, (x, y), 2, (0, 0, 255), 3)

#En la máscara binaria, se rellena un círculo blanco para representar cada célula detectada.
        cv2.circle(mask, (x, y), r, 255, -1)

    return conteo, resultado, mask