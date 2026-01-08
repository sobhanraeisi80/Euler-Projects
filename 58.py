from math import sqrt
def is_prime(n):
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
list1=[1]
side=3
count=0
while 1:
    
    for _ in range(4):
        a=list1[-1]+side-1
        list1.append(a)
        if is_prime(a):
            count+=1
    percent=(count/len(list1))*100
    print(side,percent)
    if (percent)<10:
        print(f'side={side}')
        break
    side+=2
