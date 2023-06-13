import random

#Block if 1
if True:
    print("ce message s'affichera toujours")

if False:
    print("Ce message ne s'affichera jamais")

else:
    print("La première condition n'est pas vérifiée")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

#Block if 2
if number1 < number2:
    print("number1 est plus petit que number2")

else: # number1 >= number2
    print("number1 est plus grand ou égale à number2")

#Block if 3
if number1 < number2:
    print("number1 est plus petit que number2")

elif number1 > number2:
    print("la variable number1 est plus grande que number2")

else: # number1 = number2
    print("Les deux variables number1 et number2 sont égales")

# elif == else if 


# réécriture du block if 3 avec des if imbriqués

if number1 < number2:
    print("number1 est plus petit que number2")
else: 
    if number1 < number2:
        print("number1 est plus grande que number2")
    else:
        print("les deux variables number1 et number2 sont égales")

# opérateurs booléens

# négation
print(not True)
print(not False)

# table de vérité de l'opérateur de négation
# A     not A
# True  False
# False True

# OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Table de vérité de l'opérateur ou logique
# A     B      A or B
# True  True   True
# True  False  True
# False True   True 
# False False  False

# pour retrouver la table, remplacez :
# - A par "j'ai du cash"
# - B par "j'ai ma carte bleu"
# - "A or B" par "puis-je faire mes courses ?"

# ET logique
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Table de vérité de l'opérateur et logique
# A     B      A or B
# True  True   True
# True  False  False
# False True   False
# False False  False

# Tables de vérité de l'opérateur NAND (not and)
# A     B      A and B  not (A and B)
# True  True   True     False
# True  False  False    True
# False True   False    True
# False False  False    True

# utilisation de l'opérateur and pour voir si une variable est dans un interval de valeurs

# age >= 12 and age <= 25
# 12 <= age <= 25

# OU EXCLUSIF
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

# Tables de vérité de l'opérateur XOR
# A     B      A xor B
# True  True   False
# True  False  True
# False True   True
# False False  False

# exo course (opérateur OU logique)
# affichez :
has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cb or has_cash:
    print("Je peut faire les courses")
else:
    print("Je ne peut pas faire les courses")

# exo courses (opérateur ET logique)
# remplissez le même cahier des charges mais avec l'opérateur ET
if not has_cash and not has_cb:
    print("Je ne peut pas faire les courses")
else:
    print("Je peut faire les courses")

# combinaison d'opérateurs AND et OR
user_level = 1
user_xp = 0
user_social = 150

#version bugué
if user_level >= 3 and user_xp >= 100 or user_social >= 100:
    print("Le joueur peut acheter du matériel")
else:
    print("Le joueur ne peut pas acheter de matériel")

#Version corrigée
if user_level >= 3 and (user_xp >= 100 or user_social >= 100):
    print("Le joueur peut acheter du matériel")
else:
    print("Le joueur ne peut pas acheter de matériel")


# exercice carte de réduction
# déterminez la carte de réduction auquelle le voyageur a droit :
# - entre 0 et 11 (inclus), le voyageur a droit à la gratuité
# - entre 12 et 24 ans (inclus), le voyageur a droit à une réduction de 50%
# - entre 25 et 64 ans (inclus), le voyageur a droit à une réduction de 10%
# - au delà de 65 ans (inclus), le voyageyr a droit à une réduction de 50%
age = random.randint(0, 99)

if age >= 0 and age <= 11:
    print("Le voyageur à droit a la gratuité")
elif age >= 12 and age <= 24:
    print("Le voyageur a le droit à 50%")
elif age >= 25 and age <= 64:
    print("Le voyageur a le droit à 10%")
else: # Si le voyageur à plus de 65 ans
    print("le voyageur a le droit à 50%")

