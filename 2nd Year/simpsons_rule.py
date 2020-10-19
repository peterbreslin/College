#!/usr/bin/python
import pylab
import matplotlib.pyplot as plt
import numpy as np 
import math

def f(x):
	f = math.exp(x)
	return f
print "Integral calculated by normal integration technique = " + str((f(1) - f(0))) 

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
print "Integral calculated from Simpson's Rule = " + str(simpsons_rule(f, 0.,1.,50))

w = 1

def f1(x):
	f1 = math.sin(w*x)
	return f1

def f2(x):
	f2 = math.cos(w*x) + 3*math.cos(2*w*x) - 4*math.cos(3*w*x)
	return f2

def f3(x):
	f3 = math.sin(w*x) + 3*math.sin(3*w*x) + 5*math.sin(5*w*x)
	return f3

def f4(x):
	f4 = math.sin(w*x) + 2*math.cos(3*w*x) + 3*math.sin(5*w*x)
	return f4

ak_list = []
bk_list = []

for k in range(1,7,1):

#will be changed for f1 to f4
	def sin_terms(x):
		sin_terms = f1(x) * math.sin(k*w*x)
		return sin_terms

	def cos_terms(x):
		cos_terms = f1(x) * math.cos(k*w*x)
		return cos_terms

	a_k = simpsons_rule(cos_terms, 0.0, 2*math.pi, 50)/math.pi
	b_k = simpsons_rule(sin_terms, 0.0, 2*math.pi, 50)/math.pi

	ak_list.append(a_k)
	bk_list.append(b_k)

print ak_list, bk_list

plt.figure(1)
plt.title('a_k and b_k values')
#plt.plot(ak_list, 'r', linewidth = 1)
plt.plot(ak_list, 'bo', markersize = 5, label = 'a_k discrete points')

plt.figure(1)
#plt.plot(bk_list, 'm', linewidth = 1)
plt.plot(bk_list, 'mo', markersize = 5, label = 'b_k discrete points')
plt.xlabel('x')
plt.ylabel('y')

plt.legend(loc = 'best')

plt.show()
