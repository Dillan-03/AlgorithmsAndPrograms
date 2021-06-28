import tkinter as tk
from PIL import ImageTk,Image  
import random

#Window Dimensions
window = tk.Tk()
window.geometry('400x400')
window.resizable(0,0)
window.title('----------Dice Rolling Simulator----------')
window.config(bg ='skyblue')

#Canvas to hold the image
canvas = tk.Canvas(window, width = 270, height= 270, bg='skyblue',highlightthickness=1, highlightbackground="black")
canvas.pack()

#Dice Array to be further used
dice_array = ['1.png','2.png','3.png','4.png','5.png','6.png']

#Dice Holder
dice = ImageTk.PhotoImage(Image.open("Assets/"+random.choice((dice_array))))
ImageLabel = tk.Label(window, image=dice)
ImageLabel.image = dice

#RollDice subroutine
def rolldice():
    dice = ImageTk.PhotoImage(Image.open("Assets/"+random.choice((dice_array))))
    canvas.create_image(135,135,image=dice)   
    ImageLabel.configure(image=dice) #Update the image
    ImageLabel.image = dice #Keep a temporary holder for the dice

def exit():
    window.destroy()

#Adding a Button
tk.Button(window, text = 'ROLL DICE', font = 'Robo 15', padx = 10, pady = 10, bg ='grey' ,highlightthickness=1, highlightbackground="black", command = rolldice).place(x=146,y=300)
tk.Button(window, width = 8, text = 'EXIT', font = 'Robo 15', padx = 10, pady = 10, bg ='grey' ,highlightthickness=1, highlightbackground="black", command = exit).place(x=146,y=350)

window.mainloop()