from itertools import combinations as comb
count=0
def area(p1,p2,p3):
    a=(p1[0]*(p2[1]-p3[1]))+(p2[0]*(p3[1]-p1[1]))+(p3[0]*(p1[1]-p2[1]))
    a=(1/2)*abs(a)
    return a
f=open('0102_triangles.txt','r')
list2=[]
for _ in range(1000):
    list1=[]
    list_of_coordinates=f.readline().split(',')
    list_of_coordinates[-1]=list_of_coordinates[-1].replace('\n','')
    for i in range(len(list_of_coordinates)):
        list_of_coordinates[i]=int(list_of_coordinates[i])
    list1.append((list_of_coordinates[0],list_of_coordinates[1]))
    list1.append((list_of_coordinates[2],list_of_coordinates[3]))
    list1.append((list_of_coordinates[4],list_of_coordinates[5]))
    list2.append(list1)
for k in list2:
    sum1=0
    area_=area(k[0],k[1],k[2])
    list_of_combination=comb(k,2)
    for i in list_of_combination:
        p1=(0,0)
        sum1+=area(p1,i[0],i[1])
    if sum1==area_:
        count+=1
print(count)






