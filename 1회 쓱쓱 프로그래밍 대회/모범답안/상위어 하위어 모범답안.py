N,Q=map(int,input().split())
d={}
for _ in range(N):
	a,b=input().split()
	d[b]=a

for _ in range(Q):
	print(d[input()])