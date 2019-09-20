#!/usr/bin/env python3
"""
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
"""
# files
import classes
import graphics

#libraries
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
	p0 = [5e-2, 1e-3, 0.] #km
	v0 = [0., 0., 0.]     #km/s
	m = 1e7               #kg
	
	p1 = [0., 0., 0.]     #km
	v1 = [1., 1., 0.]     #km/s
	m1 = 1.               #kg
	
	dt = 1e-2             #sec

	A = classes.Particle(p0, v0, m)
	B = classes.Particle(p1, v1, m1)
	
	# dos particulas
	particles = [A, B]
	twoBody= classes.Potencial(particles, dt)
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	for t in range(1,100):
		system = twoBody.integrate(float(t)*dt)
	
	for  i, particle in enumerate(particles):
		time, trajectory = particle.getTrajectory()
		graphics.plotting3D(fig, ax, trajectory, i)
	
		
	#2D
	"""
	x = []
	y = []
	v = []
	a = []
	
	x.append(0.)
	y.append(B.getPosition())
	v.append(B.getVelocity()[0])
	a.append(0.)
	v1 = B.getVelocity()[0]
	
	for t in range(1,100):
		LastX = B.getPosition()[0]
		lastV = v1
		B.integrate(A)

		if t%3 == 2:
			print(B.getPosition())
		
		x.append(float(t)*dt)
		y.append(B.getPosition()[0])
		v1 = (B.getPosition()[0] - LastX)/B.dt
		v.append(v1)
		a.append((v1 - lastV)/B.dt)
	
	fig, ax = plt.subplots(3)
	graphics.plotting2D(fig, ax[0], x, y, "", "", "", "", "distance [$km$]")
	graphics.plotting2D(fig, ax[1], x, v, "", "", "", "", "velocity [$km/s$]")
	graphics.plotting2D(fig, ax[2], x, a, "", "", "", "time [$sec$]", "acceleration [$km/s^2$]")
	"""
	
	#3D
	"""
	B.setdt(dt)
	
	x = []
	y = []
	
	x.append(0.)
	y.append(B.getPosition())
	
	for t in range(1,100):
		B.integrate(A)
		x.append(float(t)*dt)
		y.append(B.getPosition())
		
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	graphics.plotting3D(fig, ax, y)
		
	posA = A.getPosition()
	ax.scatter(posA[0], posA[1], posA[2], marker="o")
	#graphics.plotting3D(fig, ax, posA)
	"""
	
	plt.show()
