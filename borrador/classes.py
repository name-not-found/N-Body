import math

class Particle:
	G = 6.674e-11     
	def __init__(self, p, v, m):
		self.p = p
		self.v = v
		self.m = m

	def integrate(self, dt, p1, m1):
		r = self.computeR(p1)
		u = self.computeU(p1)
		
		Vx = (self.G*m1*dt/(r**3))*u[0]
		Vy = (self.G*m1*dt/(r**3))*u[1]
		Vz = (self.G*m1*dt/(r**3))*u[2]
		
		self.p = [self.p[0]+(self.v[0]+Vx)*dt, self.p[1]+(self.v[1]+Vy)*dt, self.p[2]+(self.v[2]+Vz)*dt]

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
	
