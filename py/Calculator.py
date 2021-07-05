from tkinter import * 
from math import factorial

#Window Dimensions
window = Tk()

window.geometry('450x450')
window.resizable(0,0)
window.title('----------Calculator----------')
window.config(bg ='white')

#User-Input
user_input = Entry(window,width=20,font = "Robo 25",highlightthickness=2)
user_input.grid(row=1,columnspan=5, sticky=N+E+S+W)

#Answer
equation = StringVar()
answer = Entry(window, 
            textvariable = equation, 
            font = "Robo 25", 
            bg ='white',
            highlightthickness = 2,
            highlightbackground="black",
            width = 20)
answer.grid(row=0,columnspan=5,sticky=N+E+S+W)

#Operation
i = 0
def get_input(value):
    global i
    if value == "=":
        calculate(user_input.get())
    else:
        user_input.insert(i,value)
    i+=1

#Operation
def calculate(values):
    expression = str(values)+"="+str(eval(values))
    print(expression)
    equation.set(expression)
#AC
def clear():
    user_input.delete(0,END)

#Exit
def exit():
    window.destroy()

#Buttons and Special Characters
Button(window,text="9",width = 9, height = 5, command = lambda :get_input(9)).grid(row=3,column=2, sticky=N+E+S+W)
Button(window,text="8",width = 9, height = 5, command = lambda :get_input(8)).grid(row=3,column=1, sticky=N+E+S+W)
Button(window,text="7",width = 9, height = 5, command = lambda :get_input(7)).grid(row=3,column=0, sticky=N+E+S+W)
Button(window,text="4",width = 9, height = 5, command = lambda :get_input(4)).grid(row=4,column=0, sticky=N+E+S+W)
Button(window,text="5",width = 9, height = 5, command = lambda :get_input(5)).grid(row=4,column=1, sticky=N+E+S+W)
Button(window,text="6",width = 9, height = 5, command = lambda :get_input(6)).grid(row=4,column=2, sticky=N+E+S+W)
Button(window,text="1",width = 9, height = 5, command = lambda :get_input(1)).grid(row=5,column=0, sticky=N+E+S+W)
Button(window,text="2",width = 9, height = 5, command = lambda :get_input(2)).grid(row=5,column=1, sticky=N+E+S+W)
Button(window,text="3",width = 9, height = 5, command = lambda :get_input(3)).grid(row=5,column=2, sticky=N+E+S+W)
Button(window,text="0",width = 9, height = 5, command = lambda :get_input(0)).grid(row=6,column=0, sticky=N+E+S+W)
Button(window,text=" .",width = 9, height = 5, command = lambda :get_input(".")).grid(row=6,column=1, sticky=N+E+S+W)
Button(window,text="=",width = 9, height = 5, command = lambda: get_input("=")).grid(row=6,column=2, sticky=N+E+S+W)

Button(window,text="+",width = 9, height = 5, command = lambda :get_input("+")).grid(row=3,column=3, sticky=N+E+S+W)
Button(window,text="-",width = 9, height = 5, command = lambda :get_input("-")).grid(row=3,column=4, sticky=N+E+S+W)
Button(window,text="/",width = 9, height = 5, command = lambda :get_input("/")).grid(row=4,column=3, sticky=N+E+S+W)
Button(window,text="*",width = 9, height = 5, command = lambda :get_input("*")).grid(row=4,column=4, sticky=N+E+S+W)
Button(window,text="%",width = 9, height = 5, command = lambda :get_input("%")).grid(row=5,column=3, sticky=N+E+S+W)
Button(window,text="^",width = 9, height = 5, command = lambda :get_input("^")).grid(row=5,column=4, sticky=N+E+S+W)
Button(window,text="(",width = 9, height = 5, command = lambda :get_input("(")).grid(row=6,column=3, sticky=N+E+S+W)
Button(window,text=")",width = 9, height = 5, command = lambda :get_input(")")).grid(row=6,column=4, sticky=N+E+S+W)
Button(window,text="EXIT",width = 9, height = 2, command = exit).grid(row=2,column=0, sticky=N+E+S+W)
Button(window,text="AC",width = 9, height = 2, command = clear).grid(row=2,column=1, sticky=N+E+S+W)

window.mainloop()