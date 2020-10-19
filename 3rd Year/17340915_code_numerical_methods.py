# -*- coding: utf-8 -*-
"""
Numerical solution of an ordinary differential equation

@author: Peter Breslin
"""

import numpy as np
import matplotlib.pyplot as plt

print("Name: Peter Breslin \nStudent Number: 17340915")

#Function
def ode(t,x):
    return (1+t)*x + 1 - (3*t) + (t**2) 

x = np.linspace(-3, 3, 25)
t = np.linspace(0, 5, 25)

tp, xp = np.meshgrid(t, x)

z = ode(tp,xp)
n = np.sqrt(z**2 + 1)            #normalize the vectors so that the arrows are the same length

#h = plt.contourf(x,t,z)

fig, ax = plt.subplots(figsize=(10,10))
plt.title('Direction field')
plt.xlabel('t')
plt.ylabel('x')
ax.quiver(tp, xp, 1/n, z/n, color='r')
#plt.show()

################################################################################


#Simple euler method 
def simple_euler(x, t, step_size):             
    return t + step_size*ode(x,t)

#Improved euler method
def improved_euler(x, t, step_size):
    return t + 0.5*step_size * ( ode(x,t) + ode(x+step_size, t + step_size*ode(x,t)) )

#Runge-Kutta Method
def runge_kutta(x, t, step_size):
    k1 = ode(x,t)
    k2 = ode(x + 0.5*step_size, t + 0.5*step_size*k1)
    k3 = ode(x + 0.5*step_size, t + 0.5*step_size*k2)
    k4 = ode(x + step_size, t + step_size*k3)
    
    return t + (step_size/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4) 

################################################################################


#Need to set the x and y initial values as well as define the step_size
step_size = 0.04; start = 0.0; end = 4.0    #step_size changed to 0.02 for the final part

#starting value x(t=0) = 0.0655
t0 = 0.0655       

#number of steps = k
k = int((end - start) / step_size)

#array for the iteration
it = np.arange(start, end, step_size)

SE = np.zeros(k)
IE = np.zeros(k)
RK = np.zeros(k)

IE[0] = t0
SE[0] = t0
RK[0] = t0

################################################################################


#Need to increment the solutions obtained
for i in range(1,k):
    SE[i] = simple_euler(it[i-1], SE[i-1], step_size)
    IE[i] = improved_euler(it[i-1], IE[i-1], step_size)
    RK[i] = runge_kutta(it[i-1], RK[i-1], step_size)

################################################################################


fig, ax = plt.subplots(figsize=(10,10))
line1,= ax.plot(it, SE, 'b', linewidth=2)
line2, = ax.plot(it, IE, 'g', linewidth=2)
line3, = ax.plot(it, RK, 'k', linewidth=2)
plt.xlim(0, 5)
plt.ylim(-3, 3)
ax.quiver(tp, xp, 1/n, z/n, color='r')
plt.title('Method comparison: step-size = 0.02')
plt.xlabel('t')
plt.ylabel('x')
plt.legend([line1,line2,line3],['Simple Euler','Improved Euler', 'Runge-Kutta'],loc=2)
#plt.savefig('num_methods_002.png', bbox_inches='tight')

plt.show()

###############################################################################
###############################################################################

'''
#comparison for step size = 0.04 and 0.02

#Function
def ode(t,x):
    return (1+t)*x + 1 - (3*t) + (t**2) 

#Simple euler method 
def simple_euler(x, t, step_size):             
    return t + step_size*ode(x,t)

#Improved euler method
def improved_euler(x, t, step_size):
    return t + 0.5*step_size * ( ode(x,t) + ode(x+step_size, t + step_size*ode(x,t)) )

#Runge-Kutta Method
def runge_kutta(x, t, step_size):
    k1 = ode(x,t)
    k2 = ode(x + 0.5*step_size, t + 0.5*step_size*k1)
    k3 = ode(x + 0.5*step_size, t + 0.5*step_size*k2)
    k4 = ode(x + step_size, t + step_size*k3)
    
    return t + (step_size/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4) 

################################################################################


#Need to set the x and y initial values as well as define the step_size
step_size = 0.02; start = 0.0; end = 4.0

#starting value x(t=0) = 0.0655
t0 = 0.0655       

#number of steps = k
k = int((end - start) / step_size)

#array for the iteration
it2 = np.arange(start, end, step_size)

SE2 = np.zeros(k)
IE2 = np.zeros(k)
RK2 = np.zeros(k)

IE2[0] = t0
SE2[0] = t0
RK2[0] = t0

################################################################################


#Need to increment the solutions obtained
for i in range(1,k):
    SE2[i] = simple_euler(it2[i-1], SE2[i-1], step_size)
    IE2[i] = improved_euler(it2[i-1], IE2[i-1], step_size)
    RK2[i] = runge_kutta(it2[i-1], RK2[i-1], step_size)


fig1, ax1 = plt.subplots(figsize=(10,10))
line1,= ax1.plot(it, SE, 'k', linewidth=2)
line2,= ax1.plot(it2, SE2, 'g', linewidth=2)
plt.title('Comparison of step-sizes: Simple Euler')
plt.xlim(0, 5)
plt.ylim(-3, 3)
ax1.quiver(tp, xp, 1/n, z/n, color='r')
plt.xlabel('t')
plt.ylabel('x')
plt.legend([line1,line2],['step-size = 0.04', 'step-size = 0.02'], loc=2)
#plt.savefig('simple_sizes.png', bbox_inches='tight')

fig2, ax2 = plt.subplots(figsize=(10,10))
line3, = ax2.plot(it, IE, 'k', linewidth=2)
line4, = ax2.plot(it2, IE2, 'g', linewidth=2)
plt.title('Comparison of step-sizes: Improved Euler')
plt.xlim(0, 5)
plt.ylim(-3, 3)
ax2.quiver(tp, xp, 1/n, z/n, color='r')
plt.xlabel('t')
plt.ylabel('x')
plt.legend([line3,line4],['step-size = 0.04', 'step-size = 0.02'], loc=2)
#plt.savefig('improved_sizes.png', bbox_inches='tight')

fig3, ax3 = plt.subplots(figsize=(10,10))
line5, = ax3.plot(it, RK, 'k', linewidth=2)
line6, = ax3.plot(it2, RK2, 'g--', linewidth=2)
plt.title('Comparison of step-sizes: Runge-Kutta')
plt.xlim(0, 5)
plt.ylim(-3, 3)
ax3.quiver(tp, xp, 1/n, z/n, color='r')
plt.xlabel('t')
plt.ylabel('x')
plt.legend([line5,line6],['step-size = 0.04', 'step-size = 0.02'], loc=2)
#plt.savefig('rk_sizes.png', bbox_inches='tight')


plt.show()

'''