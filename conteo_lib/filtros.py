import cv2
import numpy as np
from scipy import signal


# Conversión a escala de grises
def grey(img, mode=1):
    if mode == 1:  # BGR, formato usado por OpenCV
        b = img[:, :, 0]
        g = img[:, :, 1]
        r = img[:, :, 2]
    else:  # RGB
        r = img[:, :, 0]
        g = img[:, :, 1]
        b = img[:, :, 2]

    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray.astype(np.uint8)


# Filtro espacial gaussiano
def Gauss(img, k=5, sigma=1.2):
    return cv2.GaussianBlur(img, (k, k), sigma)


# Detección de bordes Sobel
def Sobel(img):
    kernel_sx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_sy = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ], dtype=np.float32)

    dx = signal.convolve2d(img, kernel_sx, mode="same")
    dy = signal.convolve2d(img, kernel_sy, mode="same")

    sobel = np.sqrt(dx**2 + dy**2)
    sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)

    return sobel.astype(np.uint8)


# Detección de bordes Canny
def Canny(img, k=5, sigma=1.2, low=40, high=120):
    blur = cv2.GaussianBlur(img, (k, k), sigma)
    return cv2.Canny(blur, low, high)


# Filtrado en frecuencia: filtro pasa banda
def BandPass(img, freq=30, dist=20):
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), freq, 1, dist)

    fft = np.fft.fft2(img)
    fftshift = np.fft.fftshift(fft)

    fft_filt = fftshift * mask

    reg = np.fft.ifftshift(fft_filt)
    reg = np.fft.ifft2(reg)

    img_filt = np.abs(reg)
    img_filt = cv2.normalize(img_filt, None, 0, 255, cv2.NORM_MINMAX)

    return img_filt.astype(np.uint8)


# Transformación de intensidad: logarítmica
def Logarithmic(img, c=1):
    img_f = img.astype(np.float32)

    log_img = np.log(c + img_f)

    log_img = (log_img - log_img.min()) / (log_img.max() - log_img.min())
    log_img = np.round(log_img * 255)

    return log_img.astype(np.uint8)