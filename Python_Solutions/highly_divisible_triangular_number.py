def num_of_factors(n):
    import math
    count=0
    squre=(math.sqrt(n))
    
    if isinstance(squre,int):
        for i in range(1, squre+1):
            if n%i==0:
                count+=2
        return count-1
    else:
        for j in range(1, int(squre)+1):
            if n%j==0:
                count+=2
        return count

def triangular_number(n):
    number=1
    t_number=1
    while (True):
        nf=num_of_factors(t_number)
        print(t_number, nf)
        if nf>n:
            break
        else:
             number+=1
             t_number=(number*(number+1))//2
        
    return t_number
print(triangular_number(500))