a,b=map(int,input().split())
n,m=map(int,input().split())

class newcomplex:
	def __init__(self,r,i):
		self.r=r
		self.i=i
	def __mul__(self,o):
		r=self.r;i=self.i
		return newcomplex(r*o.r-i*o.i,r*o.i+i*o.r)
	def __mod__(self,m):
		return newcomplex(self.r%m,self.i%m)
	def __repr__(self):
		return "%d %d"%(self.r,self.i)


c=newcomplex(1,0)
x=newcomplex(a,b)
for _ in range(n):
	c*=x
	c%=m
print(c)