def is_prime(n):
    count=0
    for i in range(1, n+1):
        if n%i==0:
            count+=1
    return count<=2

def max_factors(n):
    a=0
    for i in range(1, n+1):
        if n%i==0 and is_prime(i):
            a=i
    return a
print(max_factors(6008))

