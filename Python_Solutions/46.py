from math import sqrt
def is_squre(n):
    squre_root=sqrt(n)
    if int(squre_root)**2==n:
        return True
    return False
def is_prime(n):
    if n==1:
        return False
    if n<4:
        return True
    if n%2==0:
        return False
    count=0
    squre_root=sqrt(n)
    set1=set()
    for i in range(1,int(squre_root)+1):
        if n%i==0:
            set1.add(i)
            set1.add(n//i)
        if len(set1)>2:
            return False
    return len(set1)==2

def primes(n):
    number=1
    list1=[]
    while number<=n:
        if is_prime(number):
            list1.append(number)
        number+=1
    return list1

def goldbakh():
    n=9
    list_of_primes=[]
    while 1:
        print(n)
        count=0
        check=0
        if n%2==0:
            n+=1
            continue
        if not(is_prime):
            list_of_primes=primes(n)
            for i in list_of_primes:
                check=(n-i)/2
                if is_squre(check):
                    print(f'{n}={i}+2*#')
                    n+=1
                else:
                    count+=1
        if count!=0:
            return n
        n+=1
print(goldbakh())



