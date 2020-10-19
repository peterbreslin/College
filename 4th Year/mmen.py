# -*- coding: utf-8 -*-
"""
PY4A03 Planetary and Space Science 

Problem Set 1

@author: Peter Breslin - 17340915
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import integrate

#=============================================================================

" 1. Inputting variables "

# Masses of planets in the Solar System 
M_mer = 3.3e26
M_ven = 48.7e26
M_ear = 59.8e26
M_mar = 6.4e26
M_ast = 0.1e26
M_jup = 19040e26
M_sat = 5695e26
M_ura = 870e26
M_nep = 1032e26

# Solar Composition Factors
F_mer = 350
F_ven = 270
F_ear = 235
F_mar = 235
F_ast = 200
F_jup = 5
F_sat = 8
F_ura = 15
F_nep = 20

# Distances in AU
D_mer = 0.387
D_ven = 0.723
D_ear = 1
D_mar = 1.524
D_ast = 2.7
D_jup = 5.203
D_sat = 9.523
D_ura = 19.208
D_nep = 30.087

# Storing the masses/factors/distances in arrays for later use
masses  = np.array([M_mer, M_ven, M_ear, M_mar, M_ast, M_jup, M_sat, M_ura, M_nep])
factors = np.array([F_mer, F_ven, F_ear, F_mar, F_ast, F_jup, F_sat, F_ura, F_nep])
dist_au = np.array([D_mer, D_ven, D_ear, D_mar, D_ast, D_jup, D_sat, D_ura, D_nep])


#=============================================================================

" i) Mass of solar composition material required to form each planet "

# Mass required = (Mass x Factor) for each planet
mass_req = masses * factors

# Making list of Planet names for the labels
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Asteroids', 'Jupiter',
          'Saturn', 'Uranus', 'Neptune']

# Specifying a colour label for each planet
colours=['b','y','g','m','c','r','slategrey','limegreen','tab:orange']

# Plotting --> for loop to give each planet a different colour
for i in range(len(masses)):
    plt.scatter(masses[i], mass_req[i], c=colours[i], label=planets[i], marker='.')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Planet Mass (g)')
plt.ylabel('Mass Required (g)')
plt.title('Mass of Solar Composition Required to form each Planet')
plt.legend(loc='best', fontsize='small')
plt.grid(linestyle='--', alpha=50)
#plt.savefig('mass_req_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# Bar plot might be a nice way to view it too
# Getting the number of indicies for the x-axis (9 planets)
labels = np.arange(len(planets))

# Plotting the bar plot
plt.bar(labels, mass_req, log=1, color='green')
plt.xticks(labels, planets, fontsize=5, rotation=0)
plt.title('Mass of Solar Composition Required to form each Planet')
plt.xlabel('Planet')
plt.ylabel('Mass (g)')
#plt.savefig('mass_req.png', dpi=300, bbox_inches='tight')
plt.show()


#=============================================================================

" ii) Surface Density of solar nebula material for each planet "

# Distribute the mass required over a series of annuli, centred on each planet 
# Annuli boundaries will be halfway between orbits of each planet

# Adding Pluto to help find the surface density for Neptune
pluto_au = 39
all_distances = np.append(dist_au, pluto_au)

# Converting distances into cm (from AU)
dist_cm = all_distances * 1.496e13

# Creating a function to carry out the procedure   
def surface_density(inner_planet, middle_planet, outer_planet, mass):
    
    # Boundaries of the annuli
    a = (middle_planet - inner_planet)/2
    b = (outer_planet - middle_planet)/2
    
    # Calculating the area of the annulus
    area = np.pi * ((middle_planet + b)**2 - (middle_planet - a)**2)
    
    # Now finding the surface density, sigma
    sigma = mass/area
    
    return sigma
    
# Creating a list to store the surface densities
sd = []

# Looping through the distances and applying the surface_density function
for i in range (len(dist_cm)-2):
    x = surface_density(dist_cm[i], dist_cm[i+1], dist_cm[i+2], mass_req[i+1])
    sd.append(x)


# The surface_density function does NOT evaluate the first entry (Mercury) of 
# the list ---> will compute this individually and add to the sd list:
c       = (dist_cm[1] - dist_cm[0])/2  
area    = np.pi * ((dist_cm[0] + c)**2 - (dist_cm[0] - c)**2)
sigma_m = mass_req[0]/area

# Adding Mercury to the beginning of the list
sd.insert(0, sigma_m)

# Plotting
plt.plot(dist_au, sd, alpha=50, linewidth=1, linestyle='--')
for i in range(len(dist_au)):
    plt.scatter(dist_au[i], sd[i], s=75, c=colours[i], label=planets[i], 
                marker='.')
plt.xscale('log')
plt.yscale('log')
plt.title('Solar Nebula Material Surface Densities ($\sigma$)')
plt.ylabel('$\sigma$ (g cm$^{-2})$')
plt.xlabel('Distance [AU]')
plt.grid(linestyle='--', alpha=50)
#plt.savefig('mass_req_plot.png', dpi=300, bbox_inches='tight')


"""
Unfortunately, I could not figure out how to plot the error bars for the planetary 
distances correctly. Therefore, I left the xerrors out of my final script. In my 
attempt below, I used the inner and outer boundaries for each annulus as the 
errorbar lower and upper limits. 

xerror=[]
for i in range(len(all_distances)-1):
    boundary = (all_distances[i+1] - all_distances[i])/2
    xerror.append(boundary) 

lower_error  = dist_au - xerror
upper_error  = dist_au + xerror
total_xerror = [lower_error, upper_error]

plt.errorbar(dist_au, sd, xerr=total_xerror, fmt=' ', linewidth=1)
"""

#=============================================================================

" iii) Surface Density Fit "

# Defining the form of the function to be used to fit the surface density
def fit_func(r, sigma_0, alpha):
    return sigma_0 * (r**(-alpha))

# Taking out the extreme outliers from the surface densities and distances
# Making them into arrays for the fit to work
sd_arr = np.array(sd)
sd_arr = np.delete(sd_arr, 0)
sd_arr = np.delete(sd_arr, 2)
sd_arr = np.delete(sd_arr, 2)

dist_arr = np.array(dist_au)
dist_arr = np.delete(dist_arr, 0)
dist_arr = np.delete(dist_arr, 2)
dist_arr = np.delete(dist_arr, 2)

# Applying a least-squares fit to the curve using scipy.optimize
fit_params, pcov = curve_fit(fit_func, dist_arr, sd_arr)
y_fit = fit_func(dist_arr, *fit_params)

# Plotting the fit
plt.plot(dist_arr, y_fit, label="LSQ Fit", color='k', linewidth=1)
plt.legend(loc='lower left', fontsize='x-small')
#plt.savefig('fit.png', dpi=300, bbox_inches='tight')
plt.show()

stdevs = np.sqrt(np.diag(pcov))
print('')
print('Fit Parameters:')
print('sigma_0 = ' + str(round(fit_params[0])) + ' +/- ' + str(round(stdevs[0])))
print('alpha   = ' + str(round(fit_params[1], 2)) + ' +/- ' + str(round(stdevs[1], 2)))


#=============================================================================

" iv) Evaluating the integral for the Mass of solar nebula material required "

# Integrand: sigma(r)*r ---> sigma_0*(r**{-alpha})*r ---> sigma_0*r**{1-alpha}
def integrand(self, r):
    
    # Using my values
    return (1.496e13 ** fit_params[1]) * fit_params[0] * r**(1 - fit_params[1])

    # Using values in lecture notes as a test
    #return(1.496e13 ** 2) * 3300 * r**(1 - 2)

# Setting the integral bounds at an appropiate distance range:
R_s = 6.96e10               # Sun Radius = R_s = 6.96E10 cm 
R_f = pluto_au * 1.496e13   # Max distance to Pluto = R_f = 39AU 

# Using scipy to evaluate the double integral with the appropiate bounds
m = integrate.dblquad(integrand, R_s, R_f, 0, 2*np.pi)

print('')
print('Mass (g) = ' + str(m[0]) + ' = ' + str(round((m[0] / 2e33), 4)) + ' Msun')
