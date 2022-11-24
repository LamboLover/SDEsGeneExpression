import math

# y' = f(t,y)
def f(t,y):
    return 2-2*y-pow(math.e,-4*t)

# solution for c1
def c1(y,t):
    return (y-1-pow(math.e,-4*t)/2)/(pow(math.e,-2*t))

# solution to y' = f(t,y)
def y(t,c):
    return 1+pow(math.e,-4*t)/2+c*pow(math.e,-2*t)

t0 = float(input("Enter t0: "))
y0 = float(input("Enter y0: "))
h = float(input("Enter step size: "))
n = int(input("Enter the number of steps: "))

c1 = c1(y0,t0)

time = [i*h for i in range(n+1)] # t_0, t_1, t_2,..., t_n
approximate = list() # y_0, y_1, y_2,..., y_n
exact = list() # y(0), y(1), y(2),..., y(n)

# y_(n+1) = y_n + f(t_n,y_n) * (t_(n+1)-t_n)
for j in range(n+1):
    m = f(t0,y0)
    y1 = y0 + h*m
    approximate.append(y0)
    exact.append(y(t0,c1)) # exact solution
    t1 = t0 + h
    t0 = t1
    y0 = y1

error = list()

# calculate the percentage error for each approximation
for val in exact:
    index = exact.index(val)
    approx = float(approximate[index])
    if val == 0:
        percentError = 0
    else:
        percentError = abs(val-float(approx))/val*100
    error.append(percentError)

print("Time, t_n|Approximation\t\t|Exact\t\t\t    |Error")
print("---------+----------------------+---------------------------+-------------------")
for j in range(1,n+1):
    print("t"+str(j)+" = "+"{:.1f}".format(time[j])+" |y"+str(j)+" = "+"{:.15f}".format(approximate[j])+"|y("+"{:.1f}".format(time[j])+") = "+str(exact[j])+"|"+"{:.15f}".format(error[j])+"%.")
