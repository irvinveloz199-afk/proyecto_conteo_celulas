import cv2
import numpy as np
from scipy import signal

# Función para convertir imágenes a escala de grises mediante pesos de luminosidad
# mode=1: Formato BGR (OpenCV) | mode=0: Formato RGB
def grey(img, mode=1):
    if mode == 1:
        b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    else:
        r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    # Aplicación de la fórmula estándar de luminancia
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray.astype(np.uint8)


# Detector de bordes Sobel mediante aproximación de gradientes
# Calcula la derivada espacial en X y Y para hallar la magnitud del borde
def Sobel(img):
    # Kernels de aproximación de derivadas (horizontal y vertical)
    kernel_sx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    kernel_sy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    # Convolución para obtener las componentes del gradiente
    edges_x = signal.convolve2d(img, kernel_sx, mode="same")
    edges_y = signal.convolve2d(img, kernel_sy, mode="same")

    # Cálculo de la magnitud euclidiana del gradiente
    sobel = np.sqrt(edges_x**2 + edges_y**2)
    
    # Normalización del resultado al rango de 8 bits (0-255)
    sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)

    return sobel.astype(np.uint8)


# Algoritmo Canny para detección de bordes multietapa
# Incluye suavizado, gradiente y filtrado por histéresis
def Canny(img, k=5, sigma=1.2, low=40, high=120):
    # Suavizado Gaussiano para reducción de ruido de alta frecuencia
    blur = cv2.GaussianBlur(img, (k, k), sigma)

    # Aplicación del operador Canny para bordes delgados y binarios
    canny = cv2.Canny(blur, low, high)

    return canny


# Filtro Pasa-Banda en el dominio de la frecuencia mediante FFT
# Selecciona un rango de frecuencias circulares (anillo) en el espectro
def BandPass(img, freq=30, dist=20):
    # Obtención de dimensiones y centro de la imagen
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    # Creación de máscara circular (anillo de paso)
    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), freq, 1, dist)

    # Transformada Rápida de Fourier (FFT) y desplazamiento de frecuencia
    fft = np.fft.fft2(img)
    fftshift = np.fft.fftshift(fft)

    # Aplicación del filtrado espectral
    fft_filt = fftshift * mask

    # Transformada inversa para regresar al dominio espacial
    reg = np.fft.ifftshift(fft_filt)
    reg = np.fft.ifft2(reg)
    
    # Magnitud y normalización de la imagen reconstruida
    img_filt = cv2.normalize(np.abs(reg), None, 0, 255, cv2.NORM_MINMAX)

    return img_filt.astype(np.uint8)


# Transformación logarítmica de intensidad para realce de contraste
# Mejora la visibilidad de detalles en zonas de baja intensidad
def Logarithmic(img, c=1):
    # Operación sobre valores flotantes para evitar saturación
    img_f = img.astype(np.float32)

    # Transformación no lineal (compresión de rango dinámico)
    log_img = np.log(c + img_f)

    # Control de división entre cero si la imagen es constante
    if log_img.max() - log_img.min() == 0:
        return img.astype(np.uint8)

    # Reescalado lineal al rango 0-255
    log_img = (log_img - log_img.min()) / (log_img.max() - log_img.min())
    
    return np.round(log_img * 255).astype(np.uint8)