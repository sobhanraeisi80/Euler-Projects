from math import sqrt

def factors(n):
    set_of_factors=set()
    squre=sqrt(n)
    for i in range(1, int(squre)+1):
            if n%i==0 :
                set_of_factors.add(i)
                set_of_factors.add(n//i)
    set_of_factors.remove(n)
    return sum(set_of_factors)
print(factors(12496))




