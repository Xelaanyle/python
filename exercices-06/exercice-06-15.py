# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
valeur = 0
index = 0
Long_strings = 0

for i in range(len(my_list)):
    if (len(my_list)) > Long_strings:
        Long_strings = len(my_list[i])
        index = i
        Long_valeur = my_list[index]
print(f"{Long_strings = }")
print(f"{Long_valeur = }")
print(f"{index = }")

# for i in range(len(my_list)): : Cette boucle for itère sur les indices de la liste my_list. La fonction len(my_list) renvoie la longueur de la liste, et range(len(my_list)) génère une séquence d'indices allant de 0 à la longueur de la liste moins un.
# if len(my_list[i]) > longest_length: : À chaque itération de la boucle, on vérifie si la longueur de la chaîne de caractères à l'indice i est plus grande que la valeur de longest_length (la longueur de la plus longue chaîne de caractères trouvée jusqu'à présent).
# Si la condition est vérifiée, cela signifie qu'une nouvelle chaîne de caractères plus longue a été trouvée. On met alors à jour les variables suivantes :
#     longest_length = len(my_list[i]) : On met à jour longest_length avec la nouvelle longueur de la chaîne de caractères.
#     index = i : On met à jour index avec l'indice de la chaîne de caractères la plus longue.
#     longest_string = my_list[index] : On met à jour longest_string avec la valeur de la chaîne de caractères la plus longue.
# En fin de boucle, nous avons trouvé la chaîne de caractères la plus longue dans my_list. Nous imprimons ensuite les résultats :
#     print("Index:", index) : Affiche l'indice de la chaîne de caractères la plus longue.
#     print("Valeur:", longest_string) : Affiche la valeur de la chaîne de caractères la plus longue.
#     print("Longueur:", longest_length) : Affiche la longueur de la chaîne de caractères la plus longue.