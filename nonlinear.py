#-----------Non-Linear Equation solver------------
import math
xo=float(input("x1"))
x1=float(input("x2"))
x=[xo,x1]

#-----------Eqn must be on form f(x)=0--------------

def f(x):
    return math.tan(x)-math.exp(-x)

#-----------Bisection method Algorithm--------------------


while f(x[0])*f(x[1])<0:
    x.append((x[0]+x[1])/2)
    if f(x[2])*f(x[1])>0:
        del(x[1])
        if(round(f(x[-1]),4)==0):
            print("x=",round(x[1],4))
            break
    elif f(x[2])*f(x[1])<0:
        del(x[0])
        if(round(f(x[-1]),4)==0):
            print("x=",round(x[1],4))
            break
    else:
        print("x=",round(x[1],4))
        break
if f(x[0])*f(x[1])>0:
    print ("there is no solution in this interval")

else:
    if f(x[0])==0:
        print("x=",round(x[0],4))
    elif f(x[1])==0:
        print("x=",round(x[1],4))

error=x[1]-x[0]
print("Approximate error=",error)
