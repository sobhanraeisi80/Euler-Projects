from decimal import Decimal,getcontext
def squre(n):
    getcontext().prec=102
    squre_root=Decimal(n).sqrt()
    if int(squre_root)**2==n:
        return 0
    else:
        return squre_root

print(squre(2))
def sum_of_digit(n):
    sum1=0
    sq_n=squre(n)
    if sq_n==0:
        sum1+=0
    sq_n=format(sq_n,'.101f').replace('.','')
    sq_n=sq_n[:100]
    print(sq_n)
    for i in sq_n:
        sum1+=int(i)
    
    return sum1   
print(sum_of_digit(2))
sum=0
for n in range(1,101):
    sum+=sum_of_digit(n)
print(sum)

