#!/usr/bin/python
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np 
import math
#plt.switch_backend("Qt4agg")

==================================================================================================

# How the air resistance scales with velocity:

D = 1
V = np.arange(0.000005,5.0,0.001) 
DV = D*V

def air_res_linear(V,D):
	B = 0.0016
	C = 0.25
	result = B*D*V
	return result

def air_res_quadratic(V,D):
	B = 0.0016
	C = 0.25
	result = C*D*V*D*V
	return result

def air_res_both(V,D):
	B = 0.0016
	C = 0.25
	result = B*D*V + C*D*V*D*V
	return result

plt.title('Air Resistance vs Velocity')
plt.xlabel('Product of D and V')
plt.ylabel('Air Resistance')

plt.loglog(DV,air_res_both(V,D),'r',label='both terms included')
plt.loglog(DV,air_res_linear(V,D),'g--',label='negligible quadratic term (linear)')
plt.loglog(DV,air_res_quadratic(V,D),'b--',label='linear term neglected (quadratic)')

plt.legend(loc='best')

#part b can be done by observing the graph: 10**-5-ish range is linear, 10**0-ish range is quadratic while in between-ish is both!

plt.show()

==================================================================================================

# Vertical Velocity:
import matplotlib.patches as mpatches

g = -9.8
b = 1.6*10.0**-8.0
m = 1.05*10.0**-9.0
#for large mass (b/m) will go to 0 meaning that it will just keep accelerating
dt = 0.0001
tmax = 1.5
t = 0.0
Vy = 0.0
h = -5
e = 2.71828

#numerical solution
time_list = []
num_velocity_list = []

while t < tmax:
	time_list.append(t)
	num_velocity_list.append(Vy)
	dVy = -g*dt - (b/m)*Vy*dt
	Vy = Vy + dVy
	t = t + dt

#analytical solution	
def V_a(t):
	return(m*g/b)*(e**((-b*t/m))-1)
	
t_a = 0.0
Vy_a = 0.0

atl_velocity_list = []

while t_a < tmax:
	atl_velocity_list.append(Vy_a)
	Vy_a =  V_a(t_a)
	t_a = t_a + dt
	

plt.figure(1)
plt.xlabel('Time')
plt.ylabel('Vertical Velocity')
plt.plot(time_list,num_velocity_list,'k', linewidth = 2, label = 'Numerical solution')
plt.title('Comparison of the Numerical & Analytical solutions')
plt.figure(1)
plt.plot(time_list,atl_velocity_list,'c--', linewidth = 1.5, label = 'Analytical solution')
plt.legend(loc='best')


#'''
mass_list = []
tfall = []

while m < 10.0**3.0:
	mass_list.append(m)
	while h < 0:
		Vy =  V_a(t)
		t = t + dt
		h = h + Vy*dt
	tfall.append(t)
	m = m * 2
	h = -5
	t = 0.0
	Vy = 0.0

#print tfall,mass_list
plt.figure(2)
plt.ylabel('Time')
plt.xlabel('Mass')
plt.title('Mass of Particle vs Time Taken to Reach Ground')
plt.plot(mass_list,tfall,'m', linewidth = 2)
plt.plot(mass_list,tfall,'go', markersize = 3, label = 'Particles of Different Mass')
plt.legend(loc = 'best')
#plt.yscale('log')
plt.xscale('log')

#'''

plt.show()

==================================================================================================

# Time as fn of mass:

g = -9.8
b = 1.6*10.0**-8.0
m = 1.05*10.0**-9.0
dt = 0.001
tmax = 1.5
t = 0.0
Vy = 0.0
h = -5
e = 2.71828

def V_a(t):
	return(m*g/b)*(e**((-b*t/m))-1)

mass_list = []
tfall = []

while m < 10.0**3.0:
	mass_list.append(m)
	while h < 0:
		Vy =  V_a(t)
		t = t + dt
		h = h + Vy*dt
	tfall.append(t)
	m = m * 2
	h = -5
	t = 0.0
	Vy = 0.0

