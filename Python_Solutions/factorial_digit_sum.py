import math
fac=math.factorial(100)

fac=str(fac)
sum=0
for i in fac:
    sum+=int(i)
print(sum)