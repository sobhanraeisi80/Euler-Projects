def is_reversible(n):
    str_n=str(n)
    str_n=str_n[::-1]
    if str_n[0]=='0':
        return False
    res=n+int(str_n)
    for i in str(res):
        if int(i)%2==0:
            return False
    return True
count=0
for n in range(1,10**9):
    print(n)
    if is_reversible(n):
        count+=1
print(count)