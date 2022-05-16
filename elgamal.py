from random import randint

# Der Empfänger A veröffentlicht als öffentlichen Schlüssel drei Zahlen p, g und a.
# Hierbei ist p eine starke Primzahl:
p = 467
g = 2
print(f'Hierbei ist {p} eine starke Primzahl')

# Um a zu berechnen, wählt A eine Zufallszahl u mit 1<u<p-1:
u = randint(1, p-1)
print(f'Um a zu berechnen, wählt A eine Zufallszahl {u=}')
# und berechnet a = g^u mod p:
a = pow(g, u, p)

print(f'und berechnet a = g^u mod p: {a=}')
print(f'Der öffentliche Schlüssel von A ist also: {p=}, {g=}, {a=}')

# Der Sender B möchte eine Nachricht m an A schicken:
m = 33
# Hierzu wählt B zunächst eine Zufallszahl v:
v = randint(1, 1000)
# und berechnet b = g^v mod p:
b = pow(g, v, p)
# und k = a^v mod p:
k = pow(a, v, p)
# sowie anschließend c = k * m mod p:
c = k * m % p
# Somit sendet B den Geheimtext (b, c) an A.

print(f'Der Sender B möchte eine Nachricht {m=} an A schicken:')
print(f'Hierzu wählt B zunächst eine Zufallszahl {v=}')
print(f'und berechnet b = g^v mod p: {b=}')
print(f'und k = a^v mod p: {k=}')
print(f'sowie anschließend c = k * m mod p: {c=}')
print(f'Somit sendet B den Geheimtext {b=}, {c=} an A.')

# Entschlüsseln A
k_1 = pow(b, p - 1 - u, p)
print(f'Der Empfänger A berechnet zunächst {k_1=}')
klartext = k_1 * c % p
print(f'und erhält somit den Klartext {klartext=}')