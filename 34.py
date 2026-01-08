def is_digit_fac(n):
    from math import factorial
    n=str(n)
    sum=0
    for i in n:
        i=int(i)
        sum+=factorial(i)
    if int(n)==sum:
        return True
    return False
n=3
sum=0
while n<=10**7:
    if is_digit_fac(n):
        sum+=n
        n+=1
    n+=1
print(sum)