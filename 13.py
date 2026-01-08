f=open('0013.txt','r')
sum_=0
for _ in range(100):
    line=f.readline()
    print(line)
    sum+=int(line)
sum_=str(sum_)
print(sum_[:10])
