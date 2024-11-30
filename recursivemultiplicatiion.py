#Description:Recursive function to multiply two positive numbers
def recursive_multiplication(x,y):
    if y==1:
        return x
    else:
        return x+recursive_multiplication(x,y-1)
num_1=int(input("Enter the number:"))
num_2=int(input("Enter the number:"))
if num_1>0 and num_2>0:
     print("product is:",recursive_multiplication(num_1,num_2))
else:
    print("The numbers should be positive")