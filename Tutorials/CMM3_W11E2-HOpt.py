import sympy as sym
from sympy import symbols, solve
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')

def func(x1,x2):
    return (0.5 * 9 * (sym.sqrt(x1**2+(10-x2)**2)-10)**2 +
            0.5 * 2 * (sym.sqrt(x1**2+(10-x2)**2)-10)**2 - 2*x1 - 4*x2)

F = sym.Symbol('F')
F = func(x1,x2)

dFdx1 = sym.Symbol('dFdx1')
dFdx2 = sym.Symbol('dFdx2')
dFdx1 = sym.diff(F, x1)
dFdx2= sym.diff(F, x2)

dFdx1 = sym.lambdify(dFdx1, x1)
dFdx2 = sym.lambdify(dFdx2, x2)

def HOpt(F,dFx,dFy,x,y):

    hsym = symbols('hsym')

    xlist = []
    ylist = []
    flist = []
    dfxlist = []
    dfylist = []


    for i in range(0, 10, 1):
        xold = x
        yold = y

        dfx = dFx(x)
        dfy = dFy(y)

        #Create a function for the path to the top of the mountain.
        g = F(x+dfx*hsym, y+dfy*hsym)
        hexpr = sym.diff(g, hsym)

        hsolved = solve(hexpr)
        hopt = hsolved[0]

        x = xold + hopt*dfx
        y = yold + hopt*dfy

        Fxy = F(x, y)
        dfx = dFx(x)
        dfy = dFy(y)

        xlist.append(x)
        ylist.append(y)
        flist.append(Fxy)
        dfxlist.append(dfx)
        dfylist.append(dfy)

        if dfx <= 0.0001 and dfy <= 0.0001:
            break

    print(x, y, Fxy, dfx, dfy)

print(HOpt(F, dFdx1, dFdx2, 1, 1))

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, dpi=400)
ax.plot_surface(X, Y, func(X,Y), cmap=cm.Blues)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
