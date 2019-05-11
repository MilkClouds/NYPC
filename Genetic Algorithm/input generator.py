import random
N=15

print(N)
for i in range(N):
    for j in range(N):
        if i==j:
            print(0,end=' ')
        else:
            print(random.randint(1,1000000),end=' ')
    print()