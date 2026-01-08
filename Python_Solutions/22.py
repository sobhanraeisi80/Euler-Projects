f=open('0022_names.txt','r')
list_of_names=f.readline()
list_of_names=list_of_names.split(',')
list_of_names.sort()
sum2=0
for word in list_of_names:
    sum1=0
    index=list_of_names.index(word)
    word=word.lower()
    for w in word:
        if w=='"':
            continue
        sum1+=ord(w)-96
    sum2+=sum1*(index+1) 
print(sum2)

