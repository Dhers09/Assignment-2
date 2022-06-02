import matplotlib.pyplot as plt


x0 = 0           #initial x
t0 = 1           #initial t
xn = 2           #end x
step = 10
dis = []         #list for displacement
t_d = []         #list for time displacement

def f(x,t):
    v = x/t      #differentcial equation
    return v

def rk4(x0,t0,xn,n,c,x):

    h = (xn-x0)/n        
    
    for i in range(n):
        k1 = h * (f(x0, t0))
        k2 = h * (f((x0+h/2), (t0+k1/2)))
        k3 = h * (f((x0+h/2), (t0+k2/2)))
        k4 = h * (f((x0+h), (t0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        tn = t0 + k

        t0 = tn
        x0 = x0+h
        dis.append(x0)
        t_d.append(t0)
    print(c,', at',x ,' =',xn ,'and t =',tn ,', equals ',f(xn,tn))
    return f(xn,tn)

print('a)')
v = rk4(x0,t0,xn,step,'Velocity','x')

plt.figure()
plt.plot(dis, t_d, '-r', label = 'Theoretical displacement vs time plot')
plt.legend()

Accel = rk4(v,t0,xn,step,'Acceleration/-kx', 'v')

#-------------------------------------------------------------------

print('b)')

g = 0.5       #damping constant
rk4(Accel-g*v, t0, xn, step, 'Accel with damping/-kx-gamme*v', 'v')


#------------------------------------------------------------------



