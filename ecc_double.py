print("Punktverdoppelung P auf E : y^2 = x^3 + 2x + 2 mod 17")
print("------------------------------------------------------")
x_1 = int(input("Punkt x_1 von P angeben:"))
y_1 = int(input("Punkt y_1 von P angeben:"))
x_2 = int(input("Punkt x_2 von Q angeben:"))
y_2 = int(input("Punkt y_2 von Q angeben:"))
a = int(input("a angeben:"))
b = int(input("b angeben:"))
p = int(input("Mod p angeben:"))

print(f"y^2 = x^3 + {a}x + {b} mod {p}")
print(f"P = ({x_1}, {y_1}) verdoppeln:")

if x_1 is x_2 and y_1 is y_2:
    s = (pow(a*1, -1, p)) * (3*x_1**2 + a) % p
else:
    s = (y_2 - y_1)/(x_2 - x_1) % p

x_3 = (s**2 - x_1 - x_2) % p
y_3 = (s * (x_1 - x_3) - y_1) % p
if x_1 is x_2 and y_1 is y_2:
    print(f"x*P = ({x_1}, {y_1}) + ({x_2}, {y_2}) = ({x_3}, {y_3})")
else:
    print(f"P + Q = ({x_1}, {y_1}) + ({x_2}, {y_2}) = ({x_3}, {y_3})")