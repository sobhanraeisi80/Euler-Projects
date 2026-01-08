from itertools import permutations as per
list_of_strings=list(per('1234567890',10))
sum=0
for string in list_of_strings:
    print(string)
    count=0
    if string[0]=='0':
        continue
    for j in range(1,8):
        sub_string=''
        sub_string=string[j]+string[j+1]+string[j+2]
        if j==1:
            if int(sub_string)%2==0:
                count+=1
        if j==2:
            if int(sub_string)%3==0:
                count+=1
        if j==3:
            if int(sub_string)%5==0:
                count+=1
        if j==4:
            if int(sub_string)%7==0:
                count+=1
        if j==5:
            if int(sub_string)%11==0:
                count+=1
        if j==6:
            if int(sub_string)%13==0:
                count+=1
        if j==7:
            if int(sub_string)%17==0:
                count+=1
    if count==7:
        string1=''
        for i in string:
            string1+=i
        sum+=int(string1)
print(sum)