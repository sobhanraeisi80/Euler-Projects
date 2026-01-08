max_sum=0
for a in range(1,101):
    for b in range(1,101):
        sum=0
        number=(a)**b
        number=str(number)
        for n in number:
            sum+=int(n)
        if sum>max_sum:
            max_sum=sum
print(max_sum)