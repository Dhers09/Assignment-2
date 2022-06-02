import matplotlib.pyplot as plt
import numpy as np

print('Pauli matrices')
def f(x): 
    y = (x**2)-1
    return y 
a = 0
b = 10
All_I = []
def bisection(a,b,funct):     #bisection method
    if funct(a)*funct(b)>0:
        print("No root found")
        return
    c =a
    All_I.append(c)
    while ((b-a)>=0.01):     #checking for limits
        c = (a+b)/2
        All_I.append(c)
        if funct(c)==0:
            break  
        if funct(c)*funct(a)<0:
            b = c 
        else:
            a=c 
    print("Bisection root is : ", c)
bisection(a,b,f)

y_val = np.arange(a, b+1)
x_val = np.array([All_I])

plt.scatter(x_val, y_val, label = 'Scatter plot of convergency')
plt.legend()

#################################################################

def g(x):
    y = (x**2) - 1
    return y

def secant(x0,x1,N,funct):      #secant method
    root = 'None'
    step = 1
    condition = True
    while condition:
        if funct(x0) == funct(x1):
            print('First and second Y values were the same')
            break
        else:
            x2 = (x1*funct(x0) - (x0)*funct(x1))/( funct(x0) - funct(x1) ) 
            print('Step-', step,', x2 = ',x2,' and y(x2) = ', funct(x2))
            x0 = x1
            x1 = x2
            step = step + 1
            
            if step > N:
                print('Not Convergent')
                break
            
            condition = abs(funct(x2)) > 0.01       #if condition is true loop
            root = x2
    print('Secant root is: ', root)


x0 = 0
x1 = 10
N = 100

secant(x0,x1,N,g)

#The secant method and bisection method for the Pauli matrices is very close to each other

#-------------------------------------------------------
print('')
print('Matrix (4,1,2,-1)')
def h(x): 
    y = (x**2) - (3*x) - 6
    return y
a = 0
b = 10
bisection(a, b, h)

###########################################################

def j(x): 
    y = (x**2) - (3*x) - 6
    return y
x0 = 0
x1 = 10
N = 100
secant(x0,x1,N,j)

#The secant method and bisection method for the matrix is no so close to each other