import tkinter as tk
import random

#Window Dimensions
window = tk.Tk()
window.geometry('1200x300')
window.resizable(0,0)
window.title('----------Welcome to the Rock, Paper, Scissors Game----------')
window.config(bg ='white')

#Creating Canvas
canvas1 = tk.Canvas(window, width = 10, height = 300)
canvas1.pack()

#Title
tk.Label(window, 	 
		 fg = "blue",
		 bg = "white",
		 font = "Helvetica 26 bold underline").pack()

#User-Input
userinput = tk.StringVar()
tk.Label(window,
        text="Choose either Rock, Paper or Scissors : ",
        font = "Arial 20 bold").place(relheight=0.3)
tk.Entry(window, 
        textvariable = userinput,
        text="1000px high",
        bg = "pink",
        font = "Arial 20 bold")

user = tk.Entry(window, width = 25, bg = "white", font=('Arial',20),highlightthickness=2, highlightbackground="black")
canvas1.create_window(-35, 45, window=user)        


#Answer Validation
answer = tk.StringVar()
#Output
tk.Entry(window, 
            textvariable = answer, 
            font = "Arial 20", 
            bg ='white',
            highlightthickness = 2,
            highlightbackground="black",
            width = 60).place(x=400, y = 100)


def rps():

    global user_input
    user_input = user.get()
    
    # #Computer_random selection
    selection = ['rock','paper','scissors']
    choice = random.choice(selection)

    #Draw
    if choice == user_input:
        answer.set("You have both selected the same answer.")
    #Computer Won 
    elif (choice == 'rock' and user_input == 'scissors') or (choice == 'rock' and user_input == 'Scissors'):
        answer.set("Rock smashes scissors. I have won this game. Better luck next time.")
    elif (choice == 'paper' and user_input == 'rock') or (choice == 'paper' and user_input == 'Rock'):
        answer.set("Paper covers rock. I have won this game. Better luck next time.")
    elif (choice == 'scissors' and user_input == 'paper') or (choice == 'scissors' and user_input == 'Paper'):
        answer.set("Scissors cuts paper. I have won this game. Better luck next time.")

    #User Won
    elif (choice == 'scissors' and user_input == 'rock') or (choice == 'scissors' and user_input == 'Rock'):
        answer.set("Rock destroys scissors. CONGRATULATIONS, You have won!")
    elif (choice == 'paper' and user_input == 'scissors') or (choice == 'paper' and user_input == 'scissors'):
        answer.set("Scissors cuts paper. CONGRATULATIONS, You have won!")    
    elif (choice == 'rock' and user_input == 'paper') or (choice == 'rock' and user_input == 'Paper'):
        answer.set("Paper covers rock. CONGRATULATIONS, You have won!")

    #Invalid input
    else:
        answer.set("Invalid input. Either choose paper, rock or scissors")
        
    
def exitgame():
    window.destroy()


def reset():
    answer.set("")
    # user.set("")
    user.delete(0, 'end')

#Button Dimensions
tk.Button(window, text = 'PLAY', font = 'Arial 15', padx = 10, pady = 10, bg ='grey' , command = rps).place(x=5,y=97)
tk.Button(window, text = 'RESET', font = 'Arial 15', padx = 10, pady = 10, bg ='grey', command = reset).place(x=87,y=97)
tk.Button(window, text = 'EXIT', font = 'Arial 15', padx = 10, pady = 10, bg ='grey', command = exitgame).place(x=182,y=97)


window.mainloop()
