import matplotlib.pyplot as plt
import numpy as np

def f(x,r):
    return r*x*(1-x)

n = 500
r = 2.4

fx = [i/100 for i in range(100)]
fy = [f(x,r) for x in fx]
plt.plot(fx,fx)
plt.plot(fx,fy)

x0 = 0.05
xlst = [x0,x0]
ylst = [0,f(x0,r)]
while len(xlst) < n:
    xlst.extend(2*[f(xlst[-1],r)])
    ylst.extend([ylst[-1],f(ylst[-1],r)])

x = np.array(xlst)
y = np.array(ylst)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")

plt.show()
