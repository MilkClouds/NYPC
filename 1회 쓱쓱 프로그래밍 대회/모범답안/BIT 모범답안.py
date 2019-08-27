import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
A=[*map(int,input().split())]
tree=[0]*(N+1)
def query(u):
    t=0
    while u:
        t^=tree[u]
        u&=u-1
    return t
def update(u,v):
    while u<=N:
        tree[u]^=v
        u+=u&-u
for i in range(1,1+N):
    update(i,A[i-1])
for _ in range(Q):
    t,a,b=map(int,input().split())
    if t&1:
        update(a,b)
    else:
        print(query(b)^query(a-1))