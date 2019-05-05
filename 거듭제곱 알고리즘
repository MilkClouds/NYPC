A=2
B=10**50
C=12345

def pow_row(a,x):
    ret=1
    for _ in range(x):
        ret = ret * a % C
    return ret

def pow_recursive(a,x):
    if x==0:
        return 1
    if x%2==0:
        return pow_recursive(a,x//2)**2 % C
    return a*pow_recursive(a,x//2)**2 % C

def pow(a,x):
    r=1
    while x:
        if x%2:
            r = r*a %C
        x//=2
        a = a*a %C
    return r

print(pow_recursive(A,B))
print(pow(A,B))
