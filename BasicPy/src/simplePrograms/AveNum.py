
def avg():
    n = int(input("Enter the list of numbers"))
    a =[]
    for i in range(0,n):
        num = int(input("enter the elements of array: "))
        a.append(num)
    print(a)
    print(sum(a))    
    avg = sum(a)/n
    
    print("Average of elements in the list :" , avg)
    
print(avg)
