# Please add question in the file so that others who are reading gets a context

guessnum = input("Guess a number:")
if int(guessnum)<1 or int(guessnum)>9:
    guessnum = input("Guess a number:")
elif int(guessnum)>=1 and int(guessnum)<=9:
    print("Well guessed!")


