
def check(n):
    n=str(n)
    digit_last=n[-9:]
    digit_first=n[:9]
    set_of_digit=set(digit_last)
    set_of_digit_1=set(digit_first)
    if set_of_digit_1==set_of_digit=={'1','2','3','4','5','6','7','8','9'}:
        return True
    else:
        return False

list_of_elements=[0,1]
count=1
while 1:
    print(count)
    count+=1
    element1=list_of_elements[-1]
    element2=list_of_elements[-2]
    list_of_elements.append(element1+element2)
    del list_of_elements[0]
    n=list_of_elements[-1]
    if check(n):
        break
print(f'count={count}')
