def calculate_jaccard_similarity(set_a, set_b):
    """Calcula la similitud de Jaccard entre dos conjuntos."""
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0