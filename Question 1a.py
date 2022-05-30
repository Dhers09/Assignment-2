import numpy as np
import matplotlib.pyplot as plt

h=0.1

x = np.linspace(-2,3,100)

def func(x):
    y = ((1/4)*(x**4)) - (x**2) - x
    return y

def f_dev(f,h,x):            # to calculate foward derivative
    y_fd = (f(x+h) -f(x))/h
    return y_fd

def b_dev(f,h,x):            # to calculate backward derivative
    y_bd = (f(x) -f(x-h))/h
    return y_bd

def c_dev(f,h,x):            # to calculate centred derivative
    y_cd = (f(x+h) -f(x-h))/(2*h)
    return y_cd

plt.figure()
plt.plot(x,func(x),'--r',label = 'Original Function')
plt.legend()

plt.figure()
plt.plot(x,(x**3)-(2*x)-1,'-k',label = 'Theoretical')
plt.plot(x,f_dev(func,h,x),'.r',label = 'Numerical Forwards')
plt.plot(x,b_dev(func,h,x),'.g',label = 'Numerical Backwards')
plt.plot(x,c_dev(func,h,x),'.b',label = 'Numerical Centred')
plt.legend()
#the three numerical graphs are very similar to the theoretical graph

plt.figure()
plt.plot(x, (x**3)-(2*x)-1 - f_dev(func,h,x), '-*', label = 'Error Forwards')
plt.legend()
#the accuracy of the forward is good when looking at the graphs. The error is not alot as we can see it slightly increases then at 0 it decreases
#the error is a concave parabola

plt.figure()
plt.plot(x, (x**3)-(2*x)-1 - b_dev(func,h,x), '-*', label = 'Error Backwards')
plt.legend()
#the accuracy of the backwards graph is about the same as the forwards. They have the similar numerical difference.
#the error is a convex parabola which is the opposite of the forward graph even though they have similar error value, just in +ve axis

plt.figure()
plt.plot(x, (x**3)-(2*x)-1 - c_dev(func,h,x), '-*', label = 'Error Centred')
plt.legend()
#the error is quiet linear in a decending fashion for the centred error. this is very different from the other errors

#the accuracy of these methods are good but not exact