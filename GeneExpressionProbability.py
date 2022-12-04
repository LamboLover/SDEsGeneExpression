def probGeneExpr(x1,x2,a=1,b=1,k=1,S=0.5,n=4):
    return (a*pow(x1,n))/(pow(S,n)+pow(x1,n))+(b+pow(S,n))/(pow(S,n)+pow(x2,n))-k*x1
