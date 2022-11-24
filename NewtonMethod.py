def f(x):
    return x**3-3*x+1

def df(x):
    return 3*x**2-3

def newtons_method(x0, f, df, tolerance):
    y = f(x0)
    yprime = df(x0)

    x1 = x0 - y / yprime        # get the first interation

    iteration = 0

    print("Iteration: ",iteration,", dx: ",y/yprime,", f(x1): ",y)

    x = x0

    x0 = x1

    while abs(y/yprime) > tolerance:
        iteration += 1
        
        y = f(x0)
        yprime = df(x0)

        x1 = x0 - y / yprime        # get the next interation

        print("Iteration: ",iteration,", dx: ",y/yprime,", f(x1): ",y)

        if abs(y/yprime) <= tolerance:
            break                   # x1 is within tolerance

        x = x0

        x0 = x1                     # update x0 and start again
    return x1

x0 = float(input("x0: "))
tolerance = float(eval(input("tolerance: ")))
print(newtons_method(x0,f,df,tolerance))
