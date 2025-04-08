import os
import random
import string

def generar_texto_aleatorio(longitud=100):
    """Genera un texto aleatorio de una longitud dada."""
    return ''.join(random.choices(string.ascii_lowercase + ' ', k=longitud))

def crear_documentos(cantidad=100, carpeta='documentos'):
    """Crea una cantidad específica de documentos de texto con contenido aleatorio."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)  # Crea la carpeta si no existe

    for i in range(cantidad):
        nombre_archivo = f"documento_{i + 1}.txt"
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        
        # Generar un texto aleatorio de longitud 500
        texto = generar_texto_aleatorio(longitud=500)
        
        # Escribir el texto en el archivo
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(texto)

    print(f"{cantidad} documentos han sido creados en la carpeta '{carpeta}'.")

if __name__ == "__main__":
    crear_documentos()