string='0'
for n in range(1,10**6+3):
    string+=str(n)
num=int(string[1])*int(string[10])*int(string[100])*int(string[1000])*int(string[10000])*int(string[100000])*int(string[1000000])
print(num)