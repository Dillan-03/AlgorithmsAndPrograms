#!/Users/Dillan/PersonalProgramming/Python/Project_Env/bin/python


# Notion Number Guessing

import random
class Guess:
    correctanswer = random.randint(0,100)

    def __init__(self,number):
        self.number = number

    def check(self) -> object:
        if self.number < Guess.correctanswer:
            print("Too Low, Please Try again")
            print('')
            return True
        elif self.number > Guess.correctanswer:
            print("Too High, Please Try Again")
            print('')
            return True
        else:
            return False

user_guess = int(input("A random number has generated. Attempt to guess the number: "))
guess = Guess(user_guess)

while guess.check() == True:
    user_guess = int(input("A random number has generated. Attempt to guess the number: "))
    guess = Guess(user_guess)

print("Congratulations, You have correctly guessed the number.")
