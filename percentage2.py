science=int(input(""))
marathi=int(input(""))
hindi=int(input(""))
english=int(input(""))
math=int(input(""))
Total=science+marathi+hindi+english+math
percentage=(Total/500.0)*100
if percentage<25:
    print("F")
elif percentage>=25 and percentage<=45:
    print("E") 
elif percentage>=45 and percentage<50:
    print("d") 
elif percentage>=50 and percentage<60:
    print("c")  
elif percentage>=60 and percentage<80:
    print("b")
elif percentage>80:
    print("a")    
