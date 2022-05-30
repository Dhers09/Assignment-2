import numpy as np
import matplotlib.pyplot as plt
import math as mat               #to use tanh and cosh

h=0.1

x = np.linspace(-5,5,100)

def func(x):              #to convert tanh
    y =[]
    for i in x:
        y.append(mat.tanh(i))
    y = np.array(y)
    return y


def f_dev(f,h,x):
    y_fd = (f(x+h) -f(x))/h
    return y_fd

def b_dev(f,h,x):
    y_bd = (f(x) -f(x-h))/h
    return y_bd

def c_dev(f,h,x):
    y_cd = (f(x+h) -f(x-h))/(2*h)
    return y_cd

def func2(x):             #to convert cosh
    y =[]
    for i in x:
        y.append(mat.cosh(i))
    y = np.array(y)
    return y

plt.figure()
plt.plot(x,func(x),'--r',label = 'Original Function')
plt.legend()

plt.figure()
plt.plot(x,1/func2(x)**2,'-k',label = 'Theoretical')
plt.plot(x,f_dev(func,h,x),'.r',label = 'Numerical Forwards')
plt.plot(x,b_dev(func,h,x),'.g',label = 'Numerical Backwards')
plt.plot(x,c_dev(func,h,x),'.b',label = 'Numerical Centre')
plt.legend()
#all numerical graphs are very similar to the theoretical graph

plt.figure()
plt.plot(x, 1/func2(x)**2 - f_dev(func,h,x), '-*', label = 'Error Forwards')
plt.legend()
#accuracy is good as error foward is mostly straight except for the sudden dip and rise in the middle of the graph
#the peak and trough are the exact same distance from the centre. 

plt.figure()
plt.plot(x, 1/func2(x)**2 - b_dev(func,h,x), '-*', label = 'Error Backwards')
plt.legend()
#accuracy is good as error backwards is mostly straight except for the sudden rise and fall at the centre of the graph
#the trough and peak are the exact same distance from the centre. 

plt.figure()
plt.plot(x, 1/func2(x)**2 - c_dev(func,h,x), '-*', label = 'Error Centre')
plt.legend()
#accuracy is the best so far as is the lowest error values.
#the graph starts of straight, dips, suddenly rises to a peak at 0, dips again and then levels out

#the accuracy of these methods are good but not exact
