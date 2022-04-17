print("Verschlüsselung nach Caesar")
print("---------------------------")

alphabet = "abcdefghijklmnopqrstuvwxyz"
klartext = input("Klartext eingeben: ")
klartext = klartext.lower()

schluessel = input("Schlüssel eingeben: ")

geheimtext = ""

for buchstabe in klartext:
    if buchstabe == " ":
        geheimtext += " "
    else:
        nummer = alphabet.index(buchstabe)
        nummer += int(schluessel)
        nummer %= 26
        geheimtext += alphabet[nummer]

print("Geheimtext: ", geheimtext.upper())

klartext = ""

for buchstabe in geheimtext:
    if buchstabe == " ":
        klartext += " "
    else:
        nummer = alphabet.index(buchstabe)
        nummer -= int(schluessel)
        nummer %= 26
        klartext += alphabet[nummer]

print("Klartext: ", klartext.upper())