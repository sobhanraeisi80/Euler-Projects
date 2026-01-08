def is_prime(n):
    from math import sqrt
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
list_of_primes=[]
count=0
sum=0
for i in range(5,10**6+10):
    if is_prime(i):
        list_of_primes.append(i)
for j in range(0,len(list_of_primes)-1):
    p1=list_of_primes[j]
    p2=list_of_primes[j+1]
    n=1
    l=len(str(p1))
    while 1:
        
        string=''
        m=n*p2
        n_str=str(m)
        if len(n_str)>=l:
            for _ in range(-l,0):
                string+=n_str[_]
            if string ==str(p1) :
                count+=1
                print(f'p1={p1},p2={p2},n={m}')
                sum+=(m)
                break
        n+=1
print(f'sum={sum}')
        