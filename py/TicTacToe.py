#Tic-Tac-Toe CL Game

import numpy as np
import random

def greeting():
    user_input = input("Would you like to play a game? y = Yes, n = No : " )

    while user_input not in ["Y","N","y","n"] :
        user_input = input("Would you like to play a game? y = Yes, n = No : " )
        
    if user_input in ["Y","y"]:
        board()
    elif user_input in ["n","N"]:
        print("Thanks for playing!")
        exit()

def board():
    
    print('     |     |     ')
    print('  0  |  1  |  2  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  3  |  4  |  5  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  6  |  7  |  8  ')
    print('     |     |     ')

def user_input(): #Max of 9 inputs
    dict = {}
    choice = str(input('Player 1 choose a value O or X: '))
    if choice in ['o','O','0']:
        dict['Player 1']='O'
        dict['Player 2']='X'
    else:
        dict['Player 1']='X'
        dict['Player 2']='O'  
    # counter = 0
    positions = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    # ran = random.randint(0,10)
    turn = 0
    while turn < 9:
        if turn % 2 == 0:
            whoseturn = dict['Player 1']
            # turn += 1
        else:
            whoseturn = dict['Player 2']
            # turn += 1 

        place = int(input(f'Turn: {whoseturn}\nEnter a place on the board: '))
        while place not in range(0,9):
            place = int(input(f'Turn: {whoseturn}\nEnter a place on the board: '))

        turn +=- 1
        positions[place] = whoseturn
        # print(place)
        updateboard(positions,dict)
        # validation(positions,dict)
    # pass

def updateboard(positions,dict):
    # print(positions)
    print('\n')
    print('     |     |     ')
    print(' ',positions[0],' | ',positions[1],' | ',positions[2],' ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(' ',positions[3],' | ',positions[4],' | ',positions[5],' ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(' ',positions[6],' | ',positions[7],' | ',positions[8],' ')
    print('     |     |     ')
    validation(positions,dict)

def validation(positions,won):
    # print(won)
    winner = False 
    if positions[0] == 'X' and positions[1] == 'X' and positions[2] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winer = True
        print(*myKey + 'is the winner !')
    elif positions[3] == 'X' and positions[4] == 'X' and positions[5] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[6] == 'X' and positions[7] == 'X' and positions[8] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[0] == 'X' and positions[3] == 'X' and positions[6] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[1] == 'X' and positions[4] == 'X' and positions[7] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[2] == 'X' and positions[5] == 'X' and positions[8] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[0] == 'X' and positions[4] == 'X' and positions[8] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[2] == 'X' and positions[4] == 'X' and positions[6] == 'X':
        myKey= [player for player,choice in won.items() if choice=="X"]
        winner = True
        print(*myKey + 'is the winner !')    
    elif positions[3] == 'O' and positions[4] == 'O' and positions[5] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[6] == 'O' and positions[7] == 'O' and positions[8] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[0] == 'O' and positions[3] == 'O' and positions[6] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[1] == 'O' and positions[4] == 'O' and positions[7] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[2] == 'O' and positions[5] == 'O' and positions[8] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[0] == 'O' and positions[4] == 'O' and positions[8] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif positions[2] == 'O' and positions[4] == 'O' and positions[6] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey , 'is the winner !')    
    elif positions[2] == 'O' and positions[4] == 'O' and positions[6] == 'O':
        myKey= [player for player,choice in won.items() if choice=="O"]
        winner = True
        print(*myKey + 'is the winner !')
    elif ['X','O'] in positions:
        print("A draw has been played")
        
    # if winner == False:
        # print('It is a draw')
        # exit()
    # elif
    #     pass
    # pass


greeting()
user_input()