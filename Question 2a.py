import numpy as np

a = 1
b = 4
n = 1001
h = (b - a) / (n-1)
x = np.linspace(a, b, n)
f = (1+(x)**2)**0.5

trap_int = (h/2) * (f[0] + 2*sum(f[1:n-1:]) + f[n-1])    #Trapezoidal rule

print("Trapezoidal rule integral = ", trap_int)

simp_int = (h/3) * (f[0] + 2*sum(f[:n-2:2]) + 4*sum(f[1:n-1:2]) + f[n-1])
    
print("Simpson's rule integral = ",simp_int)     #Simpson's rule

def integral():                 #calc exact integral
    e = (np.log(np.abs(((4**2)+1)**0.5 +4))+(4*((4**2) + 1)**0.5))/2 - (np.log(np.abs(((1**2)+1)**0.5 +1))+1*((1**2) + 1)**0.5)/2
    return(e)

print('Exact integral = ', integral())

#the three diferent methods for working out the integral gave very similar answers

#the accuracy of these methods are good almost exact