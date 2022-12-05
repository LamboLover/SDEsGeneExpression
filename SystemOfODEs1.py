import numpy as np
import matplotlib.pyplot as plt
import GeneExpressionProbability as gxp



# x1 = np.[int(input("x1(0): "))]
# x2 = [int(input("x2(0): "))]
h = .01
end = 15
t = np.linspace(0.0, end, round(end/h)+1)
x1 = np.zeros(np.size(t))
x2 = np.zeros(np.size(t))
x1[0] = input("initial value of x1 at t=0")
x2[0] = input("initial value of x2 at t=0")
# print(t)
for t0 in range(1, np.size(t), 1):
    # x1t0 = x1[int(t0/h)]
    # x2t0 = x2[int(t0/h)]
    x1[t0] = gxp.probGeneExpr(x1[t0-1], x2[t0-1])*h+x1[t0-1]
    x2[t0] = gxp.probGeneExpr(x2[t0-1], x1[t0-1])*h+x2[t0-1]
fig, ax = plt.subplots(layout='constrained')
ax.plot(t, x1, alpha=0.5, linestyle='--', linewidth=3, label='x1')
ax.plot(t, x2, alpha=0.5, linestyle='--', linewidth=3, label='x2')
ax.legend()  # Add a legend.
plt.show()