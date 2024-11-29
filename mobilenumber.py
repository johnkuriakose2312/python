def mobile_number(num):
    if len(num)==10 and num[0] in "789":
        print("The mobile number is valid")
    else:
        print("The mobile number is not valid")
num=input("Enter a mobile number:")
mobile_number(num)