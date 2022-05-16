from tabulate import tabulate

aX = []
aY = []
heady = []
mod = 17
a = 2
b = 2

x_1 = 13
y_1 = 7

x_2 = 6
y_2 = 3

for i, x, y in zip(range(mod), range(mod), range(mod)):
    heady.append(i)
    aY.append(y**2 % mod)
    aX.append((x**3 + a*x + b) % mod)

Y1 = y_1**2 % mod
X1 = (x_1**3 + a*x_1 + b) % mod

Y2 = y_2**2 % mod
X2 = (x_2**3 + a*x_2 + b) % mod

print(f"y^2 mod {mod}")
print(tabulate([aY], headers=heady, tablefmt='orgtbl'))
print()
print(f"x^3 + {a}x + {b} mod {mod}")
print(tabulate([aX], headers=heady, tablefmt='orgtbl'))
print()
print(f"P({x_1}, {y_1}) liegt" + ("" if Y1 == X1 else " NICHT") + " auf der Kurve")
print(f"P({x_2}, {y_2}) liegt" + ("" if Y2 == X2 else " NICHT") + " auf der Kurve")
print()

for i in range(mod):
    d = ""
    for j in range(mod):
        if aX[i] == aY[j]:
            d += f"({i};{j}) und "

    t = print(f"Für x = {i}: gibt es {'keine Punkte' if d == '' else 'die Punkte ' + d[:-4]}")

