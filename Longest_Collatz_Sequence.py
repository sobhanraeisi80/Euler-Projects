def collatz_sequence(n):
    count=1
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        count+=1
    return count+1

def longest(n):
    number=1
    max_l=0
    starting_number=1
    while number<n+1:
        
        if (term:=collatz_sequence(number))>max_l:
            starting_number=number
            max_l=term
        number+=1
    return starting_number
print(f'number:{longest(1000000)} has longest sequence')