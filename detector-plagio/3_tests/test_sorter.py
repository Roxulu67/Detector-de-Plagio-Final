import random
import time
import unittest
from src.sorter import merge_sort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        # Generar un conjunto de datos grande (1000 elementos aleatorios)
        self.large_data = [random.randint(1, 10000) for _ in range(1000)]

    def test_merge_sort(self):
        # Guardar una copia de los datos originales
        original_data = self.large_data.copy()
        
        # Ordenar los datos usando merge_sort
        sorted_data = merge_sort(self.large_data)

        # Verificar que la lista esté ordenada
        self.assertEqual(sorted_data, sorted(original_data))

    def test_performance(self):
        # Medir el tiempo de ejecución del algoritmo
        start_time = time.time()
        merge_sort(self.large_data)
        end_time = time.time()
        
        print(f"Tiempo de ejecución para ordenar 1000 elementos: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    unittest.main()