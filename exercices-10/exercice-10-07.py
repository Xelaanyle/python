# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoie le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7
import random

# initialisation des variables
price = 100
tax_type = None

# déclaration de la fonction
def compute_tax(price: float, tax_type: int):
    if tax_type == 1:
       tax_price = price + price * (2.1/100)
       return tax_price
    elif tax_type == 2:
       tax_price = price + price * (5.5/100)
       return tax_price
    elif tax_type == 3:
       tax_price = price + price * (10/100)
       return tax_price
    elif tax_type == 4:
       tax_price = price + price * (20/100)
       return tax_price
    else:
       return price

#Premier jet de boucle
for i in range(0, 5):
   tax_type = i
   tax_price = compute_tax(price, tax_type)
   print(tax_price)

#Deuxième jet de boucle
for tax_type in range(0, 5):
   tax_price = compute_tax(price, tax_type)
   print(tax_price)
