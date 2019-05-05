import random

INF=10**20
start=0
size=[100,40]
N=int(input())
dist=[list(map(int,input().split()))for _ in range(N)]

for i in range(N):
    for j in range(N):
        if dist[i][j]==0:
            dist[i][j]=INF

class Chromosome:
    def __init__(self,genes=[]):
        if genes:
            self.genes=genes
        else:
            self.genes=list(range(1,N))
            random.shuffle(self.genes)
    def crossover(a,b,point):
        return Chromosome(a.genes[:point]+b.genes[point:])

def cost(x: Chromosome):
    global start
    if len(set(x.genes))!=len(x.genes):
        return INF
    last=start
    cost=0
    for i in x.genes:
        cost+=dist[last][i]
        last=i
    return cost+dist[last][start]
def f(x: Chromosome):
    return 10000000/cost(x)

def Seletion():
    global Ch
    Ch=random.choices(Ch,weights=[f(x) for x in Ch],k=size[1])
def Crossover():
    global Offspring
    for _ in range(size[0]):
        a,b=random.choices(range(size[1]),k=2)
        # Invalid for TSP Problem
        Offspring.append(Chromosome.crossover(Ch[a],Ch[b],random.randint(0,len(Ch[a].genes))))

def Mutate():
    global Offspring
    for i in range(size[0]):
        if random.random()*100<=0.1:
            t=Offspring[i].genes
            a,b=random.choices(range(len(t)),k=2)
            t[b],t[a]=t[a],t[b]

Ch=[Chromosome() for _ in range(size[0])]
print([cost(x) for x in Ch])
for _ in range(10000):
    Offspring=[]
    Seletion()
    Crossover()
    Mutate()
    Ch=Offspring
print([cost(x) for x in Ch])
# print([x.genes for x in Ch])