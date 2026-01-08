def is_prime(n):
    from math import sqrt
    if n<2:
        return False
    if n==2:
        return True
    elif n%2==0:
        return False
    count=0
    squre=sqrt(n)
    if isinstance(squre,int):
        for i in range(1, squre+1):
            if n%i==0:
                count+=2
        count-1
        return count==2
    else:
        for j in range(1, int(squre)+1):
            if n%j==0:
                count+=2
        return count==2



max_n_of_primes=0
for a in range(-9999, 10000):
    for b in range(-10000,10001):
        n=0
        count=0
            #print(a,b)
        while 1:
                #print(f'n={n}')
            number=(n)**2+a*(n)+b
            if is_prime(number):
                count+=1
                n+=1
            else:
                break
        if count>max_n_of_primes:
            max_n_of_primes=count
            t=(a,b)    
print(t,max_n_of_primes)


