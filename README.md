# Proyecto Conteo de Células

Librería en Python para el conteo automático de células en imágenes microscópicas mediante técnicas de procesamiento digital de imágenes.

---

# Descripción

Este proyecto implementa una librería capaz de procesar imágenes microscópicas para detectar, segmentar y contar células. El sistema utiliza técnicas de preprocesamiento, filtrado espacial y en frecuencia, detección de bordes, umbralización, segmentación por regiones y transformada de Hough para estructuras aproximadamente circulares.

El proyecto fue desarrollado como parte de la materia de procesamiento digital de imágenes.

---

# Objetivo general

Diseñar e implementar una librería en Python para el conteo automático de células en imágenes microscópicas, integrando técnicas de preprocesamiento, segmentación y detección de características.

---

# Técnicas implementadas

- Conversión de imagen RGB/BGR a escala de grises
- Filtrado espacial Gaussiano
- Filtrado en frecuencia mediante filtro pasa banda
- Transformación logarítmica de intensidad
- Detección de bordes con Sobel
- Detección de bordes con Canny
- Segmentación basada en color HSV
- Umbralización
- Conteo mediante componentes conectados
- Transformada de Hough para detección de círculos
- Visualización de resultados con Matplotlib

---

# Temas integrados

- Point, line and edge detection
- Thresholding
- Region-based segmentation
- Hough transform
- Preprocesamiento de imágenes

---

# Estructura del proyecto

```text
proyecto_conteo_celulas/
│
├── conteo_lib/
│   ├── __init__.py
│   ├── conteo.py
│   ├── filtros.py
│   ├── hough.py
│   └── segmentacion.py
│
├── prueba.py
├── test.jpg
├── README.md
├── pyproject.toml
└── .gitignore
```

---

# Requisitos

Para ejecutar el proyecto se necesitan las siguientes librerías:

```bash
pip install opencv-python numpy matplotlib scipy
```

---

# Instalación

Clona el repositorio:

```bash
git clone https://github.com/irvinveloz199-afk/proyecto_conteo_celulas.git
```

Entra a la carpeta del proyecto:

```bash
cd proyecto_conteo_celulas
```

Instala las dependencias:

```bash
pip install opencv-python numpy matplotlib scipy
```

También es posible instalar el proyecto directamente desde GitHub:

```bash
pip install git+https://github.com/irvinveloz199-afk/proyecto_conteo_celulas.git
```

---

# Uso

Ejecuta el script principal:

```bash
python prueba.py
```

---

# Funcionamiento general

El programa realiza el siguiente flujo:

1. Carga la imagen microscópica.
2. Convierte la imagen a escala de grises.
3. Aplica filtrado espacial y filtrado en frecuencia.
4. Aplica transformación logarítmica.
5. Detecta bordes mediante Sobel y Canny.
6. Segmenta las células usando color azul en HSV.
7. Detecta componentes conectados.
8. Cuenta las células detectadas.
9. Muestra resultados intermedios y finales.

---

# Salida esperada

Al ejecutar `prueba.py`, el programa muestra:

- Conteo final de células
- Segmentación azul
- Imagen original
- Resultado Sobel
- Resultado Canny
- Resultado del filtro en frecuencia
- Resultado de transformación logarítmica
- Resultado de Hough

Además, en consola se imprime el número de células detectadas.

---

# Resultados

El sistema detecta correctamente la mayoría de las células visibles en la imagen de prueba, incluyendo células pequeñas y parcialmente visibles.

El conteo final se realiza mediante segmentación basada en color y componentes conectados, mientras que la transformada de Hough se utiliza como técnica complementaria para detección de formas circulares.

---

# Limitaciones

El algoritmo puede presentar errores cuando:

- Las células están parcialmente fuera de la imagen.
- Existen reflejos o sombras.
- Las células tienen colores muy similares al fondo.
- Las células están superpuestas.
- Las estructuras no son completamente circulares.
- La iluminación de la imagen cambia significativamente.

---

# Requerimientos técnicos cumplidos

- Conversión RGB a escala de grises
- Filtrado espacial
- Filtrado en frecuencia
- Transformación de intensidad
- Detección de bordes
- Umbralización
- Segmentación
- Conteo automático de células

---

# Autores
Integrantes:

- Irvin Bladimir Veloz Briones
- Joshua Natanael Alarcon Hernandez
- Jonathan Padilla Alvarado 

---

# Estado del proyecto

Proyecto funcional para detección, segmentación y conteo automático de células en imágenes microscópicas.
