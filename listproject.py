#Author=John Kuriakose
L1=[55,82,47,97,2,15,91,5,9,6,]
L2=[10,6,99,54,38,2,80,60]
print("First List:",L1)
print("Second List:",L2)
L3=L1+L2

even_list=[]
odd_list=[]
for i in L3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
L4=even_list+odd_list
print("Combined list:",L4)