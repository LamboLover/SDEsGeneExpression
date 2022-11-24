import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import GeneExpresssionProbability as gxp

x1 = [int(input("x1(0): "))]
x2 = [int(input("x2(0): "))]
h = .1
end = 2
t = [h*i for i in range(int(end/h))]
for t0 in t:
    if t0 == end:
        continue
    x1t0 = x1[int(t0/h)]
    x2t0 = x2[int(t0/h)]
    x1.append(gxp.probGeneExpr(x1t0,x2t0)*h+x1t0)
    x2.append(gxp.probGeneExpr(x2t0,x1t0)*h+x2t0)
print("x1: ",x1)
print("x2: ",x2)
print("t: ",t)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

a = np.arange(0,2,.05)
x = np.arange(-2,2,.1)
y = np.arange(-2,2,.1)
X, Y = np.meshgrid(x, y)
Z = gxp.probGeneExpr(X,Y)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()