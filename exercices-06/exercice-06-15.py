# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
index = 0
valeur = 0
Long_strings = 0

for i in range(len(my_list)):
    if (len(my_list)) > Long_strings:
        Long_strings = len(my_list[i])
        index = i
        valeur = my_list[index]
        
print(f"{index = }")
print(f"{valeur = }")
print(f"{Long_strings = }")
