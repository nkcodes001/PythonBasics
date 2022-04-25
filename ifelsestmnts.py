var1=67
var2=45

var3=int(input())

if var3>var1:
    print("Greater than ",var1)
    
elif var3==var1:
    print(" both are Equal")
    
else:
    print("Lesser than",var1)
    
list1=[2,45,67,87,99]

print(2 in list1)


if 2 in list1:
    print("Yes it is in the List")
    
print("Enter your Age Now!!!")   
age=int(input())

if age<18:
    print("Sorry your under age")
elif age>18&age<55:
    print("You are eligible for Driving liecence")
elif age>55:
    print("Sorry your too old for it")
else:
    print("Wrong Input")
    
    
    
    
