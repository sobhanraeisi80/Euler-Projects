def phi(n):
    from math import gcd
    number=1
    count=0
    while number<n:
        if gcd(number, n)==1:
            count+=1
        number+=1
    return count
def is_prime(n):
    from math import sqrt
    if n<2:
        return False
    elif n==2:
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
num=2
max_num=0
max_result=0
while num<=1e6:
    if is_prime(num):
        num+=1
        continue
    result=(num/phi(num))
    if result>=max_result:
        max_result=result
        max_num=num
        print(num)
    num+=1
print(max_num)



        
