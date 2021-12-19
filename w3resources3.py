# Please add question in the file so that others who are reading gets a context
# Please move the Files Under Appropriate folder (Come up with folder structure {may be Excercises/ Scratchpad/ Musa})

guessnum = input("Guess a number:")
if int(guessnum)<1 or int(guessnum)>9:
    guessnum = input("Guess a number:")
elif int(guessnum)>=1 and int(guessnum)<=9:
    print("Well guessed!")


