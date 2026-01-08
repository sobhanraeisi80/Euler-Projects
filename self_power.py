sum=0
for i in range(1, 1001):
    sum+=i**i
sum=str(sum)
l=len(sum)
print(sum[l-10:])