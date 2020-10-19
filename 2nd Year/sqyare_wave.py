#!/usr/bin/python
import pylab
import matplotlib.pyplot as plt
import numpy as np 
import math

def simpsons_rule(f, a, b, n):
	h = (b-a)/n
	d = 0

	x = a + h
	for i in range(1, n/2 + 1):	#50 divided by 2 would be 24 in python, so 1 is added
		d = d + 4*f(x)
		x = x + 2*h

	x = a + 2*h
	for i in range(1, n/2):
		d = d + 2*f(x)
		x = x + 2*h

	return (h/3) * (f(a) + f(b) + d)

#Analytic Square Wave
x_values = np.arange(0, 4*np.pi, 0.01)
y_values = []
for i in x_values:
	if 0.0 < i < np.pi or 2*np.pi < i < 3*np.pi:
		y_values.append(1)
	elif np.pi < i < 2*np.pi or 3*np.pi < i < 4*np.pi:
		y_values.append(-1)
	else:
		y_values.append(0)
		
plt.figure(1)
plt.plot(x_values, y_values, 'r', linewidth = 1.50, label = "Analytic Square Wave")

#Reconstructed Square Wave
def square_wave(x):
	if x > np.pi:
		return -1
	if x < np.pi:
		return 1

w = 1
ak_list = []
bk_list = []

for k in range(1,30,1):

	def a0_terms(x):
		return square_wave(x)

	def sin_terms(x):
		sin_terms = square_wave(x) * np.sin(k*w*x)
		return sin_terms

	def cos_terms(x):
		cos_terms = square_wave(x) * np.cos(k*w*x)
		return cos_terms

	a_0 = simpsons_rule(a0_terms, 0.0, 2*np.pi, 100)/np.pi
	a_k = simpsons_rule(cos_terms, 0.0, 2*np.pi, 100)/np.pi
	b_k = simpsons_rule(sin_terms, 0.0, 2*np.pi, 100)/np.pi

	ak_list.append(a_k)
	bk_list.append(b_k)

print ak_list, bk_list


total = 0

def periodic_fourier_series(t, ak_list, bk_list, a_0):
	total = 0
	for n in range(1, len(ak_list)):
		total += ak_list[n-1] * np.cos(n*w*t) + bk_list[n-1]*np.sin(n*w*t)
	total += a_0
	return total
t = np.arange(0, 4*np.pi, 0.01)

plt.figure(1)
plt.title('Reconstructed and Exact Square Wave Comparison') 
plt.plot(t, periodic_fourier_series(t, ak_list, bk_list, a_0), label = 'Reconstructed Square Wave (N = 30)') 
plt.xlabel('t')
plt.ylabel('f(t)')

plt.ylim([-2, 2])
plt.legend(loc = "best")
plt.axhline(y = 0, color = 'k')

plt.annotate('Gibbs Phenomenon', xy=(9.4, -1.2), xytext=(6, -1.7), arrowprops=dict(facecolor='black', arrowstyle = "->",))

plt.show()
