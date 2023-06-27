# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoie une valeur booléenne
# - renvoie `oui` si le paramètre est égal à True
# - renvoie `non` si le paramètre est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3

def oui_non(value):
    if value == True:
        return "oui"
    elif value == False:
        return "non"
    return None

result1 = oui_non(1 == 1)
result2 = oui_non(1 == 2)
print(result1)
print(result2)