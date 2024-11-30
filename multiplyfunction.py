def product_of_num(x):
    product=1
    for i in x:
        product*=i
    print("The product of the numbers is:",product)
count=int(input("Enter the number of values:"))
numbers=[]
for j in range (count):
    num=int(input("Enter the values:"))
    numbers.append(num)
print(numbers)
product_of_num(numbers)

