#!/usr/bin/python

import pylab
import matplotlib.pyplot as plt
import numpy as np 
import math

#Script to solve the nonlinear pendulum equation using the Runge-Kutta algorithm

#Initialising values
t = 0.0
dt = 0.01
nsteps = 0.0 

k = 0.0
phi = 0.66667
A = 0.0
g = 1.0
L = 1.0

theta = 3.0
omega = 0.0


def f(theta,omega,t):
	f = -(g/L) * math.sin(theta) - k*omega + (A * math.cos(phi) * t)  
	return f

for nsteps in range(0,1000):
	nsteps = nsteps+1

	k1a = dt * omega 
	k1b = dt * f(theta, omega, t) 
	k2a = dt * (omega + k1b)
	k2b = dt * f(theta + k1a, omega + k1b, t + dt)

	theta = theta + (k1a + k2a)/2 
	omega = omega + (k1b + k2b )/2 
	t = t + dt 
	
	plt.figure(1)
	plt.plot(t, theta, 'mo', alpha = 0.7, markersize = 4, label = 'Trapezoidal Method')
	#plt.figure(2)
	#plt.plot(t, omega, 'rs', markersize = 2)


#Re-initialising values
t = 0.0
dt = 0.01
nsteps = 0.0 

k = 0.0
phi = 0.66667
A = 0.0
g = 1.0
L = 1.0

theta = 3.0
omega = 0.0

for nsteps in range(0,1000):
	nsteps = nsteps+1

	k1a = dt * omega 
	k1b = dt * f(theta, omega, t) 

	k2a = dt * (omega + k1b/2)
	k2b = dt * f(theta + k1a/2, omega + k1b/2, t + dt/2)

	k3a = dt * (omega + k2b/2) 
	k3b = dt * f(theta + k2a/2, omega + k2b/2, t + dt/2)

	k4a = dt * (omega + k3b)
	k4b = dt * f(theta + k3a, omega + k3b, t + dt)

	theta = theta + (k1a + 2*k2a + 2*k3a + k4a)/6 
	omega = omega + (k1b + 2*k2b + 2*k3b + k4b)/6  
	t = t + dt	

	plt.figure(1)
	plt.plot(t, theta, 'cs', markersize = 2, label = 'Runge-Kutta Method')
	#plt.figure(2)
	#plt.plot(t, omega, 'co', markersize = 2)

plt.figure(1)
plt.ylabel("Theta")
plt.xlabel("t")
plt.title("Theta vs Time for Trapezoidial/Runge-Kutta Method")
plt.legend(loc='best')
plt.axis([0,10,-math.pi,math.pi])

plt.show()
