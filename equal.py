num=int(input("enter the number"))
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if num==num1 and num==num2 and num1==num2:
    print("All are equal")
elif num==num1 or num==num2 or num1==num2:
    print("Any of two are equal")             
else:
    print("not equal")        