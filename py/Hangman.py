import random
import time
import re

# global pre_words
# global secret_word

# pre_words = ["computer","life","earth"]
# secret_word = random.choice(pre_words)

# # secret_word = secret_word.strip()

# print(secret_word)
# print("Hangman Game\n")
# name = input("Enter your name: ")
# time.sleep(3)
# print("The game is about to start!\n Let's play Hangman!")
# time.sleep(3)
# pre_words = ["computer","life","earth"]
# secret_word = random.choice(pre_words)



# def hangman():
#     global name, entered, correct ,correct_word,word_attempt, guess

#     entered = [] #To hold all of the guesses
#     correct = False
#     correct_word = False
#     word_attempt = [] #To hold the correct guesses
#     guess = 10 #Limited amount of guesses

#     print("Use the Hangman rules to guess the word")

#     while not(correct_word) and guess < 10:
#         user = str(input("Enter a character: "))

#         if user in list(secret_word):
#             print("Your letter '"+user+"' is in the word")
#             entered.append(user)
#             word_attempt.append(user)
#             guess =+1
#         else:
#             if user in entered:
#                 print("You have already entered the letter. Please try again.")
                
#             else:
#                 print("Incorrect. Please Try Again")
#                 entered.append(user)
#                 guess =+1

#         if len(word_attempt) == len(secret_word):
#             correct_word = True

# from tkinter import *

# windows = Tk()

# windows.title("Hangman Game")

# windows.mainloop()

# pre_words = ["computer","life","earth"]

#     print(secret_word)


def greeting():

    global temp
    global user_input
    global pre_words
    global secret_word
    global correct_word 
    global guess
    guess = 10
    
    global entered
    entered = []

    secret_word = str    

    print("\nWelcome to Hangman!")
    time.sleep(1)
    user_input = input("Would you like to play a game? y = Yes, n = No : " )

    while user_input not in ["Y","N","y","n"] :
          user_input = input("Would you like to play a game? y = Yes, n = No : " )
          
    if user_input in ["Y","y"]:
        pre_words = ["computer","life","earth"]
        secret_word = random.choice(pre_words)
        correct_word = '_'*len(secret_word)
        print(secret_word)
        print("A word has been randomly generated. Attempt to guess it")

# secret_word = secret_word.strip()
        # print(secret_word)
        Hangman()
    elif user_input in ["n","N"]:
        print("Thanks for playing!")
        exit()

def Hangman():

    global entered #Holds the entered guesses
    
    global secret_word
  

    # global correct #Boolean to represent whether the word has been guessed

    global correct_word #Holds the correctly guesses characters

    # global word_attempt 
    global guess #Limited amount of guesses
 
    global word_attempt #To hold the correct guesses
#     
    global user #Holds the entered character

    
    
    print("Correct guesses made: "+correct_word)
    user = str(input("Enter a character: "))

    if len(user) > 1 or user == '' or not(re.search("[a-zA-Z]", user)):
        print("Invalid guess. Please Try Again")
        print("You have "+ str(guess) +" guess remaining\n")
        Hangman()
    else:
        
        # guessing()
        guess = guess - 1
 # def guessing():
    # if user in entered:
        # print("Try again. You have already entered '"+user+"'.")
            # Hangman()
    # if user in entered:
    #     print("You have already guessed '"+user +"'. Please Try Again")
    #     Hangman()
    
    if user not in secret_word and user not in entered:
            # entered.append(user)
            if guess == 9:
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("____________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 8:
                print("\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 7:
                print("   __________________\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 6:
                print("   __________________\n")
                print("  |                  | \n")
                print("  |                  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 5:
                print("   __________________\n")
                print("  |                  | \n")
                print("  |                  |\n")
                print("  |                  O\n")
                print("  |                  |\n")
                print("  |                  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 4:
                print("   __________________\n")
                print("  |                  | \n")
                print("  |                  |\n")
                print("  |                  O\n")
                print("  |                  |\ \n")
                print("  |                  | \ \n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 3:
                print("   __________________\n")
                print("  |                  | \n")
                print("  |                  |\n")
                print("  |                  O\n")
                print("  |                 /|\ \n")
                print("  |                / | \ \n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 2:
                print("   __________________\n")
                print("  |                  | \n")
                print("  |                  | \n")
                print("  |                  O \n")
                print("  |                 /|\ \n")
                print("  |                / | \ \n")
                print("  |                   \ \n")
                print("  |                    \ \n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 1:
                print("   __________________\n")
                print("  |                  | \n")
                print("  |                  | \n")
                print("  |                  O \n")
                print("  |                 /|\ \n")
                print("  |                / | \ \n")
                print("  |                 / \  \n")
                print("  |                /   \ \n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("\nYour guess is incorrect")
                print("You now have "+str(guess)+ " guesses remaining\n")
                entered.append(user)
                Hangman()
            elif guess == 0:
                print("   __________________\n")
                print("  |  /               | \n")
                print("  | /                | \n")
                print("  |                  O \n")
                print("  |                 /|\ \n")
                print("  |                / | \ \n")
                print("  |                 / \  \n")
                print("  |                /   \ \n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("  |\n")
                print("__|_________\n")
                print("You have ran out of guesses")
                print("The word was '" + secret_word+ "'.")
                time.sleep(1)
                gameover()
    elif user in entered:
        print("You have already made this guess")
        guess += 1
        print("Guesses made "+str(entered)+".")
        Hangman()
    else:
        print("Your guess is correct")
        hold = secret_word.find(user)
        temp = list(correct_word)
        temp[hold] = user
        correct_word = ''.join(temp)
        # secret_word = secret_word.strip((user))

       
        word_attempt = secret_word[:hold] + "_" + secret_word[hold+1:]
        entered.append(user)

        if re.match(secret_word,correct_word):
            print("You have correctly guessed the word : '" + correct_word+"'\n")
            gameover()
        else:
            Hangman()
        
        

def gameover():
    print("Thank you for playing Hangman")
    exit()        
#     while not(correct_word) and guess < 10:
#         user = str(input("Enter a character: "))

#         if user in list(secret_word):y

#             print("Your letter '"+user+"' is in the word")
#             entered.append(user)
#             word_attempt.append(user)
#             guess =+1
#         else:
#             if user in entered:
#                 print("You have already entered the letter. Please try again.")
                
#             else:
#                 print("Incorrect. Please Try Again")
#                 entered.append(user)
#                 guess =+1

#         if len(word_attempt) == len(secret_word):
#             correct_word = True

greeting()
# Hangman()