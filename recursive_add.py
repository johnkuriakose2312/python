#Description:Recursive function to add two positive numbers.
def recursive_add(m,n):
    if n==0:
       return m
    else:
        return recursive_add(m+1,n-1)
num_1=int(input("Enter the number:"))
num_2=int(input("Enter the number:"))
print("Sum is",recursive_add(num_1,num_2))