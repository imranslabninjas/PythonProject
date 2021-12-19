#Asking user to input a temperatre value
temp= int(input("What' the temperature:"))
#Asking user in what to convert the temperature in.
converter=str(input("Do you want to convert it into c for Celcius or in f for Farenheit\n"))
#Using if statements  to convert value
if converter == "f" or "F":
    print((5/9) * (temp - 32))
elif converter == "c" or "C":
    print((temp*9/5)+32)






