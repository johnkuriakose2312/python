"""
Author:JOHN KURIAKOSE
Date:18 October
Description:Python program that demonstrates the usage of arithmetic, comparison, and
 logical operators.
 Expected Output:

Sum: 15, Division: 2.0

Is a greater than b?: True

Are a and b equal?: False

Logical AND: True

Logical OR: True


"""
No_1=int (input("Enter the first number:"))
No_2=int(input("Enter the second number:"))
print("Sum:",No_1+No_2,"Division:",No_1/No_2)

print("Is No_1 greater than No_2?:",No_1>No_2)
print("Are No_1 and No_2 equal?:",No_1==No_2)
print("Logical AND:",No_1>0 and No_2>0 )
print("Logical OR:",No_1>0 or No_1<0)
