def sum_of_num(x):
    sum=0
    for i in x:
        sum+=i
    print("The sum of the numbers is:",sum)
count=int(input("Enter the number of values:"))
numbers=[]
for j in range (count):
    num=int(input("Enter the values:"))
    numbers.append(num)
print(numbers)
sum_of_num(numbers)




