def isPrime(n):
    if n%2==0 or n<=1 or n%1: return n==2
    k=3
    while k*k<=n and n%k!=0: k+=2
    return k*k>n
def divALL(n):
    A=[i for i in range(2,int(n**(1/2)+1))if isPrime(i)]
    B=[]
    for i in A:
        while n%i==0:
            n=n//i
            B.append(i)
    
    return B
#print(divALL(41348564178))
for i in range(810000000,1000000000000000):
    c=divALL(i)
    d=list(set(c))
    m=1
    for x in d:
        m *= (c.count(x)+1)
    if (m==1000):
        print(m,i)
        #dividers of prime numbers
def divALL(n):
    A=[i for i in range(2,int(n**(1/2)+1))if isPrime(i)]
    B=[]
    for i in A:
        while n%i==0:
            B.append(i)
            B.append(n//i)
            n=n//i
    return sorted(B)

#print(divALL(41348564178))
'''for i in range(810000000,1000000000000000):
    c=divALL(i)
    d=list(set(c))
    m=1
    for x in d:
        m *= (c.count(x)+1)
    if (m==1000):
        print(m,i)
'''
#2 simple dividers 
for i in range(125697,125721+1):
        f=divALL(i)
        if (len(f)==2):
            print(f)
#var 2
for a in range(125721+1//2+1):
    if isPrime(a): m.append(a)
for i in range(len(m)-1,i,-1):
    if 125697<=(m[i]*m[k])<=126721:
        print(m[i],m[k])
        
