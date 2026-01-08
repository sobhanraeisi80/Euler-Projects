from math import pow
import sys
sys.set_int_max_str_digits(0)
f=open('0099_base_exp.txt','r')
max_x=0
for i in range(1, 1001):
    a=(f.readline())
    b=a.split(',')
    base=int(b[0])
    power=int(b[1])
    x=base**power
    if x>max_x:
        max_x=x
        t=i
print(t)

