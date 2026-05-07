import cv2
import numpy as np
from scipy import signal

def grey(img, mode=1):
    if mode == 1:  # BGR
        b = img[:, :, 0]
        g = img[:, :, 1]
        r = img[:, :, 2]
    else:          # RGB
        r = img[:, :, 0]
        g = img[:, :, 1]
        b = img[:, :, 2]

    gray = 0.2989*r + 0.5870*g + 0.1140*b
    return gray.astype(np.uint8)

def Gauss(img, k=5, sigma=1.2):
    return cv2.GaussianBlur(img, (k, k), sigma)

def Sobel(img):
    kernel_sx = np.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]], dtype=np.float32)

    kernel_sy = np.array([[ 1,  2,  1],
                          [ 0,  0,  0],
                          [-1, -2, -1]], dtype=np.float32)

    dx = signal.convolve2d(img, kernel_sx, mode='same')
    dy = signal.convolve2d(img, kernel_sy, mode='same')

    sobel = np.sqrt(dx**2 + dy**2)
    sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)

    return sobel.astype(np.uint8)

def Canny(img, k=5, sigma=1.2, low=40, high=120):
    blur = cv2.GaussianBlur(img, (k, k), sigma)
    return cv2.Canny(blur, low, high)