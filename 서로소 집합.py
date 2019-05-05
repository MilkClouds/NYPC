par=[]
for i in range(100):
    par.append(i)

def find(u):
    if u==par[u]:
        return u
    par[u]=find(par[u]) # Path Compression, 경로 압축
    return par[u]

def merge(u,v):
    u,v=find(u),find(v)
    if u==v:
        return
    par[u]=v # without Union-By-Rank

merge(1,5)
merge(2,5)
merge(4,1)

print(find(5)==find(4))
print(find(0)==find(1))