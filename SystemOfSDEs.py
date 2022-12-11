## Solving the System of SDEs and plot

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import GeneExpressionProbability as gxp

n = 1000
h = .1
end = 100
sig1 = 1.0
sig2 = 1.0
t = [h*i for i in range(int(end/h))]
x1end = np.zeros(n)
x2end = np.zeros(n)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
for i in range(n):
    x1[0] = np.random.uniform(-2,2)
    x2[0] = np.random.uniform(-2,2)
    for t0 in range(1,len(t)):
        x1[t0] = gxp.probGeneExpr(x1[t0-1], x2[t0-1]) + \
            sig1 * np.sqrt(h) * np.random.normal() + x1[t0-1]
        x2[t0] = gxp.probGeneExpr(x2[t0-1], x1[t0-1]) + \
            sig2 * np.sqrt(h) * np.random.normal() + x2[t0-1]
    x1end[i] = x1[-1]
    x2end[i] = x2[-1]

fig, ax = plt.subplots(layout='constrained')
fig.suptitle('SDE solution')

ax.plot(t, x1end, 'o-')
ax.set_ylabel('x1')

plt.hist(x1end,bins=100)

plt.show()