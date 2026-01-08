from math import sqrt
def squre(n):
    squre_root=sqrt(n)
    if int(squre_root)**2==n:
        return int(squre_root)
    else:
        return squre_root
n=1
list1=[]
while len(list1)<=5:
    triangle=n*(n+1)//2
    check_pen=squre((24*triangle)+1)
    check_hex=squre((8*triangle)+1)
    if isinstance(check_pen, int) and ((check_pen+1)%6==0) and (check_pen%6==5):
        if isinstance(check_hex, int) and ((check_hex+1)%4==0):
            print(triangle)
            list1.append(triangle)
    n+=1    
print(list1)








