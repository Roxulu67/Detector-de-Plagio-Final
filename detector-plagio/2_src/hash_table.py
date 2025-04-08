class HashTable:
    def __init__(self, size=100):
        """Inicializa la tabla hash con un tamaño específico."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Inicializa la tabla como una lista de listas

    def _hash(self, key):
        """Función hash simple que calcula el índice para una clave dada."""
        return hash(key) % self.size

    def insert(self, key):
        """Inserta un n-grama en la tabla hash."""
        index = self._hash(key)
        # Evitar duplicados
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        """Busca un n-grama en la tabla hash y devuelve True si se encuentra."""
        index = self._hash(key)
        return key in self.table[index]

    def get_all_keys(self):
        """Devuelve todos los n-gramas almacenados en la tabla hash."""
        keys = []
        for bucket in self.table:
            keys.extend(bucket)
        return keys

    def __len__(self):
        """Devuelve el número total de n-gramas almacenados en la tabla hash."""
        return sum(len(bucket) for bucket in self.table)