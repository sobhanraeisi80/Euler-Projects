from math import sqrt

def set_of_factors(n):
    set_of_factor=set()
    squre=int(sqrt(n))
    for i in range(1, squre+1):
            if n%i==0:
                set_of_factor.add(i)
                set_of_factor.add(n//i)
    return len(set_of_factor)
count=0
for i in range(2, 10**7):
    print(i)
    if set_of_factors(i)==set_of_factors(i+1):
        count+=1
print(count)