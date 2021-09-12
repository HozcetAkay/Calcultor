print("Please choose your gender")
print("1-Female\n2-Male")
gender=int(input())

print("Please enter your age :\t")
age=int(input())

print("Please enter your weight:\t")
weight=int(input())

print("Please enter your height :\t")
height=int(input())

if(weight>0) and (height>0) and (gender==1 or gender==2):
    if(gender==1):
        idealweight=int(45.5+2.3*(height/2.54-60))
        if(idealweight<weight):
            print("Your ideal weight is :"+str(idealweight))
            print("To have ideal weight you should lose :"+str(weight-idealweight))
        elif(idealweight>weight):
            print("Your ideal weight is :"+str(idealweight))
            print("To have ideal weight you should gain :"+str(idealweight-weight))
        else:
            print("Your ideal weight is :")
            print("Your weight is ideal !")
    else:
        idealweight=int(45.5+2.3*(height/2.5-60))
        if(idealweight<weight):
            print("Your ideal weight is :"+str(idealweight))
            print("To have ideal weight you should lose :"+str(weight-idealweight))
        elif(idealweight>weight):
            print("Your ideal weight is :"+str(idealweight))
            sub=int(idealweight-weight)
            print("To have ideal weight you should gain :"+str(sub))
        else:
            print("Your ideal weight is :")
            print("Your weight is ideal !")
else:
    print("Please enter a valid weight and valid height")