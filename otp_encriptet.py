# Chiffre c an Bob übermitteln
c = "1100110000011000001100000111100101100000010011000100010000001001011010000100000001100100010111000001100100010000001111000001000000001000001010000000010001101000000110010000010010111100010000000011010000010000011001000100010000110100001100000100000101100000010001000000110000000101000011001101110000011100000001000011100000101001011010000000110000111101000001001011110000010000010110"
print("Übermitteltes Chiffrat:\n" + c)

# Schlüssel eingeben woimxzbvzupycdhajohwcaaqnlkxnddxglocvkhmozbaamkt
schluessel = input("Bitte Schlüssel eingeben: ")

# Übermittelter Schlüssel in bit umwndeln
s = ''.join(format(i, '08b') for i in bytearray(schluessel, encoding='utf-8'))

# Chiffre c mittels Schlüssel s zurück XORen = m
m = int(c, 2) ^ int(s, 2)
m = '0{:08b}'.format(m)

# m von Bit in Nachricht umwandeln
m = ''.join(chr(int(m[i*8:i*8+8], 2)) for i in range(len(m)//8))

# Bob kann Nachricht von Alice lesen
print("Nachricht:\n" + m)
