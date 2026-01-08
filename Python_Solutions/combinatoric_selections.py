import math
count=0
for i in range(1, 101):
    
    for j in range(1, i+1):
        result=math.factorial(i)//(math.factorial(j)*math.factorial(i-j))
        print(result)
        if result>1e6:
            count+=1
        
print(f'count={count}')

