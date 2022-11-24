import matplotlib.pyplot as plt
import numpy as np

n = 200
alst = [-2,-.5,.5,2]
b = 1
x0lst = [[b/(1-a)+i for i in [-.1,.1]] for a in alst]

def construct_sequence(x0,n,a,b):
    x = [x0]
    for i in range(n):
        x.append(a*x[i]+b)
    return x

for i in range(1,9):
    a = alst[(i-1)//2]
    x0 = x0lst[(i-1)//2][(i-1)%2]
    lst = construct_sequence(x0,n,a,b)
    y = np.array([lst[i] for i in range(n)])
    x = np.array(list(range(n)))
    plt.subplot(2,4,i)
    plt.plot(x,y)
    plt.xlabel("n")
    plt.ylabel("x_n")

plt.show()
