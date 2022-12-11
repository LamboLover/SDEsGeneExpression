# Solving the System of SDEs and plot

import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator
import numpy as np
import GeneExpressionProbability as gxp

n = 5000  # no. of stochastic samples
h = .01   # time step size
end = 15  # End time
sig1 = 1.0  # it is coeffiecient that gets multiplied with the random term.
sig2 = 1.0  # similar to sig1 but for the second equation.
t = [h*i for i in range(int(end/h))]
x1end = np.zeros(n)
x2end = np.zeros(n)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
x10 = np.random.uniform(-2, 2, n)
x20 = np.random.uniform(-2, 2, n)
for i in range(n):
    x1[0] = x10[i]
    x2[0] = x20[i]
    for t0 in range(1, len(t)):
        x1[t0] = gxp.probGeneExpr(x1[t0-1], x2[t0-1]) + \
            sig1 * np.sqrt(h) * np.random.normal() + x1[t0-1]
        x2[t0] = gxp.probGeneExpr(x2[t0-1], x1[t0-1]) + \
            sig2 * np.sqrt(h) * np.random.normal() + x2[t0-1]
        # print(x1t0,x2t0)
    x1end[i] = x1[-1]
    x2end[i] = x2[-1]
    if (i % 500 == 0 and i > 0):
        print('number of samples generated =  ', i)

print('DONE!!')
plt.hist(x1end, bins=100)

plt.show()