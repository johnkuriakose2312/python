rows=int(input("Enter the number of rows:"))
for i in range(1,rows+1):
    print("*"*i)

rows=int(input("Enter the number of rows:"))
for i in range(rows):
    print("*"*(rows-i))

rows=int(input("Enter the number of rows:"))
for m in range(1,rows+1):
    for n in range(rows-m):
        print(" ",end=" ")
    for o in range(2*m-1):
         print("*",end=" ")
    print('')
rows = int(input("Enter the number of rows:"))
for m in range(rows,0,-1):
    for n in range(rows - m):
        print(" ", end=" ")
    for o in range(2 * m - 1):
        print("*", end=" ")
    print('')