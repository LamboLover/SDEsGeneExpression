# Solving the System of SDEs

import time
start_time = time.time()
import numpy as np
import GeneExpressionProbability as gxp

f1 = open("x1end.txt","w")
f2 = open("x2end.txt","w")
n = 1000  # no. of stochastic samples
h = .01   # time step size
end = 15  # End time
sig1 = 1.0  # it is coeffiecient that gets multiplied with the random term.
sig2 = 1.0  # similar to sig1 but for the second equation.
t = np.arange(0,int(end/h),h)
a = np.linspace(0,2,20)
x1end = np.zeros([n,len(a)])
x2end = np.zeros([n,len(a)])
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
x10 = np.random.uniform(-2, 2, n)
x20 = np.random.uniform(-2, 2, n)
for a0 in a:
    for j in range(n):
        x1[0] = x10[j]
        x2[0] = x20[j]
        for t0 in range(1, len(t)):
            x1[t0] = gxp.probGeneExpr(x1[t0-1], x2[t0-1],a=a0) + \
                sig1 * np.sqrt(h) * np.random.normal() + x1[t0-1]
            x2[t0] = gxp.probGeneExpr(x2[t0-1], x1[t0-1],a=a0) + \
                sig2 * np.sqrt(h) * np.random.normal() + x2[t0-1]
        x1end[j][np.where(a == a0)[0]] = x1[-1]
        x2end[j][np.where(a == a0)[0]] = x2[-1]
    print("a=",a0)
f1.write(str(x1end))
f2.write(str(x2end))
f1.close()
f2.close()
print("--- %s seconds ---" % (time.time() - start_time))