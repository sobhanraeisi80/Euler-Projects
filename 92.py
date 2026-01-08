def chain(n):
    sum=0
    while 1:
        n_str=str(n)
        for i in n_str:
            sum+=int(i)**2
        if sum==89:
            return True
        if sum==1:
            return False
        n=sum
        sum=0
n=1
count=0
while n<10**7:
    print(n)
    if chain(n):
        count+=1
    n+=1
print(count)