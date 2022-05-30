import numpy as np

p = []
q = []
y = 0.0
h1 = 1.0  #h1 = (4-1)/3 , 3 subintervals were taken
h2 = 1.5  #h2 + (4-1)/2 , 2 subint as must be even

def func():                     #calculates values and puts them in a list
    for i in range(1,5):
        y = (1+(i)**2)**0.5
        p.append(y)
    return(p)

def trap_int(p):                #calulates trapezoidal integral
    tsum = 0.0
    for i in range(len(p)-1):
        tsum += (h1/2)*(p[i]+p[i+1])
        
    return(tsum)

print("Trapezoidal rule integral = ", trap_int(func())) #gives trapezoidal integral for numbers in list
    

def simp():                     #calculates values and puts them in a list
    for i in np.arange(1,5,1.5):
        y = (1+(i**2))**0.5
        q.append(y)
    return(q)

def simp_int(q):                # calc simpson's integral
    tsimp = (h2/3)*(q[0] + 4*(q[1]) + q[2])
    return(tsimp)

print("Simpson's rule integral = ", simp_int(simp()))   #gives simpson's integral for numbers in list


def integral():                 #calc exact integral
    e = (np.log(np.abs(((4**2)+1)**0.5 +4))+(4*((4**2) + 1)**0.5))/2 - (np.log(np.abs(((1**2)+1)**0.5 +1))+1*((1**2) + 1)**0.5)/2
    return(e)

print('Exact integral = ', integral())

#the three diferent methods for working out the integral gave very similar answers

#the accuracy of these methods are good but not exact