def is_palindromic(n):
    n=str(n)
    n_reverse=n[::-1]
    if n==n_reverse:
        return True
    return False
number_of_lyrich=0
for n in range(1,10001):
    count=0
    n_saved=n
    for _ in range(0,50):
        str_n=str(n)
        str_n_r=str_n[::-1]
        res=int(str_n)+int(str_n_r)
        if not(is_palindromic(res)):
            n=res
            count+=1
        else:
            break
    if count==50:
        print(n_saved)
        number_of_lyrich+=1
print(number_of_lyrich)