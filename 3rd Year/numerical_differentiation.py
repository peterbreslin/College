'''
Assignment 1: Numerical Differentiation
Name: Peter Breslin
ID: 17340915
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

print('Name: Peter Breslin\nStudent ID: 17340915')
#Part 1 - Plotting the analytical and numerical results

def function(x):
    """ define function to be differentiated"""
    f = np.cos(x)
    return f
    
def analytic(x):
    """analytic derivative"""
    f = -np.cos(x)
    return f

def central(x,h):
    f = ( function(x+h) - 2*function(x) + function(x-h) ) / (h**2)
    return f
    
x=np.arange(0, 4*np.pi, 0.001);

plt.figure(1)
plt.xlabel('Range: [0:4pi]')
plt.ylabel('f(x)')
plt.title('Test function f(x) = cos(x)')
plt.plot(x,function(x))
plt.grid()
#plt.show()

plt.figure(2)
plt.xlabel('Range: [0:4pi]')
plt.ylabel('f"(x)')
plt.title('Analytical result: 2nd derivative of the function f(x) = cos(x)')
plt.plot(x,analytic(x))
plt.grid()
#plt.show()

plt.figure(3)
plt.xlabel('Range: [0:4pi]')
plt.ylabel('f"(x)')
plt.title('Numerical result: 2nd derivative of the function f(x) = cos(x)')
plt.plot(x,central(x, 0.001))
plt.grid()
#plt.show()

#Errors - Part 2 and 3

x=np.arange(0, 4*np.pi, 0.001);

def abs_error(x):
    f = abs(central(x,0.001)-analytic(x))
    return f
    
plt.figure(4)
plt.xlabel('Range: [0:4pi]')
plt.ylabel('Absolute error')
plt.title('Variation of the absolute error')
plt.plot(x,abs_error(x))
plt.grid()
plt.show()

'''
#step_size = []
#for h in range(10**-7, np.pi/10)

x = np.arange(10**-7, np.pi/10);
y = np.arange(0, 4*np.pi);

def rel_error(x):
    f = abs(central(x,10**-7)-analytic(x) / analytic(x))
    return f

print(rel_error(x))


plt.figure(5)
plt.xlabel('step size h')
plt.ylabel('relative error')
plt.title('Relationship between the error and step-size')
plt.loglog(x,rel_error(x))
plt.show()


def central_error(y):
    f = abs(central(1,y)-analytic(1))
    return f
    
plt.figure(5)
plt.xlabel('Step size h')
plt.ylabel('Absolute error')
plt.title('Variation of the absolute error')
plt.loglog(x,abs_error(x))
plt.grid()
plt.show()
'''


#Subtractive Cancellation method 2nd Derivative    
def sub_method(x,h): 
	f = (((function(x+h) - function(x)) - (function(x) - function(x-h))) / (h**2))
	return f
    
def sub_rel(x):
	f = abs(sub_method(x,0.001) - analytic(x))
	return f

plt.figure(6)
plt.xlabel('Range: [0:4pi]')
plt.ylabel('Absolute error using Subtractive Cancellation')
plt.title('Variation of the absolute error')
plt.plot(x,sub_rel(x))
plt.grid()
plt.show()

plt.figure(7)
plt.xlabel('Range: [0:4pi]')
plt.ylabel('Absolute error')
plt.title('Variation of the absolute error for both methods')
plt.plot(x,abs_error(x), 'r', linewidth = 2, label = 'C-D Method')
plt.plot(x,sub_rel(x), 'k--', markersize = 1, label = 'S-C Method')
plt.grid()
plt.legend(loc='best')
plt.show()
