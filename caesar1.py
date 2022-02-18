print("Verschlüsselung nach Caesar")
print("---------------------------")

alphabet = "abcdefghijklmnopqrstuvwxyz"
klartext = input("Klartext eingeben: ")
klartext = klartext.lower()

schluessel = 3

geheimtext = ""

for buchstabe in klartext:
    if buchstabe == " ":
        geheimtext += " "
    else:
        nummer = alphabet.index(buchstabe)
        nummer += schluessel
        if nummer > 25:
            nummer -= 26
        geheimtext += alphabet[nummer]

print("Geheimtext: ", geheimtext.upper())