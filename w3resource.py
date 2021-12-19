# Please add question in the file so that others who are reading gets a context
# Please move the Files Under Appropriate folder (Come up with folder structure {may be Excercises/ Scratchpad/ Musa})
number = input("Type a number:")
if int(number)<1500 or int(number)>2700:
    print("The number you have type is less 1500 or bigger than 2700")
    number = input("Type a number:")
elif int(number)%5==0 and int(number)%7==0 :
    print("The number is divisible by 7 and multiple of 5")
elif int(number)%5==0:
    print("The number is a multiple of 5 ")
elif int(number)%7==0:
    print("The number is divisible by 7 ")
elif int(number)>=0 :
    print("The number isn't divisible by 7 or multiple of 5")
elif int(number)%5==0 and int(number)%7==0:
    print("The number is divisible by 7 and multiple of 5")
