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
while n:
	if n&1:
		c*=x
		c%=m
	n>>=1
	x=x*x
	x%=m
print(c)