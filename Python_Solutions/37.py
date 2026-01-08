from math import sqrt
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    squre=int(sqrt(n))
    set_of_factors=set()
    for i in range(1, squre+1):
        if n % i == 0 :
            set_of_factors.add(i)
            set_of_factors.add(n // i)
        if len(set_of_factors) > 2 :
            return False
    return True

def right_to_left (number) :
    while number > 0 :
        #print(number)
        if not (is_prime(number)) :
            return False
        number //= 10
    return True

def left_to_right (number) :
    l = len(str(number))
    for i in range (l - 1 , -1, -1) :
        #print(number)
        if not (is_prime(number)) :
            return False
        power = 10 ** i 
        rem = number % power
        digit = (number - rem) // power 
        number -= digit * power
    return True
star_number = 20 
count = 0
sum_of_number = 0
while count != 12 :
    if (left_to_right(star_number) and right_to_left(star_number)) :
        print(star_number)
        count += 1
        sum_of_number += star_number
    star_number += 1
print(f'sum = {sum_of_number}')