# import du module random (pour les nombres aléatoires)
import random 

# arithmétique

a = 42 + 123
a = 42 - 123
a = 42 * 123
a = 42 / 123

# division entière, integer division

a = 42 // 123
print(a)

# modulo ou reste de la division (euclidienne)

a = 53
# s'il y a un reste, le nombre n'est aps divisible par deux, donc il n'est pas pair
print(a % 2)

a = 74
# s'il y a un reste, le nombre n'est pas divisible par deux, donc il est pair
print(a % 2)

# puissance, exponentiaton
# deux puissance trois

a = 2 ** 3
print(a)

# opérateurs de comparaison
# opérateur d'égalité

result = 123 == 42
print(result)

password = "abc"
user_input = "def"
print(password == user_input)

# (strictement) plus grand que

print(123 > 42)

# plus grand ou égal à 

print(42 >= 42)

# (strictement) plus petit que

print(123 < 42)

# plus petit ou égal à 

print(42 <= 42)

# différent de 

print(123 != 42)

print(2 % 2 != 1 % 2) # Pair ou impair

# Opérateurs composés
b = 0

# incrémentation
b = 1
b = b + 1
b += 1
b += 1
print(b)

b = 1
b = b - 1
b -= 1
b -= 1
print(b)

# multiplication
c = 3
c = c * 2
c *= 2
print(c)

# division
d = 10
d = d / 3
d /= 3
print(d)

#division entière

d = 10
d = d // 3 
d //= 3
print(d)

# opérateur d'inclusion
text1 = "Lorem ipsum"

result = "e" in text1
print(result)
print("Lorem" in text1)
print("lorem" in text1)

list1 = ["Lorem", "ipsum"]
print("e" in list1) # False
print("ipsum" in list1) # True

# comparaison avec des nombres aléatoires
e = random.randint (0, 100)
f = random.randint (0, 100)

print(f'{e = }')
print(f'{f = }')

result = e == f
print(result)

result = e < f
print(result)

# expression 
# 1 + 1 -> 2
# (100 + 2) * 3 -> 102 * 3 -> 306
# 1 + 1 > (100 + 2) * 3 -> 2 > 306 -> False
# random.randint(0, 100) -> entre 0 et 100
#  
# print(100) -> ce n'est pas une expression

