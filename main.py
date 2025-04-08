import sys
import os

# Agregar la carpeta 'src' al path para que Python pueda encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from detector import PlagiarismDetector

def main():
    # Crear una instancia del detector de plagio
    detector = PlagiarismDetector()
    
    # Cargar documentos desde la carpeta 'documentos'
    detector.load_documents('documentos/')
    
    # Detectar plagio entre los documentos cargados
    detector.detect_plagiarism()
    
    # Guardar los resultados en un archivo
    detector.save_results('resultados/similitudes.txt')

if __name__ == "__main__":
    main()