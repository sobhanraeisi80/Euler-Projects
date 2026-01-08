max_num=0
for i in range(100, 1000):
    for j in range(100, 1000):
        number=i*j
        str_num=str(number)
        str_num=str_num[::-1]
        if int(str_num)==number:
            if number>=max_num:
                max_num=number
print(max_num)