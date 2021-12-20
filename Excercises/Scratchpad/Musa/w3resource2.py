#asking temperature
temperature = int(input("What's the temperature:"))
#asking in what to convert
converter= str(input("Do you want to convert it into c for celcius or f for farenheit:"))
if converter=="c" or converter=="C":
    print((temperature-32) * 5/9)
elif converter == "F" or converter=="f":
    print((temperature * 9/5) + 32)
#adding loop so that if user mistypes code re-runs
while converter!= "f" or converter!="F" or converter!="c" or converter !="C":
    temperature = int(input("What's the temperature:"))
    converter = str(input("Do you want to convert it into c for celcius or f for farenheit\n(PLEASE TYPE C IF YOU WANT TO CONVERT IT INTO CELCIUS AND F FOR FARENHEIT)->"))
    if converter == "c" or converter == "C":
        print((temperature - 32) * 5 / 9)
    elif converter == "F" or converter == "f":
        print((temperature * 9 / 5) + 32)