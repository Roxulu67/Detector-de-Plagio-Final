import os
from hash_table import HashTable  # Cambiar a importación absoluta
from similarity import calculate_jaccard_similarity  # Cambiar a importación absoluta
import matplotlib.pyplot as plt


class PlagiarismDetector:
    def __init__(self):
        self.documents = []  # Lista para almacenar documentos
        self.similarity_scores = {}  # Diccionario para almacenar puntuaciones de similitud

    def load_documents(self, path):
        """Carga documentos de texto desde la carpeta especificada."""
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                with open(os.path.join(path, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.documents.append((filename, self.tokenize(content)))

    def tokenize(self, text):
        """Tokeniza el texto en n-gramas (bi-gramas o tri-gramas)."""
        n = 2  # Cambia este valor para bi-gramas (2) o tri-gramas (3)
        tokens = []
        text = text.lower().replace('\n', ' ')  # Convertir a minúsculas y eliminar saltos de línea
        words = text.split()  # Dividir el texto en palabras

        for i in range(len(words) - n + 1):
            n_gram = ' '.join(words[i:i + n])  # Crear n-grama
            tokens.append(n_gram)

        return tokens

    def detect_plagiarism(self):
        """Calcula la similitud entre documentos y almacena los resultados."""
        for i in range(len(self.documents)):
            for j in range(i + 1, len(self.documents)):
                doc_a, tokens_a = self.documents[i]
                doc_b, tokens_b = self.documents[j]
                
                # Calcular similitud usando Jaccard
                similarity = calculate_jaccard_similarity(set(tokens_a), set(tokens_b))
                self.similarity_scores[(doc_a, doc_b)] = similarity

        # Llamar a la función para graficar similitudes
        self.graficar_similitudes()

    def graficar_similitudes(self):
        """Genera un gráfico de barras de las similitudes entre documentos."""
        documentos = []
        puntuaciones = []

        for (doc_a, doc_b), similarity in self.similarity_scores.items():
            documentos.append(f"{doc_a} - {doc_b}")
            puntuaciones.append(similarity)

        plt.figure(figsize=(10, 6))
        plt.barh(documentos, puntuaciones, color='skyblue')
        plt.xlabel('Puntuación de Similitud')
        plt.title('Similitudes entre Documentos')
        plt.xticks(rotation=45)
        plt.tight_layout()  # Ajusta el diseño para que no se corten las etiquetas

        if not os.path.exists('resultados'):
            os.makedirs('resultados')  # Crea la carpeta si no existe

        plt.savefig('resultados/similitudes.png')  # Guarda el gráfico como imagen
        plt.show()  # Muestra el gráfico

    def save_results(self, path):
        """Guarda los resultados de similitud en un archivo."""
        with open(path, 'w', encoding='utf-8') as file:
            for doc_pair, similarity in self.similarity_scores.items():
                file.write(f"{doc_pair[0]} - {doc_pair[1]}: {similarity:.2f}\n")