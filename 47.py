import time
start=time.time()
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
    for i in range(1,squre+1):
        if n%i==0:
            set_of_factors.add(i)
            set_of_factors.add(n//i)
            if len(set_of_factors)>2:
                return False
    return len(set_of_factors)==2
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
n=2
while 1:
    set1=factors(n)
    set2=factors(n+1)
    set3=factors(n+2)
    set4=factors(n+3)
    l1=len(set1)
    l2=len(set2)
    l3=len(set3)
    l4=len(set4)
    if  (l1==l2==l3==l4==4):
        print(n)
        break
    n+=1
end=time.time()
print(end-start)
