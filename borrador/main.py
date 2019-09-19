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

#libraries
import math

if __name__ == "__main__":
	p0 = [1., 0., 0.] #km
	v0 = [0., 0., 0.] #km/s
	m = 1.            #kg
	
	p1 = [0., 0., 0.] #km
	v1 = [1., 0., 0.]  #km/s
	m1 = 1e2           #kg
	
	dt = 1e-2            #sec

	A = classes.Particle(p0, v0, m)
	B = classes.Particle(p1, v1, m1)
	
	A.setdt(dt)

	for t in range(100):
		#print(A.getPosition())

		#A.integrate(dt,p1,m1)
		
		A.integrate(B)

		if t%3 == 2:
			print(A.getPosition())
