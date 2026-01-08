def fibonacci():
    list_of_elements=[1,1]
    count=2
    while True:
        count+=1
        element1=list_of_elements[-1]
        element2=list_of_elements[-2]
        list_of_elements.append(element1+element2)
        num_of_digit=len(str(list_of_elements[-1]))
        if num_of_digit==1000:
            break
    return count
print(fibonacci())
