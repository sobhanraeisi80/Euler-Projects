from math import gcd,sqrt
def factors(n):
    set_of_factors=set()
    squre=sqrt(n)
    for i in range(1, int(squre)+1):
            if n%i==0 :
                set_of_factors.add(i)
                set_of_factors.add(n//i)
    return set_of_factors
def is_prime(n):
    if n<2:
         return False
    if n==2:
         
        return True
    if n%2==0:
         return False
    set1=set()
    squre=sqrt(n)
    for i in range(1, int(squre)+1):
            if n%i==0:
                 set1.add(i)
                 set1.add(n//i)
                 if len(set1)>2:
                      return False
    return True
                
def rad(n):
    set_n=factors(n)
    product=1
    for i in set_n:
        if is_prime(i):
            product*=i
    return product
list_of_rads=[]
list_of_num=[]
for n in range(100001):
    list_of_rads.append(rad(n))
min_of_rad=min(list_of_rads)
max_of_rads=max(list_of_rads)
print(max_of_rads)
while min_of_rad<=max_of_rads:
    print(min_of_rad)
    for i in range(100001):
        if list_of_rads[i]==min_of_rad:
            list_of_num.append(i)
    min_of_rad+=1
print(list_of_num[10000])
     


