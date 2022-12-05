# Solving the System of ODEs and plot

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import GeneExpressionProbability as gxp

h = .01
end = 15
t = [h*i for i in range(int(end/h))]
x1 = [float(input("x1(0): "))] + [0] * (len(t)-1)
x2 = [float(input("x2(0): "))] + [0] * (len(t)-1)
for t0 in range(1,len(t)):
    x1t0 = x1[t0-1]
    x2t0 = x2[t0-1]
    x1[t0] = gxp.probGeneExpr(x1t0,x2t0)*h+x1t0
    x2[t0] = gxp.probGeneExpr(x2t0,x1t0)*h+x2t0
print("x1: ",x1)
print("x2: ",x2)
print("t: ",t)

#fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
#
#a = np.arange(0,2,.05)
#x = np.arange(-2,2,.1)
#y = np.arange(-2,2,.1)
#X, Y = np.meshgrid(x, y)
#Z = gxp.probGeneExpr(X,Y)
#surf = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')
#fig1.colorbar(surf, shrink=0.5, aspect=5)

fig, ax = plt.subplots(layout='constrained')
ax.plot(t, x1, alpha=0.5, linestyle='--', linewidth=3, label='x1')
ax.plot(t, x2, alpha=0.5, linestyle='--', linewidth=3, label='x2')
ax.legend()

plt.show()