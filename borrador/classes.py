import math
#composición de una particula
class Particle:
	G = 6.674e-11     
	def __init__(self, p, v, m, dt=1):
		self.p = p
		self.v = v
		self.m = m
		self.dt = dt

	#def integrate(self, dt, p1, m1):
	def integrate(self, B):
		r = self.computeR(B.p)
		u = self.computeU(B.p)
		
		Vx = (self.G*B.m*self.dt/(r**3))*u[0]
		Vy = (self.G*B.m*self.dt/(r**3))*u[1]
		Vz = (self.G*B.m*self.dt/(r**3))*u[2]

		self.v[0] += Vx
		self.v[1] += Vy
		self.v[2] += Vz
		
		self.p = [self.p[0]+(self.v[0])*self.dt, self.p[1]+(self.v[1])*self.dt, self.p[2]+(self.v[2])*self.dt]

	def getPosition(self):
		return self.p

	def getKineticEnergy(self):
		k = (1/2)*self.m*( math.sqrt( self.v[0]**2 + self.v[1]**2 + self.v[2]**2) )
		return k
	
	def computeR(self,p1):
		r= math.sqrt( (p1[0]-self.p[0])**2 + (p1[1]-self.p[1])**2 + (p1[2]-self.p[2])**2 ) 
		return r
	
	def computeU(self, p1):
		u=[0,0,0]
		i=0
		for a,b in zip(self.p, p1):
			u[i] = b - a
			i+=1
		return u

	def setdt(self, dt):
		self.dt = dt

	
