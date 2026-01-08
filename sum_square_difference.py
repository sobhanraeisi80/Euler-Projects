def sum_square_1(n):
    sum=0
    for i in range(1, n+1):
        sum+=i**2
    return sum
def sum_square_2(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum**2
print(sum_square_2(100)-sum_square_1(100))
        