#print tfall,mass_list
plt.figure(1)
plt.ylabel('Time')
plt.xlabel('Mass')
plt.title('Mass of Particle vs Time to Reach Ground')
plt.plot(mass_list,tfall,'m')
plt.plot(mass_list,tfall,'ko', markersize = 2)
plt.plot(1.05*10.0**-9.0,7.841000000000953, 'bo', label = '1.05E-9')
plt.plot(4.2*10.0**-9.0,2.206999999999868, 'ro', label = '4.2E-9')
plt.plot(1.68*10.0**-8.0, 1.2029999999999783, 'yo', label = '1.68E-8')
plt.plot(6.88*10.0**-5.0, 1.0109999999999995, 'go', label = '6.88E-5')
plt.plot(50, 1.0109999999999995, 'co', label = '50')
#plt.yscale('log')
plt.legend(loc='best', title = 'Mass (kg)')
plt.xscale('log')

plt.show()

#after about 10^-2 it falls off exponentially

==================================================================================================

# Trajectory - linear dependance:

g = 9.8
b = 1.6*10.0**-8.0
m = 1.05*10.0**-9.0
dt = 0.0001
t = 0.0
Vy = 0.0
Vx = 0.0
y = 0
x = 0

initial_vel = 0.5
angle = np.pi/3
Vy_0 = initial_vel * np.sin(angle) 
Vx_0 = initial_vel * np.cos(angle)
Vy = Vy_0 
Vx = Vx_0 

#with Air Resistance
velocity_y = []
velocity_x = []

while y >= 0.0:
	velocity_y.append(y)
	velocity_x.append(x)
	t = t + dt
	Vy = Vy - g*dt - (b/m)*Vy*dt
	Vx = Vx - (b/m)*Vx*dt
	y = y + dt*Vy
	x = x + dt*Vx
t = 0
Vy = Vy_0 
Vx = Vx_0 
y = 0
x = 0

#without Air Resistance
velocity_ay = []
velocity_ax = []

while y >= 0.0:
	velocity_ay.append(y)
	velocity_ax.append(x)
	t = t + dt
	Vy = Vy - g*dt
	y = y + dt*Vy
	x = x + dt*Vx

plt.figure(1)
plt.xlabel('x - direction')
plt.ylabel('y - direction')
plt.title ('Trajectory of Particle in Motion')

plt.plot(velocity_x,velocity_y,'r', linewidth = 2, label = 'With Air Resistance')
plt.plot(velocity_ax,velocity_ay,'c', alpha = 0.7, linewidth = 2, label = 'Without Air Resistance')
plt.legend(loc=2)
plt.show()

==================================================================================================

# Optimum Launch Angle:

g = 9.8
b = 1.6*10.0**-8.0
m = 1.05*10.0**-9.0
dt = 0.001
t = 0.0
Vy = 0.0
Vx = 0.0
y = 0
x = 0

initial_vel = 5
angle = np.pi/2
Vy_0 = initial_vel * np.sin(initial_vel) 
Vx_0 = initial_vel * np.cos(initial_vel)
angle_list = np.arange(0, np.pi/2, 0.001)
displacement = []

for i in angle_list:
	#print(i)
	Vy = initial_vel * np.sin(i) 
	Vx = initial_vel * np.cos(i)
	t = 0
	x = 0
	y = 0
	while y >= 0:
		t = t + dt
		Vy = Vy - g*dt - (b/m)*Vy*dt
		Vx = Vx - (b/m)*Vx*dt
		y = y + dt*Vy
		x = x + dt*Vx
	displacement.append(x)

max_displacement = 0
optimum_angle = 0

for j in range (0, len(displacement)):
	if displacement[j] > max_displacement:
		max_displacement = displacement[j]
		optimum_angle = angle_list[j]
		
print "Optimum Angle = " + str(optimum_angle)
print "Max displacement = " + str(max_displacement)

plt.title('Optimal Launch Angle for Maxiumum Horizontal Displacement')
plt.ylabel('Horizontal Displacement')
plt.xlabel('Launch Angle (rad)')
plt.plot(angle_list, displacement, 'c', linewidth = 2)
plt.show()

