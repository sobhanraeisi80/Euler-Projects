f=open('008.txt','r')
string=f.read()
max_product=0
for i in range(0,987):
    product=1
    for j in range(i,i+13):
        product*=int(string[j])
    if product>max_product:
        max_product=product
print(max_product)
        
