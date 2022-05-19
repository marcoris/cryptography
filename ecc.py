from tabulate import tabulate

aX = []
aY = []
header = []
a = 3
b = 2
mod = 7

x_1 = 5
y_1 = 4

x_2 = 5
y_2 = 3

for i, x, y in zip(range(mod), range(mod), range(mod)):
    header.append(i)
    aY.append(y**2 % mod)
    aX.append((x**3 + a*x + b) % mod)

X1 = (pow(x_1, 3) + a*x_1 + b) % mod
Y1 = pow(y_1, 2) % mod

X2 = (pow(x_2, 3) + a*x_2 + b) % mod
Y2 = pow(y_2, 2) % mod

print(f"y^2 mod {mod}")
print(tabulate([aY], headers=header, tablefmt='orgtbl'))
print()
print(f"x^3 + {a}x + {b} mod {mod}")
print(tabulate([aX], headers=header, tablefmt='orgtbl'))
print()
print(f"P({x_1};{y_1}) liegt" + ("" if Y1 == X1 else " NICHT") + " auf der Kurve")
if x_1 != x_2 or y_1 != y_2:
    print(f"Q({x_2};{y_2}) liegt" + ("" if Y2 == X2 else " NICHT") + " auf der Kurve")
print()

count = 0
for i in range(mod):
    d = ""
    for j in range(mod):
        if aX[i] == aY[j]:
            d += f"({i};{j}) und "
            count = count + 1

    t = print(f"Für x = {i}: gibt es {'keine Punkte' if d == '' else 'die Punkte ' + d[:-4]}")

print(f"Somit gibt es {count} Punkte + Nullpunkt = {count + 1} Punkte, d.h. |E| = {count + 1}")

# punktdoppelung
def pointDouble(x_1, y_1):
    return ((3*pow(x_1, 2) + a) * (pow((2*y_1), -1, mod))) % mod

# punktaddition
def pointAdd(x_1, x_2, y_1, y_2):
    if (x_2 - x_1) != 0:
        return ((y_2 - y_1) * (pow((x_2 - x_1), -1, mod))) % mod
    else:
        return 0

if x_1 is x_2 and y_1 is y_2:
    s = pointDouble(x_1, y_1)
else:
    s = pointAdd(x_1, x_2, y_1, y_2)

def calcX3(x_1, x_2, s):
    return (pow(s, 2) - x_1 - x_2) % mod

def calcY3(x_1, x_3, y_1, s):
    return (s * (x_1 - x_3) - y_1) % mod

# Add/Double
x_3 = calcX3(x_1, x_2, s)
y_3 = calcY3(x_1, x_3, y_1, s)

print(f"P({x_1},{y_1}) + " + ("P" if x_1 is x_2 and y_1 is y_2 else "Q") + f"({x_2},{y_2}) = " + ("2P" if x_1 is x_2 and y_1 is y_2 else "R") + f"({x_3},{y_3})")
print()
print("Für alle P das k*P:")
header = ["k"]
kP = ["k*P"]
firstDouble = True
posX = x_1
posY = y_1
firstPosX = posX
counter = 0
for i in range(1, (count + 1)):
    header.append(i)
    kP.append(f"({posX};{posY})")
    counter = counter + 1
    if i > count:
        break
    if firstDouble:
        s = pointDouble(x_1, y_1)
        x_3 = calcX3(x_1, x_1, s)
        y_3 = calcY3(x_1, x_3, y_1, s)
        firstDouble = False
    else:
        if firstPosX == posX:
            break;
        s = pointAdd(x_1, x_2, y_1, y_2)
        x_3 = calcX3(x_1, x_2, s)
        y_3 = calcY3(x_1, x_3, y_1, s)

    posX = x_3
    posY = y_3
    x_2 = posX
    y_2 = posY
header.append(counter + 1)
kP.append("O")

print(tabulate([kP], headers=header, tablefmt='orgtbl'))