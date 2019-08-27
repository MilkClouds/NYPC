import numpy as np
p=np.array([*map(int,input().split())])
v=np.array([*map(int,input().split())])
target=np.array([*map(int,input().split())])

if (p==target).all():
	print(0)
	exit()

for i in range(3):
	if v[i]==0:
		if p[i]==target[i]:
			v[i]=1
		else:
			print(-1)
			exit()

s=[*(set((target-p)/v)-{0})]

print(int(s[0]) if len(s)==1 and int(s[0])==s[0] else -1)