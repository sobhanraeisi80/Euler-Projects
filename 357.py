from math import sqrt
def is_prime(n):
    if n < 2 :
        return False
    if n == 2 :
        return True
    if n % 2== 0:
        return False
    
    squre = int(sqrt(n))
    set_of_factors = set()

    for i in range(1, squre + 1):
        if n % i == 0 :
            set_of_factors.add(i)
            set_of_factors.add(n // i)
        if len(set_of_factors) > 2 :
            return False
        
    return True

def is_factors_primes (number) :
    square_root = int(sqrt(number)) + 1
    count = 0
    set_of_divisors = set()
    for d in range(1, square_root) :
        if number % d == 0 :
            set_of_divisors.add(d)
            set_of_divisors.add(number // d)
    
    for m in set_of_divisors :
        res = m + number // m
        #print(res)
        if (is_prime(res)) :
            count += 1            
    
    return count == len(set_of_divisors)

sum_of_proper_number = 0
for i in range(1, 10 ** 8) :
    if is_factors_primes (i) :
        print(i)
        sum_of_proper_number += i

print(sum_of_proper_number)



