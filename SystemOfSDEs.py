## Solving the System of SDEs and plot

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import GeneExpressionProbability as gxp

n = 1000
h = .1
end = 100
t = [h*i for i in range(int(end/h))]
x1end = np.zeros(n)
x2end = np.zeros(n)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
x10 = np.random.uniform(-2,2,n)
x20 = np.random.uniform(-2,2,n)
for i in range(n):
    x1[0] = x10[i]
    x2[0] = x20[i]
    #print(x10,x20)
 #   input("")
    for t0 in range(1,len(t)):
        x1t0 = x1[t0-1]
        x2t0 = x2[t0-1]
        x1[t0] = gxp.probGeneExpr(x1t0,x2t0)*np.sqrt(h)*np.random.normal()+x1t0
        x2[t0] = gxp.probGeneExpr(x2t0,x1t0)*np.sqrt(h)*np.random.normal()+x2t0
        print(x1t0,x2t0)
    x1end[i] = x1[-1]
    x2end[i] = x2[-1]

fig, ax = plt.subplots(layout='constrained')
fig.suptitle('SDE solution')

ax.plot(t, x1end, 'o-')
ax.set_ylabel('x1')

#plt.hist(x1end,bins=100)

plt.show()