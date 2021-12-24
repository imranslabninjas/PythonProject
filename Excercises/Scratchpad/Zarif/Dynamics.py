import random

input_number = random.randint(1, 10)
guess_num = 0
while guess_num != input_number:
    guess_num = int(input("Please guess again:  "))
else:
    print("WELL GUESSED")
