import numpy as np
import pylab as pl

Y, X = np.mgrid[-10:10:100j, -10:10:100j]

def f(x):
    return x**3 + 3*x + 0

px = -2.0
py = -np.sqrt(f(px))

qx = 0.5
qy = np.sqrt(f(qx))

k = (qy - py)/(qx - px)
b = -px*k + py

poly = np.poly1d([-1, k**2, 2*k*b+3, b**2-5])

x = np.roots(poly)
y = np.sqrt(f(x))

pl.contour(X, Y, Y**2 - f(X), levels=[0])
pl.plot(x, y, "o")
pl.plot(x, -y, "o")

x = np.linspace(-5, 5)
pl.plot(x, k*x+b)
pl.show()
