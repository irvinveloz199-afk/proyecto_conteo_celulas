import numpy as np

def umbral_manual(imagen_gris, valor_umbral=127):
    """
    Convierte la imagen a blanco y negro puro (binaria).
    Píxeles arriba del umbral -> Blanco (255)
    Píxeles abajo del umbral -> Negro (0)
    """
    # Creamos una matriz de ceros (negra) del mismo tamaño
    binaria = np.zeros_like(imagen_gris)
    
    # Donde la imagen original sea mayor al umbral, ponemos blanco
    # Esto es una operación de máscara mucho más rápida que un ciclo for
    binaria[imagen_gris > valor_umbral] = 255
    
    return binaria.astype(np.uint8)