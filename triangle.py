'''def right_triangle(side1,side2,side3):
    if (side1**2) == (side2**2) + (side3**2) or  (side2**2) == (side1**2) + (side3**2) or  (side1**3) == (side2**2) + (side3**1):
        print("This is a right triangle")
    else:
         print("This is not a right triangle")
side1=input("enter side one:")
side2=input("enter side two:")
side3= input("enter side three:")
right_triangle(side1,side2,side3)'''


def right_triangle(x):
    x.sort()
    if x[2]**2==(x[1]**2)+(x[0]**2):
        print("This is a right triangle:")
    else:
         print("This is not a right triangle:")
side1=int(input("Enter side one:"))
side2=int(input("Enter side two:"))
side3=int(input("Enter side three:"))
sides=[side1,side2,side3]
right_triangle(sides)