==================================================================================================

# Opt. launch angle as fn of mass:

g = 9.8
b = 1.6E-8
dt = 0.001
m = 1.05E-9
t = 0.0
y = 0
x = 0

initial_vel = 5
angle_list = np.arange(0, np.pi/2, 0.001)
displacement = []

def h(m):
	displacement = []
	for i in angle_list:
			Vy = initial_vel * np.sin(i) 
			Vx = initial_vel * np.cos(i)
			t = 0
			x = 0
			y = 0
			while y >= 0:
				t = t + dt
				Vy = Vy - g*dt - (b/m)*Vy*dt
				Vx = Vx - (b/m)*Vx*dt
				y = y + dt*Vy
				x = x + dt*Vx
			displacement.append(x)

	max_displacement = 0
	optimum_angle = 0

	for j in range (0, len(displacement)):
		if displacement[j] > max_displacement:
			max_displacement = displacement[j]
			optimum_angle = angle_list[j]
	return optimum_angle

#Different Masses

mass = [1E-9, 1E-7, 1E-5, 1E-3, 1E-1, 1E2]
#mass = [1E-10, 1E-9, 1E-8, 1E-7, 1E-6, 1E-5, 1E-4, 1E-3]
optimum_mass = []
for k in mass:
	optimum_mass.append(h(k))
	
plt.figure(1)
plt.title('Optimum Launch Angle Variation with Mass')
plt.plot(mass, optimum_mass, 'm', linewidth = 2)
plt.plot(mass, optimum_mass, 'bo', label = 'Particles of increasing mass')
plt.legend(loc='best')
plt.xscale('log')
plt.xlabel('Mass')
plt.ylabel('Optimum Launch Angle')
plt.show()

==================================================================================================

# Air resistance w/ quadratic dependance:

#variables
initial_vel = 2
angle = np.pi/5
D = 1E-4
m = 1E-9
B = 1.6E-4

g = 9.8
C = 0.25
dt = 0.0001
t = 0.0
y = 0
x = 0

b = B*D
c = C * D**2
Vy_0 = initial_vel * np.sin(angle) 
Vx_0 = initial_vel * np.cos(angle)
Vy = Vy_0 
Vx = Vx_0 

none_x = []
none_y = []
linear_x = []
linear_y = []
quadratic_x = []
quadratic_y = []

while y >= 0:
	none_x.append(x)
	none_y.append(y)
	t = t + dt
	Vy = Vy - g*dt
	x = x + dt*Vx
	y = y + dt*Vy

Vy = Vy_0 
Vx = Vx_0 
t = 0
x = 0
y = 0

while y >= 0:
	linear_x.append(x)
	linear_y.append(y)
	t = t + dt
	Vx = Vx - (b/m)*Vx*dt
	Vy = Vy - g*dt - (b/m)*Vy*dt
	x = x + dt*Vx
	y = y + dt*Vy

Vy = Vy_0 
Vx = Vx_0 
t = 0
x = 0
y = 0

while y >= 0:
	quadratic_x.append(x)
	quadratic_y.append(y)
	t = t + dt
	Vx = Vx -c/m * (np.sqrt(Vx**2 + Vy**2))*Vx*dt
	Vy = Vy - g*dt -c/m * (np.sqrt(Vx**2 + Vy**2))*Vy*dt
	x = x + dt*Vx
	y = y + dt*Vy

Vy = Vy_0 
Vx = Vx_0 
t = 0
x = 0
y = 0

plt.title("Trajectory Comparison")
plt.xlabel("x - direction")
plt.ylabel("y - direction")

plt.plot(none_x, none_y, 'r', linewidth = 2, label = 'No Air Resistance')
plt.plot(linear_x, linear_y, 'c--', linewidth = 2, label = 'Linearly-Dependent Air Resistance')
plt.plot(quadratic_x, quadratic_y, 'm--', linewidth = 2, label = 'Quadratically-Dependent Air Resistance')
plt.legend(loc = 2, fontsize = 'small')

plt.show()
