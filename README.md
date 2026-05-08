# Librería de Conteo de Células en Imágenes Microscópicas

Proyecto desarrollado en Python para la detección, segmentación y conteo automático de células en imágenes microscópicas utilizando técnicas de procesamiento digital de imágenes.

---

# Objetivo del Proyecto

Diseñar e implementar una librería en Python capaz de:

- Procesar imágenes microscópicas.
- Detectar células automáticamente.
- Segmentar regiones celulares.
- Contar células presentes en la imagen.
- Aplicar técnicas de procesamiento digital de imágenes vistas en clase.

---

# Técnicas Implementadas

El proyecto integra diferentes técnicas de visión artificial y procesamiento digital de imágenes:

## Preprocesamiento
- Conversión a escala de grises.
- Suavizado Gaussiano.
- Reducción de ruido.

## Detección de bordes
- Sobel.
- Canny.

## Umbralización
- Método de Otsu.

## Segmentación
- Segmentación por color en espacio HSV.
- Componentes conectados.

## Detección de formas
- Transformada de Hough para detección de círculos.

## Procesamiento adicional
- Filtro en frecuencia usando FFT.
- Transformación logarítmica.

---

# Estructura del Proyecto

```text
proyecto_conteo_celulas/
│
├── conteo_lib/
│   ├── filtros.py
│   ├── segmentacion.py
│   ├── hough.py
│   └── conteo.py
│
├── test1.jpg
├── test2.jpg
├── test3.jpg
├── test4.jpg
├── test5.jpg
│
├── prueba.py
├── README.md
└── pyproject.toml
```

---

# Explicación de Archivos

## `filtros.py`
Contiene funciones de preprocesamiento:

- Escala de grises.
- Sobel.
- Canny.
- FFT.
- Transformación logarítmica.

---

## `segmentacion.py`
Contiene funciones de:

- Umbralización Otsu.
- Segmentación por color HSV.
- Limpieza morfológica.

---

## `hough.py`
Implementa:

- Transformada de Hough.
- Filtrado de círculos repetidos.
- Detección multiescala.

---

## `conteo.py`
Archivo principal de procesamiento.

Incluye:

- Conteo por componentes conectados.
- Pipeline completo.
- Selección automática entre segmentación y Hough.

---

## `prueba.py`
Archivo de pruebas y visualización.

Permite:
- Cambiar la imagen de prueba.
- Mostrar resultados del procesamiento.
- Visualizar filtros y detecciones.

---

# Instalación

## Crear entorno virtual (opcional)

```bash
python -m venv .venv
```

## Activar entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# Instalación de Dependencias

```bash
pip install opencv-python numpy scipy matplotlib
```

---

# Ejecución del Proyecto

Para ejecutar el programa:

```bash
python prueba.py
```

---

# Uso de Imágenes de Prueba

El proyecto incluye 5 imágenes de prueba:

- `test1.jpg`
- `test2.jpg`
- `test3.jpg`
- `test4.jpg`
- `test5.jpg`

Para cambiar la imagen analizada, modificar la siguiente línea dentro de `prueba.py`:

```python
imagen = "test1.jpg"
```

Por ejemplo:

```python
imagen = "test3.jpg"
```

---

# Resultados Mostrados

El programa genera una ventana con:

1. Conteo final.
2. Segmentación / máscara.
3. Imagen original.
4. Detección Hough.
5. Sobel.
6. Canny.
7. Filtro en frecuencia.
8. Transformación logarítmica.

---

# Funcionamiento General

El pipeline principal funciona de la siguiente manera:

```text
Imagen original
→ Escala de grises
→ Sobel y Canny
→ Segmentación HSV
→ Conteo por regiones
→ Hough como respaldo
→ Selección automática del mejor método
→ Conteo final
```

---

# Selección Automática de Método

El sistema evalúa automáticamente si la segmentación por color es confiable.

- Si la máscara tiene buena calidad:
  - se usa segmentación por color.

- Si la máscara falla o detecta demasiadas regiones:
  - se utiliza la Transformada de Hough.

Esto permite mayor robustez ante diferentes tipos de imágenes.

---

# Parámetros Ajustables

Durante pruebas o presentación se pueden modificar:

## En `prueba.py`

```python
imagen = "test1.jpg"
```

Para cambiar la imagen.

---

## En `conteo.py`

```python
if total_color >= 5 and area_blanca < 0.28:
```

El valor `0.28` controla cuándo usar segmentación o Hough.

---

## En `hough.py`

```python
param2
```

Controla la sensibilidad de Hough.

- Más alto → menos círculos falsos.
- Más bajo → detecta más círculos.

---

# Limitaciones

El sistema funciona mejor en imágenes:

- con buen contraste,
- células aproximadamente circulares,
- poco ruido,
- y pocas superposiciones.

En imágenes con:
- células muy recortadas,
- bajo contraste,
- o demasiadas células superpuestas,

el conteo puede variar.

---

# Tecnologías Utilizadas

- Python
- OpenCV
- NumPy
- SciPy
- Matplotlib

---

# Integrantes

- Irvin Bladimir Veloz Briones
- Joshua Natanael Alarcón Hernández
- Jonathan Padilla Alvarado 

---

# Materia

Vision Robotica 

---


