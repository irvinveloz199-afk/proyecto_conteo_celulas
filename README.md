# Proyecto Conteo de Células

Librería en Python para el conteo automático de células en imágenes microscópicas mediante técnicas de procesamiento digital de imágenes.

---

# Descripción

Este proyecto implementa una librería capaz de procesar imágenes microscópicas para detectar, segmentar y contar células. El sistema utiliza técnicas de preprocesamiento, detección de bordes, umbralización, segmentación por regiones y transformada de Hough para estructuras aproximadamente circulares.

---

# Técnicas implementadas

- Conversión de imagen RGB/BGR a escala de grises
- Filtrado espacial mediante suavizado Gaussiano
- Detección de bordes con Sobel
- Detección de bordes con Canny
- Segmentación mediante umbralización
- Segmentación por color azul en espacio HSV
- Conteo de regiones mediante componentes conectados
- Transformada de Hough para detección de círculos
- Visualización de resultados con Matplotlib

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
└── .gitignore
```

---

# Requisitos

Para ejecutar el proyecto se necesitan las siguientes librerías:

```bash
pip install opencv-python numpy matplotlib scipy
```

---

# Uso

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

Ejecuta el script de prueba:

```bash
python prueba.py
```

---

# Funcionamiento general

El programa realiza el siguiente flujo:

1. Carga la imagen microscópica.
2. Convierte la imagen a escala de grises.
3. Aplica técnicas de filtrado y detección de bordes.
4. Segmenta las células usando el color azul característico.
5. Detecta regiones conectadas.
6. Cuenta las células encontradas.
7. Muestra imágenes intermedias y el resultado final.

---

# Salida esperada

Al ejecutar `prueba.py`, el programa muestra una ventana con:

- Imagen original
- Imagen con conteo final
- Segmentación azul
- Resultado de Sobel
- Resultado de Canny
- Resultado de Hough

Además, en consola se imprime el número de células detectadas.

---

# Limitaciones

El algoritmo puede presentar errores cuando:

- Las células están parcialmente fuera de la imagen.
- Existen reflejos o sombras.
- Las células tienen colores muy similares al fondo.
- Las células están superpuestas.
- Las estructuras no son claramente circulares.

---

# Autores

Proyecto desarrollado para la materia de procesamiento de imágenes.

Integrantes:

- Irvin Bladimir Veloz Briones
- Joshua Natanael Alarcon Hernandez
- Jonathan Padilla Alvarado 

---

# Estado del proyecto

Proyecto funcional para detectar, segmentar y contar células en imágenes microscópicas de prueba.
