import sys
input=sys.stdin.readline

x=int(input())
N=int(input())
p={i:1 for i in map(int,input().split())}

from collections import deque
if p.get(x):
    print(-1)
    exit()
if x==100000:
    print(0)
    exit()
Q=deque([(x,0)])
visit=[False]*100001

def f(u,t):
    if u>100000 or visit[u] or p.get(u): return
    if u==100000:
        print(t)
        exit()
    visit[u]=True
    Q.append((u,t))

while Q:
    pos,time=Q.popleft()
    f(pos+1,time+1)
    f(pos+3,time+1)
print(-1)