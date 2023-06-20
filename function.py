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

