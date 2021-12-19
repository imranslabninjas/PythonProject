# Please add question in the file so that others who are reading gets a context

temp = input("What's the temp\n")
con1 = input("Convert into C or celcius and F for farenheit\n")
con2 = 0
if str(con1) == "C":
    con2 = int(temp) - 32* 5 / 9
elif str(con1) == "F":
    con2 = int(temp) * 9 / 5+32
print(con2)

