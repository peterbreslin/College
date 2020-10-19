import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np 
import math

#(s + 8)(s - 2) = s**2 + 6s - 16 ... equation of parabola

a = 1.0 
b = 6.0
c = -16.0
#h = 10.0**-12.0
x = np.arange(-12.0, 7.0, 0.2) 

def f(s):
	f = a * s * s   + b * s + c
	return f

# Finding the derivaive of f(s):
def g(s):
	#g = ((f(s) + h) - f(s)) / h
	g = 2.0*a*s + 6.0
	return g

# Now for finding the roots of the parabola using the NR method:
x1 = 1.0
x2 = -6.0

if f(x1) < 0 and f(x2) < 0:
	print("x1 and x2 are initialised")
else: 
	print ("x1 and x2 are not initialised")

x1 = x1 - f(x1)/g(x1)
x2 = x2 - f(x2)/g(x2)

plt.plot(x2, f(x2), 'gs', markersize = 5)
plt.text(-8, 10, 'Initial Point', fontsize=12, color = 'green',)



# Loop to update x1 and x2 iteratively using the Newton-Raphson rule while the absolute value of f(x1) and f(x2) is greater than the min:
min = 0.0001
while abs(f(x1)) > min and abs(f(x2)) > min:
	x1 = x1 - f(x1)/g(x1)
	x2 = x2 - f(x2)/g(x2)

if abs(f(x1)) < min: 
	print 'root x1 = ' + str(x1) + " , " + str(f(x1))		#correct roots shown!
if abs(f(x2)) > min:
	print 'root x2 = ' + str(x2) + " , " + str(f(x2))		#correct roots shown!


#nsteps

my_tol = []
my_nsteps = []

min = 0.1

while min > 10.0**-14.0:
	x3 = 1
	nsteps = 0
	while abs(f(x3)) > min:
		x3 = x3 - f(x3)/g(x3)
		nsteps = nsteps + 1
		
	min = min * 0.1
	my_nsteps.append(nsteps)
	my_tol.append(-1.0*math.log10(min))

print "Number of steps: " + str(nsteps) 


plt.plot(x, f(x))    
plt.plot(x, g(x))
plt.plot(x, (0*x), 'k') 

plt.plot(x, f(x), 'b', label='f(s)')
plt.plot(x, g(x), 'r', label='g(s)')
plt.legend(loc='upper left')   

plt.title('f(s) and it\'s derivative, g(s) ')
plt.ylabel('y-axis')
plt.xlabel('x-axis')

plt.plot(x1, f(x1), 'ro')
plt.plot(x2, f(x2), 'ro')

plt.text(2.2, -5, '$x2$', fontsize=12, color = 'red',)
plt.text(-9.2, -5, '$x1$', fontsize=12, color = 'red',)



#plt.plot(x1,f(x1),'o')
plt.figure()
line = plt.plot(my_tol,my_nsteps)
plt.scatter(my_tol, my_nsteps)
plt.title('Relationship between nsteps and the minimum using NR method')
plt.ylabel('number of steps')
plt.xlabel('-1 log(10) of minimum tolerence')
plt.setp(line, color='g', linewidth=2.0)


plt.show()
