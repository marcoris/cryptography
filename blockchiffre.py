from random import SystemRandom

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Alice gibt Nachricht für Bob ein
nachricht = input("Nachricht: ")

# Nachricht in Bit (m) umwandeln und ausgeben
m = ''.join(format(i, '08b') for i in bytearray(nachricht, encoding='utf-8'))
print("Nachricht in bit:\n" + str(m))

# Schlüssel der Länge Nachricht per random generieren und ausgeben
schluessel = ''.join(SystemRandom().choice(alphabet) for _ in range(len(nachricht)))
print("Schlüssel: " + schluessel)

# Schlüssel in Bit (s) umwandeln und ausgeben
s = ''.join(format(i, '08b') for i in bytearray(schluessel, encoding='utf-8'))
print("Schlüssel in bit:\n" + str(s))

# m und s XORen = c
c = int(m, 2) ^ int(s, 2)
c = format(c, '08b')
print("Chiffrat:\n" + c)

# Chiffre c an Bob übermitteln

# Schlüssel s an Bob mittels sicherer Leitung (SSL) übermitteln

# Chiffre c mittels Schlüssel s zurück XORen = m
m = int(c, 2) ^ int(s, 2)
m = '0{:08b}'.format(m)
print("Nachricht in bit:\n" + m)

# m von Bit in Nachricht umwandeln
m = ''.join(chr(int(m[i*8:i*8+8], 2)) for i in range(len(m)//8))

# Bob kann Nachricht von Alice lesen
print("Nachricht:\n" + m)
