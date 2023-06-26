import library


def hello():
    print('Hello Python!')

# appel ou exécution
hello()

def hello2(name):
    print(f"Hello {name}!")

hello2("Xelaanyle")

# paramètres + retour de valeur
def addition(a, b):
    return a + b

resultat = addition(42, 123)
print(resultat)

# appel d'une fonction stockée dans un autre module
resultat = library.oui_non(False)
print(resultat)
resultat = library.oui_non(True)
print(resultat)

# reverse lookup
my_list = [42, 123, 3.14]

def reverse_lookup(my_list, value):
    """Cette fonction prend un paramètre une liste et une valeur à rechercher, Elle renvoie l'index de la valeur si elle est toruvée,
    ou None si la valeur n'est pas trouvée. 
    
    my_list list la liste dans laquelle il fait chercher valeur any la valeur à rechercher 
    return int si la valeur est trouvée ou None si la valeur n'est pas trouvée"""

    for i in range(len(my_list)):
        if my_list[i] == value:
            # print(f"{i = }")
            return i
        
    return None
    
resultat = reverse_lookup(my_list, 42)
print(resultat)

# type hinting

def mult(a: int, b: int) -> int:
    """Cette fonction ...
    
    a ...*
    b ...
    return ..."""

    return a * b

result = mult('abc', 5)
print(result)
# mais les autres types de données passent quand même result = mult('abc', 5)

# le nom de la fonction + ses paramètres + sont type de retour = signature de la fonction def mult(a: int, b: int) -> int:


# copie d'une fonction comme si c'était une variable
mult_copy = mult
mult_copy(2, 5)


# stockage de fonctions dans une liste
operations = []
operations.append(addition)
operations.append(mult)

a = 2
b = 5
resultat = None

for operation in operations:
    resultat = operation(a, b)
    print(resultat)


# fonction de degré supérieur
# une fonction qui accepte une fonction en paramètre
# ou qui renvoie un fonction
def operateur_binaire(a, b, fonction):
    return fonction(a, b)

# appel de la fonction de degré supérieur
resultat = operateur_binaire(2, 5, mult)


my_list = ['foo', 'ipsum']
text = "toto"

print(len(my_list))
print(len(text))

def my_len(value):
    return 42

# sauvegarde de la fonction len() originale
len_backup = len
# surcharge de la fonction len() originale
# c-à-d remplacement par une autre fonction
len = my_len

print(len(my_list))
print(len(text))

# restauration de la fonction len() originale
len = len_backup

# pass permet d'écrire un code python syntaxiquement valide 
# même quand on n'a pas encore le coprs de la condition if ou de la boucle for
if True:
    pass