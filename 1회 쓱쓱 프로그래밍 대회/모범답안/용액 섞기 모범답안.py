from random import *
import sys
input=sys.stdin.readline
N,Q=map(int,input().split())

par=[i for i in range(N+1)]
rank=[1 for _ in range(N+1)]

def find(u):
    if u==par[u]:
        return u
    par[u]=find(par[u])
    return par[u]
def merge(u,v):
    u=find(u);v=find(v)
    if u==v:return
    if rank[u]>rank[v]:u,v=v,u
    par[u]=v
    if rank[u]==rank[v]: rank[v]+=1

for _ in range(Q):
    t=input().split()
    a,b=map(int,t[1:])
    if t[0]=='!':
        merge(a,b)
    else:
        print(0+(find(a)==find(b)))