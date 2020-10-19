#!/usr/bin/python

import pylab
import matplotlib.pyplot as plt
import numpy as np 
import math

#Script to solve the damped nonlinear pendulum 

#Initialising values
t = 0.0
dt = 0.01
nsteps = 0.0 

k = 0.5 #...friction (damping)
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
	plt.plot(t, theta, 'go', markersize = 2)

	plt.figure(2)
	plt.plot(t, omega, 'co', markersize = 2)

plt.figure(1)
plt.ylabel("Theta")
plt.xlabel("t")
plt.title("Theta vs Time with Damping")
plt.axis([0,10,-math.pi,math.pi])

plt.figure(2)
plt.ylabel("Omega")
plt.xlabel("t")
plt.title("Omega vs Time with Damping")
plt.axis([0,10,-math.pi,math.pi])

plt.show()
