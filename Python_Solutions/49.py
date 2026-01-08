from math import sqrt

def is_prime (number) :
    if number <= 1 :
        return False
    if number == 2 :
        return True
    if number % 2 == 0 :
        return False
    
    square_root = int (sqrt(number)) + 1
    
    for d in range(3, square_root) :
        if number % d == 0 :
            return False
    return True

list_of_primes = []

def is_permution (number1, number2) :
    list_of_digit_number1 = list (str (number1))
    list_of_digit_number2 = list (str (number2))
    list_of_digit_number1.sort()
    list_of_digit_number2.sort()
    return list_of_digit_number1 == list_of_digit_number2


for number in range(100000, 1000000) :
    if is_prime(number) :
        list_of_primes.append(number)


for prime_number in list_of_primes :
    ratio = 2
    copy_of_prime_number = prime_number
    #print(copy_of_prime_number)
    
    while (prime_number < 1000000) :
        #print(prime_number)
        list_of_sequence = [copy_of_prime_number]
        prime_number = copy_of_prime_number
        for i in range(2) :
            prime_number += ratio
            if is_permution (copy_of_prime_number, prime_number) and is_prime (prime_number) :
                list_of_sequence.append (prime_number)
            else :
                break 
        if len(list_of_sequence) == 3 :
            print(list_of_sequence)
            break
        ratio += 2
