# Nombre entier / Integer
number1 = 123
number1 = 42
print(number1)

# Nombre à virgule flottante / float
number2 = 3.14
number2 = 2.71
print(number2)

# Chaîne de caractères / string 
text1 = "foo bar baz"
print(text1)

text2 = "foo bar baz"
print(text2)

#Cette notation permet de faire des sauts de ligne
text4 = """<div>
    <h1>Titre de premier niveau</h1>
</div>
"""

#\n est équivalent à un saut de ligne
#\t est équivalent & une tabulation
text5 = "<div>\n\t<h1>Titre de premier niveau</h1>\n</div>\n"
print(text5)

#Le backslash seul est le caractère d'échappement
#Le \" est équivalent à une guillement
#Le \\ est équivalent à un backslash

text6 = "Foo \"Bar\" Baz"
print(text6)

text7 = "C:\\Program Files\\Foo"
print(text7)


# Booléen / Boolean
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

# Valeur nulle / Null value
accepted_terms = None
print(None)

# types de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_boring))
print(type(python_is_cool))
print(type(accepted_terms))

# Vérification du type de données
print(type(number1) is int)
print(type(number1) is str)

# Todo: interroger le type des autres variables

# Transtypage int -> str
#Typecasting
print(type(str(number1)))
print(str(number1))

# Transtypage int -> bool
print(type(bool(number1)))
print(bool(number1))

# Convertie en booléen, la valeur 0 donne false
number3 = 0
print(bool(number3))

# Transtypage str -> int
# print(type(int(text1))) <- Génère l'erreur print(type(number1) is int)

# Il ne peut pas avoir auter chose qu'un nombre dans la chaîne de caractère si on veut la convertir en "int"
text3 = "123456789"
print(type(int(text3)))

# Les fonctions de transtypage 
# str() convertit vers string / chaîne de caractères
# int() convertit vers integer / nombre entier
# float() convertir vers float / nombre a virgule flottante
# bool() convertir vers boolean / valeur booléen 


#permutez les deux variables a et b en utilisant l'opérateur d'affectation
#  et le nom des variables

a = 123
b = 42

# permutation des valeurs à l'aide de la méthode pythonique
# destructrured assignment

b, a = a, b

# permutation des valeurs à l'aide d'une varaible temporaire

tmp = a
a = b
b = tmp

print(a)
print(b)

# permutation des valeurs & l'aide d'opérations arithmétiques

a = a + b
b = a - b
a = a - b

print(a)
print(b)

# addition de float
# affiche 0.30000000000000004 au lieu de 0.3
print(0.1 + 0.1 + 0.1)

# affiche 0.10.10.1
print("0.1" + "0.1" + "0.1")

# pour additionner correctement des nombres décimaux

import decimal
from decimal import Decimal

# affiche correctement 0.3
print(Decimal("0.1") + (Decimal("0.1")) + (Decimal("0.1")))

# affiche correctement 0.3
print(Decimal("0.3"))

# arrondi des floats

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(Decimal("0.05").quantize(Decimal("1")))
print(Decimal("0.15").quantize(Decimal("0.1")))

decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
print(Decimal("0.05").quantize(Decimal("1")))
print(Decimal("0.15").quantize(Decimal("0.1")))
