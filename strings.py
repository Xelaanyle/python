text1 = "lorem"
text2 = "ipsum"

# concaténation
text3 = "Citation : " + text1 + " " + text2 + ", César"
print(text3)

# interpolation avec une f-string
text3 = f"citation : {text1} {text2}, César"
print(text3)

# attention la concaténation ne fonctione qu'avec des str
mails = 52
text4 = "Vous avez " + str(mails) + " non lus"
print(text4)

# répétition de texte 
text5 = "foo" * 3
print(text5)

# affichage de valeur arrondies mais sans arrondies mais sans arrondir la variable 
number1 = 10 / 3
text6 = f"10 / 3 est un peu près {number1:.2f}"
print(text6)

# les fonctions associés aux strings
text7 = "foo bar baz foo"
print(len(text7))

print(text7.count('foo')) # (/n) calcule le nombre de ligne

# retrouve l'emplacement d'un mot
position = text7.find('foo')
print(position)

# pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo', position + 1 ))

# si le mot est absent, la fonction revoie -1
position = text7.find('lorem')
print(position)

# remplacement de mots
text7 = text7.replace('foo', 'lorem')
print(text7)

# split & join
list1 = text7.split(' ')
print(list1)

text8 = " ".join(list1)
print(text8)

# documenter une fonction

def ouiNon(value):
    """ cette fonction renvoie :
    - "oui" si le paramètre passé est True
    - "non" si le paramètre passé est False
    "" dans les autres cas
    value bool valeur qui sera transformée en "oui" ou "non"
    return str
    """
    if value == True:
        return "oui"
    elif value == False:
        return "non"
    
    return None

#help(ouiNon)
print(ouiNon.__doc__)
