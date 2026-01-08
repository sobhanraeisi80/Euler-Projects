from math import sqrt
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    squre=int(sqrt(n))
    set_of_factors=set()
    for i in range(1, squre+1):
        if n%i==0:
            set_of_factors.add(i)
            set_of_factors.add(n//i)
        if len(set_of_factors)>2:
            return False
    return True
def factors(n):
    set_of_factors=set()
    squre=int(sqrt(n))
    for i in range(1, squre+1):
        if n%i==0 :
            if is_prime(i) and is_prime(n//i):
                set_of_factors.add(i)
                set_of_factors.add(n//i)
    return set_of_factors
n=1
count_tot=0
while n<10**8:
    count=0
    set1=factors(n)
    if set1=={1,n}:
        n+=1
        continue
    for p in set1:
        m=n
        while m%p==0:
            m//=p
            count+=1
    if count==2:
        count_tot+=1
        print(n)
    n+=1
print(count_tot)
            