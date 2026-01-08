from math import sqrt
def is_prime(n):
    squre=sqrt(n)
    for i in range(2, int(squre)+1):
            if n%i==0:
                return False
    return True
def factors(n):
    square_root=int(sqrt(n))
    for i in range(1, square_root+1):
        if n%i==0:
            if is_prime(i) and i > 100:
                return False
            if is_prime(n//i) and (n//i) > 100:
                return False
    return True

n=1
count=0
while n<=10**9:
    if factors(n) :
        count+=1
    print(n)
    n += 1
print(count)
