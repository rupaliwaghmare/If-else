Hight=float(input("enter the hight"))
weight=float(input("enter the weight"))
BMI=weight%(Hight)*2
if weight<18.5:
    print("underweight")
elif weight>=18.5 and weight<24.9:
    print("normal") 
elif weight>25.0 and weight<29.9:
    print("overweight") 
elif weight>30.0:
    print("obese")          
