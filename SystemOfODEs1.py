import numpy as np
import matplotlib.pyplot as plt


def f(x1, x2, a=1, b=1, k=1, S=0.5, n=4):
    return (a*pow(x1, n))/(pow(S, n)+pow(x1, n)) + \
           (b*pow(S, n))/(pow(S, n)+pow(x2, n))-k*x1


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
    x1[t0] = f(x1[t0-1], x2[t0-1])*h+x1[t0-1]
    x2[t0] = f(x2[t0-1], x1[t0-1])*h+x2[t0-1]
fig, ax = plt.subplots(layout='constrained')
ax.plot(t, x1, alpha=0.5, linestyle='--', linewidth=3, label='x1')
ax.plot(t, x2, alpha=0.5, linestyle='--', linewidth=3, label='x2')
ax.legend()  # Add a legend.
plt.show()