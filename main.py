#!/usr/bin/env python3

# n-body.py solve the n-body problem using Newton
# Copyright (C) <2019>  Angelica Nayeli Rivas Bedolla (angelica.nayeli@comunidad.unam.mx)
#                       Pablo Clemente Moreno (clemnte@comunidad.unam.mx)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# files
import classes
import graphics

#libraries
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
	
	## ALpha Centauri A
	p0 = [0., 0.]            #UA
	v0 = [0., 0.]            #m/s
	m  = 1.432                   #masas solares
	
	## ALpha Centauri B
	p1 = [11.2, 0.]          #UA
	v1 = [0., 9.8402e-7]     #km/seg
	m1 = 1.387                   #masas solares
	
	dt = 1.                      #sec
	
	lenTime=3600.*24*60         #sec
	n_steps = int(lenTime/dt)

	A = classes.Particle(p0, v0, m)
	B = classes.Particle(p1, v1, m1)
	
	particles = [A, B]
	twoBody= classes.Potencial(particles, dt)
	
	fig, ax = plt.subplots()
	
	#
	skip = 0
	save = False
	for t in range(1,n_steps):
		if skip == 1000:
			skip = 0
			save = True
		system = twoBody.integrate(float(t)*dt, save)
		save = False
		skip += 1
	
	for  i, particle in enumerate(particles):
		time, trajectory = particle.getTrajectory()
		graphics.plotting2D_multiple(fig, ax, trajectory, i)
	
	plt.show()
