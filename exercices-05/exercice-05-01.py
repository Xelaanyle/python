# exo 5.1
# Ajoutez de la documentation à la fonction suivante et vérifiez
# qu'elle s'affiche correctement en utilisant la fonction help()

# réponse 5.1

def multiplication(a: float, b: float) -> float:
    """ def appel la fonction multiplication pour multiplié les variables a et b en float 
    return nous renvoie le resultat de la multiplication des deux variables en float""" 
    return a * b

help(multiplication)