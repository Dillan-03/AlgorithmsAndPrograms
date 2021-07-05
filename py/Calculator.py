from tkinter import * 
from math import factorial

#Window Dimensions
window = Tk()

window.geometry('450x450')
window.resizable(0,0)
window.title('----------Calculator----------')
window.config(bg ='white')

#User-Input
# user_input = tk.StringVar()

user_input = Entry(window,width=20,font = "Robo 25",highlightthickness=2)

            # textvariable = user_input, 
            # 
            # bg ='white',
            # highlightthickness = 2,
            # highlightbackground="black",
            # width = 20)
user_input.grid(row=1,columnspan=5, sticky=N+E+S+W)
# user_input.pack(padx=20)
# user_input.place(x=163,y=60)
# user_input = Entry(window).place(x=163,y=60)
# user_input.grid(row=1,columnspan=6,sticky=N+E+W+S)

# user_input.grid(row=1,columnspan=10)

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

#Answer-Label

# Label(window, text = 'Total :', bg = "white", font = 'Robo 20').grid(row=0,column=0)

#Operation
i = 0
# expression = [] 
# space = ''
def get_input(value):
    # print(value)
    global i
    if value == "=":
        calculate(user_input.get())
    #     print(expression)
    #     print(space.join(expression))
    #     # calculate(expression)
    # else:
    #     expression.append(value)
    # print("".join(expression))
    # answer.set(value.strip(','))
    # user_input.insert(i,"".join(expression))
    else:
        user_input.insert(i,value)

    i+=1

    # global i
    # length = len(value)
    # display.insert(i,value)
    # i+=length

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
# Button(window,text="EXIT",width = 9, height = 2, command = exit).place(x=10,y=113)
# Button(window,text="AC",width = 9, height = 2, command = clear).place(x=95,y=113)

# Button(window,text="9",width = 9, height = 5, command = lambda :get_input(9)).place(x=180,y=150)
# Button(window,text="8",width = 9, height = 5, command = lambda :get_input(8)).place(x=95,y=150)
# Button(window,text="7",width = 9, height = 5, command = lambda :get_input(7)).place(x=10,y=150)
# Button(window,text="4",width = 9, height = 5, command = lambda :get_input(4)).place(x=10,y=235)
# Button(window,text="5",width = 9, height = 5, command = lambda :get_input(5)).place(x=95,y=235)
# Button(window,text="6",width = 9, height = 5, command = lambda :get_input(6)).place(x=180,y=235)
# Button(window,text="1",width = 9, height = 5, command = lambda :get_input(1)).place(x=10,y=320)
# Button(window,text="2",width = 9, height = 5, command = lambda :get_input(2)).place(x=95,y=320)
# Button(window,text="3",width = 9, height = 5, command = lambda :get_input(3)).place(x=180,y=320)
# Button(window,text="0",width = 9, height = 5, command = lambda :get_input(0)).place(x=10,y=405)
# Button(window,text=" .",width = 9, height = 5, command = lambda :get_input(".")).place(x=95,y=405)
# Button(window,text="=",width = 9, height = 5, command = lambda: get_input("=")).place(x=180,y=405)

# Button(window,text="+",width = 9, height = 5, command = lambda :get_input("+")).place(x=265,y=150)
# Button(window,text="-",width = 9, height = 5, command = lambda :get_input("-")).place(x=350,y=150)
# Button(window,text="/",width = 9, height = 5, command = lambda :get_input("/")).place(x=265,y=235)
# Button(window,text="*",width = 9, height = 5, command = lambda :get_input("*")).place(x=350,y=235)
# Button(window,text="%",width = 9, height = 5, command = lambda :get_input("%")).place(x=265,y=320)
# Button(window,text="^",width = 9, height = 5, command = lambda :get_input("^")).place(x=350,y=320)
# Button(window,text="(",width = 9, height = 5, command = lambda :get_input("(")).place(x=265,y=405)
# Button(window,text=")",width = 9, height = 5, command = lambda :get_input(")")).place(x=350,y=405)
# Button(window,text="EXIT",width = 9, height = 2, command = exit).place(x=10,y=113)
# Button(window,text="AC",width = 9, height = 2, command = clear).place(x=95,y=113)

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








# window.

window.mainloop()