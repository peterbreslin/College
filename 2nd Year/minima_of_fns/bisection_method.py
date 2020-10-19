import pylab
import matplotlib.pyplot as plt
import numpy as np 
import math

#(s + 8)(s - 2) = s**2 + 6s - 16 ... equation of parabola

a = 1.0 
b = 6.0
c = -16.0
x = np.arange(-12.0, 7.0, 0.2)


# Defining the function for ease of use:

def f(s):
	
		return a * s * s   + b * s   + c


# Setting variables x1 and x3 so that f(x1) < 0 and f(x2) > 0:
x1 = -2.0
x3 = 3.0

# If statements to check if variables are correctly initialised:
if f(x1) < 0:
	print("x1 is CORRECTLY initialised.")
else: 
	print ("x1 is INCORRECTLY initialised.")

if f(x3) > 0:
	print("1 is CORRECTLY initialised.")
else: 
	print ("x1 is INCORRECTLY initialised.")

# Setting x2 to be equal to half the interval that x1 and x3 creates:
x2 = 0.5 * (x1 + x3)


# Adding if and else statements to update x1 or x3 to x2 according to the following conditions:

if f(x2) > 0:
    x3 = x2
else:  
	x1 = x2
print ("New x1, x3", x1, x3)


# Creating a loop to update x2 constantly while the absolute value of f(x2) is greater than the min. We set the min to be 0.0001:

min = 0.0001
while abs(f(x2)) > min:
	if f(x2) > 0:
		x3 = x2
		x2 = 0.5 * (x1 + x3)
	else:  
		x1 = x2
		x2 = 0.5 * (x1 + x3)


# First root is found when [ abs(f(x2)) < min ]:

if abs(f(x2)) < min:
	print (x2, f(x2))


# Now for second root:

y1 = -9.0
y3 = -4


if f(y1) > 0:
	print("y1 is Correct")
else: 
	print ("y1 is Incorrect")

if f(y3) < 0:
	print("y2 is Correct")
else: 
	print ("y2 is Incorrect")

y2 = 0.5 * (y1 + y3)



if f(y2) < 0:
    y3 = y2
else:  
	y1 = y2
print ("New y1, y3", y1, y3)

min = 0.0001
while abs(f(y2)) > min:
	if f(y2) < 0:
		y3 = y2
		y2 = 0.5 * (y1 + y3)
	if f(y2) > 0:  
		y1 = y2
		y2 = 0.5 * (y1 + y3)


if abs(f(y2)) > min:
	print (y2, f(y2))

#############################################

# Plotting the parabola:
plt.figure(1)

plt.plot(x, f(x))    
plt.plot(x, 0.0 * x) 

plt.title('Parabola')
plt.ylabel('y-axis')
plt.xlabel('x-axis')

#plt.text(-5.0, -4.0, 'x1 ~ (-3,0)')
#plt.text(2, -4.0, 'x2 ~ (2,0)')
  
# Plotting the first root (x2, f(x2)):

plt.plot(x2, f(x2), 'go')

# Plotting the second root (y2, f(y2)):
print(y2,f(y2))
plt.plot(y2, f(y2), 'go')	


plt.text(2.2, -5, '$x2$', fontsize=12, color = 'green',)
plt.text(-9.2, -5, '$x1$', fontsize=12, color = 'green',)


##########################################

#nsteps

my_tol = []
my_nsteps = []

min = 0.1

while min > 10.0**-14.0:

	y1 = -9
	y3 = -4
	y2 = 0.5 * (y1 + y3)
	nsteps = 0

	while abs(f(y2)) > min:
		if f(y2) < 0:
			y3 = y2
			y2 = 0.5 * (y1 + y3)
		if f(y2) > 0:  
			y1 = y2
			y2 = 0.5 * (y1 + y3)
		nsteps = nsteps + 1

	min = min * 0.1

	my_nsteps.append(nsteps)
	my_tol.append(-1.0*math.log10(min))

print "Number of steps: " + str(nsteps) 

plt.figure(2)
line = plt.plot(my_tol,my_nsteps)
plt.scatter(my_tol, my_nsteps)
plt.title('Relationship between nsteps and the minimum')
plt.ylabel('-nsteps')
plt.xlabel('-1 log(10)')
plt.setp(line, color='g', linewidth=2.0)


plt.show()
