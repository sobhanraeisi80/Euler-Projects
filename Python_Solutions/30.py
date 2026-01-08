n=10
sum_total=0
while n<=10**6:
    sum1=0
    n_str=str(n)
    for i in n_str:
        sum1+=(int(i)**5)
    if sum1==n:
        sum_total+=n
    n+=1
print(sum_total)