# Please add question in the file so that others who are reading gets a context
# Please move the Files Under Appropriate folder (Come up with folder structure {may be Excercises/ Scratchpad/ Zarif})

temp = input("What's the temp\n")

# Do you know what is the meaning of \n used above? worth a google search
# Please put your favorite article as a comment for future reader

con1 = input("Convert into C or celcius and F for farenheit\n")
# Lets try to name the variable names appropriately. con1 does not mean anything. You can write temperature or ~

con2 = 0
if str(con1) == "C":
    # What will happen when the user will put c with the smaller letter
    con2 = int(temp) - 32* 5 / 9

elif str(con1) == "F":
    # What if the user pressee F with a dot, how do you validate? - food for thought.
    con2 = int(temp) * 9 / 5+32

    # What about when the user enters anything else like "Moon"
print(con2)

