##Parte 1:

import numpy as np

def aplicar_convolucion(imagen, kernel):
    """
    Función para aplicar un filtro (kernel) de forma manual.
    Esto cumple con la restricción de 'Implementación propia'.
    """
    # 1. Obtener dimensiones de la imagen y el kernel
    img_h, img_w = imagen.shape
    k_h, k_w = kernel.shape
    
    # 2. Padding: Agregamos un borde negro para que el kernel pueda
    # pasar por los píxeles de las orillas sin salirse.
    pad = k_h // 2
    img_padded = np.pad(imagen, ((pad, pad), (pad, pad)), mode='constant')
    
    # 3. Crear imagen de salida (vacía por ahora)
    salida = np.zeros((img_h, img_w), dtype=np.float32)
    
    # 4. Los dos ciclos FOR: Recorremos cada píxel de la imagen
    for i in range(img_h):
        for j in range(img_w):
            # Extraemos la vecindad (el pedacito de imagen donde cae el kernel)
            region = img_padded[i : i + k_h, j : j + k_w]
            
            # Multiplicamos la región por el kernel y sumamos todo
            salida[i, j] = np.sum(region * kernel)
            
    return salida

##Parte 2:

def filtro_sobel(imagen_gris):
    """
    Detecta bordes usando el operador Sobel.
    """
    # Estos son los Kernels que vienen en el código del profe
    kernel_sx = np.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]], dtype=np.float32)

    kernel_sy = np.array([[ 1,  2,  1],
                          [ 0,  0,  0],
                          [-1, -2, -1]], dtype=np.float32)

    # USAMOS NUESTRA FUNCIÓN MANUAL en lugar de cv2 o signal
    bordes_x = aplicar_convolucion(imagen_gris, kernel_sx)
    bordes_y = aplicar_convolucion(imagen_gris, kernel_sy)

    # Calculamos la magnitud del gradiente (combinar X y Y)
    # Esto es igual a: sqrt(Gx^2 + Gy^2)
    sobel = np.sqrt(bordes_x**2 + bordes_y**2)
    
    # Normalizamos para que los píxeles estén entre 0 y 255
    sobel = (sobel / sobel.max() * 255).astype(np.uint8)
    
    return sobel