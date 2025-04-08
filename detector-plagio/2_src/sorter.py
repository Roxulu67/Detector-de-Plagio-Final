import matplotlib.pyplot as pltks
def merge_sort(arr):
    """
    Implementación del algoritmo Merge Sort.
    
    :param arr: Lista de elementos a ordenar.
    :return: Lista ordenada.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio de la lista
        left_half = arr[:mid]  # Divide la lista en dos mitades
        right_half = arr[mid:]

        # Llama recursivamente a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  # Inicializa índices para las mitades y el array resultante

        # Copia los datos a los arrays temporales left_half y right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica si quedan elementos en left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica si quedan elementos en right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr