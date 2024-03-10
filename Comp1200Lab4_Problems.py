#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: westonlarhette
"""
""" Practice Problems from Lab 4"""
"""Program to calculate the gravitational force between three separate pairs of
celestial bodies (ex. Sun-Earth, Earth-Moon, Sun-Moon)"""
import numpy as np

# Define Newtonian gravitational constant:
G = 6.647e-11 # units in N m^2/kg^2
    
# Create array for planet name planet mass (kg) and distance (m))
names = np.array(["Earth and Sun","Moon and Earth","Moon and Sun"])

m_earth = 5.972e+24;
m_moon = 7.348e+22;
m_sun = 1.989e+30;

masses = np.array([[m_earth,m_sun],  # Earth and Sun
                   [m_moon,m_earth], # Moon and Earth
                   [m_moon,m_sun]])  # Moon and Sun

d_sun_earth = 148.61e+9;
d_moon_earth = 384.4e+6;
d_moon_sun = 150e+9;
distances = np.array([d_sun_earth, d_moon_earth,d_moon_sun])

# Calculate the gravitational forces

for i in range(len(masses)):
    name = names[i]
    m1,m2 = masses[i]
    d = distances[i]
    F = G * (m1 * m2) / d**2
    
    print(f"Gravitational force between the {name} {i+1}: {F:.2e} N")



"""Program to calculate the horizontal and vertical position of a projectile
at different time intervals, given its initial velocity and launch angle"""
import numpy as np

# Define constants
v0 = 30 # Initial velocity (m/s)
theta = 45 # Launch angle (degrees)
g = 9.81 # Acceleration due to gravity (m/s^2)

# Convert angle to radians
theta_rad = np.radians(theta)

# Time Intervals (s)
time_intervals = np.array([0,1,2,3,4,5])

for t in time_intervals:
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    print(f"At t={t}s: Horizontal position = {x:.2f} m, Vertical position = {y:.2f} m")



"""Program to calculate the total resistance of a circuit with resistors in
series and in parallel"""
import numpy as np
# Create arrays for resistances (in ohms):
resistors_series = np.array([10,20,30]);
resistors_parallel = np.array([10,10,10])
total_series = 0
for i in range(len(resistors_series)):
    total_series = total_series + resistors_series[i]
print(f"Total resistance in series: {total_series} ohms")

R_inverse = 0;    
for i in range(len(resistors_parallel)):
    R_inverse = R_inverse + 1 / resistors_parallel[i]
   
total_parallel = 1 / R_inverse;
print(f"Total resistance in parallel: {total_parallel:.2f} ohms")




