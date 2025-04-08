##Detector de Plagio para Trabajos Estudiantiles

## Estructura del repositorio

1. **1_documentos/**
   - Contiene los archivos de texto (.txt) con los trabajos estudiantiles a analizar

2. **2_src/**
   - Módulos principales del sistema


3. **3_tests/**
   - Pruebas automatizadas para validar el funcionamiento

4. **4_resultados/**
   - Almacena:
     - Reportes de similitud
     - Gráficos de visualización

5. **Archivos raíz:**
   - `main.py`: Punto de entrada principal
   - `requirements.txt`: Lista de paquetes necesarios
   - `README.md`: Documentación

## Descripción
    Este proyecto es un sistema de detección de plagio que identifica similitudes entre trabajos estudiantiles utilizando técnicas de procesamiento de texto y algoritmos de comparación.


## Funcionalidades
    Generación de documentos de texto aleatorios.
    Preprocesamiento de documentos para análisis.
    Cálculo de similitudes entre documentos utilizando diferentes métodos.
    Visualización de resultados a través de gráficos.
    Interfaz gráfica para facilitar la interacción del usuario.

## Instalación
    - Requisitos Previos
    1. Asegúrate de tener instalado Python (versión 3.6 o superior) en tu sistema. También necesitarás las siguientes bibliotecas:

        pandas
        matplotlib
        tkinter (generalmente incluido con Python)

1. Clona el repositorio:
   ```bash
   git clone <https://github.com/Roxulu67/Detector-de-Plagio-Final.git>
   cd <Detector-de-Plagio-Final>

2. Crea y activa un entorno virtual
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate

3. Instala las dependencias:
    pip install -r requirements.txt

3. Ejecutar
    1. Genera documentos en la carpeta documentos/.
    2. Ejecuta el script principal:
        python main.py
    3. Los resultados se guardarán en la carpeta resultados/.
       

## Integrantes del equipo
- Darla Solis
- Yasser Suárez
- Rodrigo Tovar
