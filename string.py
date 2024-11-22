
#Description:Create, concatenate, and print a string and access a sub-string from a given string
#Author:John Kuriakose
str_1=input("Enter your first name:")
str_2=input("Enter your last name:")
result=str_1+" "+str_2
print(result)
l=len(str_1)+1
last_str=result[5:14]
print(last_str)