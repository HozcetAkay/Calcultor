print("-----> Welcome <-----")
firstNumber=int(input("Lütfen işlem yapılacak ilk değeri giriniz :\n"))
secondNumber=int(input("Lütfen işlem yapılacak ikinci değeri giriniz:\n"))
print("1-Toplama \n2-Çıkarma\n3-Çarpma\n4-Bölme")
firstinput=input("Lütfen yapılacak işlemi giriniz :\n")
if(type(firstNumber)==int and type(secondNumber)==int):
    if(firstinput==1):
     result=firstNumber+secondNumber
     print(result)
    elif(firstinput==2):
     result=firstNumber-secondNumber
     print(result)
    elif(firstinput==3):
     result=firstNumber*secondNumber
     print(result)
    else:
     result=int(firstNumber/secondNumber)
     print("Sonuç :{}".format(result))
else:
 print("GEÇERSİZ İŞLEM LÜTFEN TEKRAR DENEYİNİZ...")