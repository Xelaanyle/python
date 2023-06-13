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

