# https://de.wikipedia.org/wiki/Diffie-Hellman-Schl%C3%BCsselaustausch#Programmierung
from random import randint

# Festlegung der Gruppe (modulo):
p = 107

# Festlegung einer public Zahl < p
g = 3

# Zufällige Wahl der geheimen Schlüssel von Alice und Bob:
a = randint(1, p-1)
b = randint(1, p-1)

# Berechnung der Öffentlichen Schlüssel und senden an jeweilige Partei: A <- (p,g,B) B <- (p,g,A)
A = pow(g, a, p)
B = pow(g, b, p)

print(f'Öffentlicher Schlüssel von Alice: {A=}')
print(f'Öffentlicher Schlüssel von Bob:   {B=}')

# Berechnung des gemeinsamen Geheimnisses:
k_a = pow(B, a, p)
k_b = pow(A, b, p)

print(f'{k_a=}')
print(f'{k_b=}')
