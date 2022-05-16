from tabulate import tabulate

aX = []
aY = []
header = []
a = 1
b = 6
mod = 11

x_1 = 2
y_1 = 4

x_2 = 2
y_2 = 4

for i, x, y in zip(range(mod), range(mod), range(mod)):
    header.append(i)
    aY.append(y**2 % mod)
    aX.append((x**3 + a*x + b) % mod)

Y1 = y_1**2 % mod
X1 = (x_1**3 + a*x_1 + b) % mod

Y2 = y_2**2 % mod
X2 = (x_2**3 + a*x_2 + b) % mod

print(f"y^2 mod {mod}")
print(tabulate([aY], headers=header, tablefmt='orgtbl'))
print()
print(f"x^3 + {a}x + {b} mod {mod}")
print(tabulate([aX], headers=header, tablefmt='orgtbl'))
print()
print(f"P({x_1}, {y_1}) liegt" + ("" if Y1 == X1 else " NICHT") + " auf der Kurve")
print(f"P({x_2}, {y_2}) liegt" + ("" if Y2 == X2 else " NICHT") + " auf der Kurve")
print()

count = 0
for i in range(mod):
    d = ""
    for j in range(mod):
        if aX[i] == aY[j]:
            d += f"({i};{j}) und "
            count = count + 1

    t = print(f"Für x = {i}: gibt es {'keine Punkte' if d == '' else 'die Punkte ' + d[:-4]}")

print(f"Somit gibt es {count} Punkte + Nullpunkt = {count + 1} Punkte. E = {count + 1}")

# punktaddition/-doppelung
def doubleOrAdd(x_1, x_2, y_1, y_2):
    if x_1 is x_2 and y_1 is y_2:
        return ((3*x_1**2 + a) % mod * (pow((2*y_1), -1, mod))) % mod
    else:
        if (x_2 - x_1) > 0:
            return ((y_2 - y_1) % mod * (pow((x_2 - x_1), -1, mod))) % mod
        else:
            return 0
s = doubleOrAdd(x_1, x_2, y_1, y_2)

def calcX3(x_1, x_2, s):
    return (s**2 - x_1 - x_2) % mod

def calcY3(x_1, x_3, y_1, s):
    return (s * (x_1 - x_3) - y_1) % mod

print(f"s = {s}")

# Add
x_3 = calcX3(x_1, x_2, s)
y_3 = calcY3(x_1, x_3, y_1, s)
print(f"P({x_1},{y_1})" + (' * ' if x_1 is x_2 and y_1 is y_2 else ' + ') + f"Q({x_2},{y_2}) = R({x_3},{y_3})")

header = ["k"]
kP = ["k*P"]
for i in range(1, (count + 1)):
    header.append(i)
    kP.append(f"({x_2};{y_2})")
    s = doubleOrAdd(x_1, x_2, y_1, y_2)
    x_3 = calcX3(x_1, x_2, s)
    y_3 = calcY3(x_1, x_3, y_1, s)
    x_2 = x_3
    y_2 = y_3

print(tabulate([kP], headers=header, tablefmt='orgtbl'))