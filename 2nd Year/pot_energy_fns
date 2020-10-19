import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np 
import math

S = 1.44
# Letting S be equal to ((e**2.0)/(4.0 * pi * EpsilonZero))
A = 1090.0 
p = 0.033


def V(x):
	V = A * np.exp(-x/p) - S/x
	return V

plt.figure(1)
x = np.arange(0.1, 1.0, 0.01)
plt.plot(x, x*0, 'k')
plt.plot(x, V(x), 'r')
plt.title("V(x) and V'(x)")
plt.xlabel("Distance")
plt.ylabel("Energy")

def dV(x):
	dV = ((-A * np.exp(-x/p))/p) + S/x**2.0
	return dV

# Plotting -dV
plt.figure(1)
x = np.arange(0.2, 1.0, 0.01)
plt.plot(x, -dV(x), 'c') 

plt.figure(1)
plt.plot(x, V(x), 'r', label='V(x)')
plt.plot(x, -dV(x), 'c', label="V'(x)")
plt.legend(loc='upper right')  

#plt.show()

def ddV(x):
	ddV = ((A * np.exp(-x/p))/p**2.0) - (2.0*S)/x**3.0
	return ddV

# Plotting ddV
plt.figure(2)
x = np.arange(0.1, 1.0, 0.01)
plt.plot(x, x*0, 'k')
plt.plot(x, ddV(x), 'g')
plt.title("V''(x)")
plt.xlabel("Distance")
plt.ylabel("Energy")

plt.plot(x, ddV(x), 'g', label="V''(x)")
plt.legend(loc='upper right')  


#plt.show()

# Using the NR method to find x -> the minimum value for V(x):
x1 = 0.2
if V(x1) < 0:
	print("x1 is initialised")
else: 
	print ("x1 is not initialised")
 
x1 = x1 - dV(x1)/ddV(x1)

min = 0.0001
nsteps = 0

while abs(dV(x1)) > min:
	x1 = x1 - dV(x1)/ddV(x1)
	nsteps += 1
print "The value of x found using NR is " + str(x1)
print "The value fond for V(x) is " + str(V(x1))
print "Number of steps = " + str(nsteps)

plt.show()

x = np.arange(0.1, 1.0, 0.01)
plt.plot(x, x*0, 'k')
plt.plot(x, V(x), 'b')

plt.plot(x1, V(x1), 'ro')
plt.title("Minimum Value of V(x)")
plt.xlabel("Distance")
plt.ylabel("Energy")

plt.plot(x, V(x), 'b', label="V(x)")
plt.plot(x1, V(x1), 'ro', label='minimum')
plt.legend(loc='upper right')  


plt.show()
