def sqrt(n):
    from math import sqrt
    squre_root_n=sqrt(n)
    if int(squre_root_n)**2==n:
        return int(squre_root_n)
    else:
        return squre_root_n
f=open('0042_words.txt','r')
line=f.readline()
list_of_word=line.split(',')
count=0
for i in list_of_word:
    sum=0
    m=i.lower()
    for j in m:
        if j=='"':
            continue
        sum+=ord(j)-96
    check=8*sum+1
    if isinstance(sqrt((check)),int) and ((sqrt(check)-1)%2==0):
        count+=1    
print(count)
    
    