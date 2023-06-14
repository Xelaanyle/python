# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10

sum_number = 0
for num in my_list:
    sum_number += num
num_in_list = len(my_list)
mean_number = sum_number / num_in_list
print(mean_number)