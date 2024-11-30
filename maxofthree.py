def max_of_three(x):
    x.sort()
    print("Max of the three given numbers is ",x[2])
num1=int(input("Enter the number one:"))
num2=int(input("Enter the number two:"))
num3=int(input("Enter the number three:"))
num=[num1,num2,num3]
max_of_three(num)
