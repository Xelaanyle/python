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