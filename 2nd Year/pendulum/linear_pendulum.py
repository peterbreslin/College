#!/usr/bin/python

import pylab
import matplotlib.pyplot as plt
import numpy as np 
import math

#Script to solve the linear pendulum equation using the trapezoid rule

#Initialising values
theta = 0.2 
omega = 0.0
t = 0.0
dt = 0.01
nsteps = 0.0 

k = 0.0
phi = 0.66667
A = 0.0
g = 1.0
L = 1.0

def f(theta,omega,t):
	f = -(g/L) * (theta) - k*omega + (A * math.cos(phi) * t)  
	return f

#Checking that script works by printing values of f for several values for omega, theta and t
#theta = theta + 10.0
#omega = omega + 5.0
#t = t + 1.0

#min = 100.0
#while abs(theta) < min:
#	theta = theta + 10.0
#	omega = omega + 5.0
#	t = t + 1.0
#	print f(theta,omega,t)
	
#Loop for trapezoid rule equations 
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
	plt.plot(nsteps, theta, 'go', markersize = 2, label = 'Angle - Theta')
	plt.figure(1)
	plt.plot(nsteps, omega, 'bo', markersize = 2, label = 'Angular Frequency - Omega')

plt.figure(1)
plt.ylabel("Theta/Omega")
plt.xlabel("nsteps")
plt.title("Theta/Omega vs Number of Steps")
plt.axis([0,1000,-0.2,0.2])
plt.legend(loc='best')

############## these values will be changed each time, see table
theta = 0.2
omega = 0.0
##############

for nsteps in range(0,1000):
	nsteps = nsteps+1

	k1a = dt * omega 
	k1b = dt * f(theta, omega, t) 
	k2a = dt * (omega + k1b)
	k2b = dt * f(theta + k1a, omega + k1b, t + dt)
	theta = theta + (k1a + k2a)/2 
	omega = omega + (k1b + k2b )/2 
	t = t + dt 
	
	plt.figure(2)
	plt.plot(t, theta, 'co', markersize = 2, label = 'Theta vs Time')

	plt.figure(2)
	plt.plot(t, omega, 'ro', markersize = 2, label = 'Omega vs Time')

plt.figure(2)
plt.ylabel("Theta/Omega")
plt.xlabel("Time")
plt.title("Relationship Between Theta/Omega and Time")
plt.legend(loc='best')
plt.axis([0,10,-math.pi,math.pi])

plt.show()
