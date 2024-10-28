### Part Two -- your code goes here. 
import random
CorrectNum = random.randint(1,100)
Number = 0

while Number != CorrectNum:
    Number = int(input("guess a number between 1 to 100."))
    if Number > CorrectNum:
        print("number is higher than the correct one , try again")
    elif Number < CorrectNum:
        print("number is lower than the correct one, try again")
    else:
        print("number is correct!")
    