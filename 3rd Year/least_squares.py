# Assignment 3: Least Sqaures Fit

print("Name: Peter Breslin \nStudent ID: 17340915")

import numpy as np
import matplotlib.pyplot as plt
#import scipy.optimize as leastsq
from scipy import optimize


# Data to plot:

T = [5,15,25,35,45,55,65,75,85,95,105,115]			# T = decay times in seconds
N = [32,17,21,7,8,6,5,3,4,1,5,1]					# N = number of decays 

plt.figure(1)
plt.plot(T, N, 'g--', marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Number of decays')
plt.title('Linear Plot')
plt.grid(True)


# log-lin plot

plt.figure(2)
plt.plot(T, N, 'b--', marker='o')
plt.yscale('log')
plt.xscale('linear')
plt.xlabel('Time (s)')
plt.ylabel('log(no. decays)')
plt.title('Semilog plot')
plt.grid(True)


#Mean values
X = np.log(N)
T_mean = np.mean(T)
N_mean = np.mean(X)

#T = mN + c

#Slope m
top = 0
bottom = 0

Z = len(T)
for i in range(Z): 
	top += (T[i] - T_mean)*(X[i] - N_mean)
	bottom += (T[i] - T_mean)**2

m = top / bottom
c = N_mean - m*T_mean

#Parameters
print(m, c)
print(np.exp(c))

x = np.arange(0,115)

Y = m*x + c

plt.figure(3)
plt.plot(T, N, 'g--', marker='o')
plt.plot(x, Y, 'm')
plt.xlabel('Time (s)')
plt.ylabel('Number of decays')
plt.title('Linear plot with fit')
plt.grid(True)

plt.figure(4)
plt.plot(T, N, 'b--', marker='o')
plt.plot(x, np.exp(m*x + c), 'm')
plt.yscale('log')
plt.xscale('linear')
plt.xlabel('Time (s)')
plt.ylabel('log(no. decays)')
plt.title('Semilog plot with fit')
plt.grid(True)

#Function to fit to --> y = mx + c

def func(x, m, c):
    return np.exp(m*x + c)
    
#Square residuals function

def res_func(h, y, x):
    m, c = h
    return y - func(x, m, c)

t = np.linspace(5,115,12)
true_y = func(t, m, c)
y0 = N	#y to fit on

T2 = np.array([5,15,25,35,45,55,65,75,85,95,105,115])
N2 = np.array([32,17,21,7,8,6,5,3,4,1,5,1])


#Guess
h0 = -0.1, 30
fit = optimize.leastsq(res_func, h0, args=(N, t))

fitted_y = func(t, fit[0][0], fit[0][1])
print(fitted_y)

plt.figure(5)
plt.plot(t, true_y, 'g', label = 'True value')
plt.plot(t, N, 'c--', marker='o', label = 'Fit data')
plt.plot(t, fitted_y, 'red', label = 'Fit')
plt.xlabel('Time (s)')
plt.ylabel('Number of decays')
plt.title('Decays vs Time')
plt.legend()

plt.show()
