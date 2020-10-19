# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:07:57 2017

@author: pbreslin
"""

import matplotlib.pyplot as plt
import numpy as np
import math # need math module for trigonometric functions

g = 9.81                     # gravitational constant
dt = 1e-3                    # integration time step (delta t)
v0 = 40                      # initial speed at t=0    

angle=math.pi/4              # math.pi=3.14
                             # launch angle (in rad)

time=np.arange(0,10,dt)      # create time axis
vx0=math.cos(angle)*v0       # starting velocity along x
vy0=math.sin(angle)*v0       # starting velocity along y

xa=vx0*time                  # compute x coorordinates
ya=-0.5*g*time**2+vy0*time   # compute y coorordinates

fig1=plt.figure()
plt.plot(xa,ya)              # plot y versus x
plt.xlabel("x")
plt.ylabel("y")


# Ex. 1.2

def traj(angle,v0):          # function that computes trajectory
    vx0=math.cos(angle)*v0   # for some launch angle and starting velocity
    vy0=math.sin(angle)*v0   # compute x and y component of starting velocity
    x=np.zeros(len(time))    # initialise x,y arrays
    y=np.zeros(len(time))
    
    x[0], y[0]=0,0                     # projectile starts at (0,0)
    x[1], y[1]=x[0]+vx0*dt,y[0]+vy0*dt # second elements of x and y are determined by initial velocity
    
    i=1
    while y[i]>=0:                     # conditional loop continuous until projectile hits ground (occurs when y becomes negative)
        x[i+1]=(2*x[i]-x[i-1])         # numerical integration to find x[i+1] and y[i+1]
        y[i+1]=(2*y[i]-y[i-1])-g*dt**2
        
        i=i+1                          # increment i for for next iteration
        
    # while loop has finished - no more indent
    x=x[0:i+1]                         # truncate x and y arrays
    y=y[0:i+1]
    return x,y,(dt*i),x[i]             # return x, y, flight time, range of projectile
    
x, y, duration, distance = traj(angle,v0)
print ('Distance A:',distance)
print ('Duration A:',duration)


# Now for duration for angle of pi/5

g = 9.81                     # gravitational constant
dt = 1e-3                    # integration time step (delta t)
v0 = 40                      # initial speed at t=0    

angle=math.pi/5              # math.pi=3.14
                             # launch angle (in rad)

time=np.arange(0,10,dt)      # create time axis
vx0=math.cos(angle)*v0       # starting velocity along x
vy0=math.sin(angle)*v0       # starting velocity along y

xa=vx0*time                  # compute x coorordinates
ya=-0.5*g*time**2+vy0*time   # compute y coorordinates

fig1=plt.figure()
plt.plot(xa,ya)              # plot y versus x
plt.xlabel("x")
plt.ylabel("y")

def traj(angle,v0):          # function that computes trajectory
    vx0=math.cos(angle)*v0   # for some launch angle and starting velocity
    vy0=math.sin(angle)*v0   # compute x and y component of starting velocity
    x=np.zeros(len(time))    # initialise x,y arrays
    y=np.zeros(len(time))
    
    x[0], y[0]=0,0                     # projectile starts at (0,0)
    x[1], y[1]=x[0]+vx0*dt,y[0]+vy0*dt # second elements of x and y are determined by initial velocity
    
    i=1
    while y[i]>=0:                     # conditional loop continuous until projectile hits ground (occurs when y becomes negative)
        x[i+1]=(2*x[i]-x[i-1])         # numerical integration to find x[i+1] and y[i+1]
        y[i+1]=(2*y[i]-y[i-1])-g*dt**2
        
        i=i+1                          # increment i for for next iteration
        
    # while loop has finished - no more indent
    x=x[0:i+1]                         # truncate x and y arrays
    y=y[0:i+1]
    return x,y,(dt*i),x[i]             # return x, y, flight time, range of projectile
    
x, y, duration, distance = traj(angle,v0)
print ('Distance B:',distance)
print ('Duration B:',duration)


# Now for duartion for angle of pi/3 and an initial velocity of 15 m/s

g = 9.81                     # gravitational constant
dt = 1e-3                    # integration time step (delta t)
v0 = 15                      # initial speed at t=0    

angle=math.pi/3              # math.pi=3.14
                             # launch angle (in rad)

time=np.arange(0,10,dt)      # create time axis
vx0=math.cos(angle)*v0       # starting velocity along x
vy0=math.sin(angle)*v0       # starting velocity along y

xa=vx0*time                  # compute x coorordinates
ya=-0.5*g*time**2+vy0*time   # compute y coorordinates

fig1=plt.figure()
plt.plot(xa,ya)              # plot y versus x
plt.xlabel("x")
plt.ylabel("y")

def traj(angle,v0):          # function that computes trajectory
    vx0=math.cos(angle)*v0   # for some launch angle and starting velocity
    vy0=math.sin(angle)*v0   # compute x and y component of starting velocity
    x=np.zeros(len(time))    # initialise x,y arrays
    y=np.zeros(len(time))
    
    x[0], y[0]=0,0                     # projectile starts at (0,0)
    x[1], y[1]=x[0]+vx0*dt,y[0]+vy0*dt # second elements of x and y are determined by initial velocity
    
    i=1
    while y[i]>=0:                     # conditional loop continuous until projectile hits ground (occurs when y becomes negative)
        x[i+1]=(2*x[i]-x[i-1])         # numerical integration to find x[i+1] and y[i+1]
        y[i+1]=(2*y[i]-y[i-1])-g*dt**2
        
        i=i+1                          # increment i for for next iteration
        
    # while loop has finished - no more indent
    x=x[0:i+1]                         # truncate x and y arrays
    y=y[0:i+1]
    return x,y,(dt*i),x[i]             # return x, y, flight time, range of projectile
    
x, y, duration, distance = traj(angle,v0)
print ('Distance C:',distance)
print ('Duration C:',duration)


plt.show
