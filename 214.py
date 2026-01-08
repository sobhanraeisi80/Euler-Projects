from math import sqrt
def factors(n):
    square_root=int(sqrt(n))
    set_of_factors=set()
    for i in range(1, square_root+1):
        if n%i==0:
            if is_prime(i):
                set_of_factors.add(i)
            if is_prime(n//i):
                set_of_factors.add(n//i)
    return set_of_factors
def phi(n):
    set_=factors(n)
    makhraj=1
    for i in set_:
        n*=(i-1)
        makhraj*=i
    return n//makhraj
def is_prime(n):
    set1=set()
    squre=sqrt(n)
    if n!=2 and n%2==0 :
        return False
    for i in range(1, int(squre)+1):
            if n%i==0:
                set1.add(i)
                set1.add(n//i)
            if len(set1)>2:
                return False
    return len(set1)==2
sum=0
for n in range(1,4*10**7):
    saved=n
    print(saved)
    if not(is_prime(n)):
        continue
    count=0
    while 1:
        count+=1
        n=phi(n)
        if n==1:
            break
    if count+1==25:
        sum+=saved
print(sum)
    

    
            
