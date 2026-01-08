import gmpy2 
import time
start=time.time()
def n_term_chain(n):
    set1=set()
    set1.add(n)
    while 1:
        sum=0
        for i in str(n):
            sum+=gmpy2.fac(int(i))
        if sum not in set1:
            n=sum
            set1.add(sum)
        else:
            return len(set1)
n=1
count=0
while n<=10**6:
    print(n)
    terms=n_term_chain(n)
    if terms==60:
        count+=1
    n+=1
print(count)
end=time.time()
print(end-start)