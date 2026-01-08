def fibonacci(value):
    list_of_element=[1,1]
    sum=0
    last_element=1
    while last_element < value:
        element1=list_of_element[-1]
        element2=list_of_element[-2]
        list_of_element.append(element1+element2)
        last_element=list_of_element[-1]
        if (last_element)%2==0:
            sum+=last_element
    return sum
print(fibonacci(4e7))