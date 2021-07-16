import tkinter as tk
from PIL import ImageTk,Image  
import random

#Window Dimensions
window = tk.Tk()
window.geometry('800x600')
window.resizable(0,0)
window.title('---Address Book---')
window.config(bg ='lightgrey')

#Inputs
name = tk.StringVar()
phonenum = tk.StringVar()
email = tk.StringVar()

tk.Label(window, bg='lightgrey', text="Name : ", font = "Arial 16 bold").place(x=10,y=30)
tk.Label(window, bg='lightgrey', text="Contact Number : ", font = "Arial 16 bold").place(x=10,y=80)        
tk.Label(window, bg='lightgrey', text="Email : ", font = "Arial 16 bold").place(x=10,y=130)      

tk.Entry(window, textvariable = name,bg = "lightgrey", font = "Arial 16").place(x=75,y=27)
tk.Entry(window, textvariable = phonenum, bg = "lightgrey", font = "Arial 16").place(x=160,y=77)
tk.Entry(window, textvariable = email, bg = "lightgrey", font = "Arial 16").place(x=75,y=127)

#Contact List
frame = tk.Frame(window)
frame.pack(side = tk.RIGHT)
scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
yscroll = tk.Scrollbar(frame, orient=tk.VERTICAL)

lt = tk.Listbox(frame, xscrollcommand=scroll.set, yscrollcommand=yscroll.set, height=16, width=50)

scroll.config(command=lt.xview)
scroll.pack(side = tk.BOTTOM)

yscroll.config(command=lt.yview)
yscroll.pack(side = tk.RIGHT)

lt.pack()

contacts = [
    ['Forename Surname',  '00000000000', 'Forename@email.com'],
    ['User One',  '1111111111', 'UserOne@email.com'],
    ['User Two',   '22222222222', 'UserTwo@email.com'],
    ['User Three','33333333333', 'UserThree@email.com'],
    ['User Four',   '44444444444', 'UserFour@email.com'],
    ['User Five' , '55555555555', 'UserFive@email.com'],
    ]

contacts.sort()

#Selected Index
def select_index():
    return int(lt.curselection()[0])

#Clear
def clear():
    name.set("")
    phonenum.set("")
    email.set("")
    
#Save Info
def save():
    contacts.append([name.get(),phonenum.get(),email.get()])
    refresh()

#Exit
def exit():
    window.destroy()

#Edit
def edit():
    del contacts[select_index()]
    contacts[select_index()] = [name.get(), phonenum.get(),email.get()]
    refresh()

#Delete
def delete():
    del contacts[select_index()]
    refresh()

#Refresh - Update the ListBox
def refresh():
    lt.delete(0,tk.END)
    contacts.sort()
    for Name,PhoneNumber,Email in contacts:
        lt.insert(tk.END,Name+'   '+PhoneNumber+'   '+Email)

#Buttons
tk.Button(window,text="NEW",width = 8, height = 3,bg ='white' ,highlightthickness=1, highlightbackground="black",command = clear).place(x=26,y=200)
tk.Button(window,text="SAVE", width = 8, height = 3,bg ='white' ,highlightthickness=1, highlightbackground="black", command = save).place(x=26,y=260)
tk.Button(window,text="EDIT",width = 8, height = 3,bg ='white' ,highlightthickness=1, highlightbackground="black", command = edit).place(x=26,y=320)
tk.Button(window,text="DELETE",width = 8, height = 3,bg ='white' ,highlightthickness=1, highlightbackground="black", command = delete).place(x=26,y=380)
tk.Button(window,text="EXIT",width = 8, height = 3,bg ='white' ,highlightthickness=1, highlightbackground="black", command = exit).place(x=26,y=440)


for Name,PhoneNumber,Email in contacts:
    lt.insert(tk.END,Name+'   '+PhoneNumber+'   '+Email)
    
window.mainloop()