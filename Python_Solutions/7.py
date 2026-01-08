def num_of_factors(n):
    import math
    count=0
    squre=(math.sqrt(n))
    
    if isinstance(squre,int):
        for i in range(1, squre+1):
            if n%i==0:
                count+=2
        return count-1
    else:
        for j in range(1, int(squre)+1):
            if n%j==0:
                count+=2
        return count
def is_prime(n):
    count=num_of_factors(n)
    return count<=2
def nth_prime(n):
    
    count_1=0
    num=2
    while count_1<n:
        if is_prime(num):
            count_1+=1
            nth_prime_num=num
        num+=1    
    return nth_prime_num
print(nth_prime(100001))  
