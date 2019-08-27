import sys
input=sys.stdin.readline

x,y=map(int,input().split())
N=int(input())

d={}
for _ in range(N):
    a,b=map(int,input().split())
    if a==x:
        tan=(10**12,b>y)
    else:
        tan=((b-y)/(a-x),b>y)
    if d.get(tan):
        d[tan].append((a,b))
    else:
        d[tan]=[(a,b)]

def dist(u):
    return (x-u[0])**2+(y-u[1])**2

M=0
Mv=None
for k,v in d.items():
    if len(v)>M:
        M=len(v)
        Mv=max(v,key=dist)

print(*Mv)
