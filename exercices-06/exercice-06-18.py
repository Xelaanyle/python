# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)
# Vous pouvez réutiliser la variable `size` qui a permis de construire le tableau en 2 dimensions
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.18

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        value = matrix[row_index][col_index]
        if value <= 50:
            print(f"Ligne : {row_index + 1}, Colonne : {col_index + 1}, Valeur : {value}")
            # j'ajoute +1 pour facilité la lecture pour partir de 1 au lieu de 0
