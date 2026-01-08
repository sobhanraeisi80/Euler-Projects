from math import inf,sqrt
def factors(n):
    square_root=int(sqrt(n))
    set_of_factors=set()
    for i in range(1, square_root+1):
        if n%i==0:
            if is_prime(i):
                set_of_factors.add(i)
            if is_prime(n//i):
                set_of_factors.add(n//i)
    return set_of_factors

def phi(n):
    set_=factors(n)
    makhraj=1
    for i in set_:
        n*=(i-1)
        makhraj*=i
    return n//makhraj

def is_prime(n):
    set1=set()
    squre=sqrt(n)
    if n!=2 and n%2==0 :
        return False
    for i in range(1, int(squre)+1):
            if n%i==0:
                set1.add(i)
                set1.add(n//i)
            if len(set1)>2:
                return False
    return len(set1)==2

list_of_m=[]
list_of_n=[]
minimum=inf
res=0
for n in range(2,10**7):
    #print(n)
    phi_n=phi(n)
    m=n/phi_n
    if m<=minimum:
        n_str=str(n)
        phi_n_str=str(phi_n)
        list1=list(n_str)
        list2=list(phi_n_str)
        list1.sort()
        list2.sort()
        if list1==list2:
            print(n)
            list_of_m.append(m)
            list_of_n.append(n)
min_=min(list_of_m)
ind=list_of_m.index(min_)
print(list_of_n[ind])
