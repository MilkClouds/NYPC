import sys
input=sys.stdin.readline

N=int(input())
a=0
b=0
c=0
for _ in range(N):
	x,y=map(int,input().split())
	c+=y*y
	b-=x*y*2
	a+=x*x
def f(x):
	t=int(x*1000)/1000
	return int(t) if t==int(t) else t
print(f(-b/2/a))