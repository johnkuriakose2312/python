def gcd(num1,num2):
    if num1 % num2 ==0:
        return num2
    else:
        return gcd(num2,num1 % num2)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
gcd(number1,number2)
if number1<0 and number2<0:
      print("ERROR:Enter positive numberS")
else:
  print("The Gcd of the two numbers is", gcd(number1, number2))