#Exchange Range Converter
import requests 
from tkinter import * 
from tkinter import ttk
from currency_symbols import CurrencySymbols



#Window Dimensions
window = Tk()
window.geometry('500x800') #width * height
window.resizable(0,0)
window.title('')
window.config(bg ='white')

#Title
title = Label(window,
        text="CURRENCY CONVERTER",
        font = "Arial 20 bold").place(x=0,y=5)

#Entries
currency = StringVar()
from_currency = Entry(window,
                text='',
                width=18,
                highlightthickness=0.7, 
                highlightbackground="black",
                textvariable = currency,
                font = 'Arial 19')
from_currency.place(x=230,y=80)

tocurrency = StringVar()
to_currency = Entry(window,
                text='',
                width=18,
                highlightthickness=0.7, 
                highlightbackground="black",
                textvariable = tocurrency,
                font = 'Arial 19')
to_currency.place(x=230,y=140)

#ExchangeRate
url = requests.get('https://api.exchangerate-api.com/v4/latest/GBP').json() #Base Currency GBP
rates = url.get('rates')

# Dropdown-Currencies Rate
currency_from = StringVar()
currency_from.set("GBP")
currency_to = StringVar()
currency_to.set("USD") 
 
currency_dropdown = ttk.Combobox(textvariable = currency_from,
                    values=list(rates.keys()), 
                    font = 'Arial 19', 
                    state = 'readonly', 
                    width = 12, 
                    justify = CENTER).place(x=60,y=80)
to_currency_dropdown = ttk.Combobox(textvariable = currency_to,
                       values=list(rates.keys()),
                       font = 'Arial 19', 
                       state = 'readonly', 
                       width = 12, 
                       justify = CENTER).place(x=60,y=140)
 
#Functions
 
#Button Input Function
i = 0 #hold the number of times a button is pressed
def get_input(num):
    global i
    from_currency.insert(i,num)
    i += 1
    

#clear
def clear():
    pass

#ac
def ac():
    from_currency.delete(0,END)
    to_currency.delete(0,END)
    i = 0

#Exit
def exit():
    window.destroy()

#Convert the exchange
def convert() :
    different_url = requests.get(('https://api.exchangerate-api.com/v4/latest/{}').format(currency_from.get())).json() #Different base currency
    different_rates = different_url.get('rates')

    #Call calculate function
    value = calculate(different_rates)

    #Inserting the conversion back into the entries
    #From Currency
    temp = currency.get()
    from_currency.delete(0,END)
    from_currency.insert(0,CurrencySymbols.get_symbol(currency_from.get()))
    from_currency.insert(1,temp)

    #To Currency
    temp = currency.get()
    to_currency.delete(0,END)
    # from_currency.insert(0,CurrencySymbols.get_symbol(currency_from.get()))
    # to_currency.insert(1,temp) 
    # to_currency.delete(0,END)

    to_currency.insert(0,CurrencySymbols.get_symbol(currency_to.get()))
    to_currency.insert(1,value)

#Complete the conversion
#And send it back to the convert function 
def calculate(rates):
    conversion = float(rates[str(currency_to.get())])
    cal = round(float(currency.get())*conversion,3)
    return cal


#Buttons
btn1 = Button(window,text="9",width = 10, height = 6,command = lambda :get_input(9))
btn1.place(x=320, y=300)

btn2 = Button(window,text="8",width = 10, height = 6, command = lambda :get_input(8))
btn2.place(x=190, y=300)

btn3 = Button(window,text="7",width = 10, height = 6, command = lambda :get_input(7))
btn3.place(x=60,y=300)

btn4 = Button(window,text="4",width = 10, height = 6, command = lambda :get_input(4))
btn4.place(x=60, y=410)

btn5 = Button(window,text="5",width = 10, height = 6, command = lambda :get_input(5))
btn5.place(x=190, y=410)

btn6 = Button(window,text="6",width = 10, height = 6, command = lambda :get_input(6))
btn6.place(x=320, y=410)

btn7 = Button(window,text="1",width = 10, height = 6, command = lambda :get_input(1))
btn7.place(x=60,y=520)

btn8 = Button(window,text="2",width = 10, height = 6, command = lambda :get_input(2))
btn8.place(x=190, y=520)

btn9 = Button(window,text="3",width = 10, height = 6, command = lambda :get_input(3))
btn9.place(x=320, y=520)

btn10 = Button(window,text="0",width = 10, height = 6, command = lambda :get_input(0))
btn10.place(x=60,y=630)

btn11 = Button(window,text=" .",width = 10, height = 6, command = lambda :get_input("."))
btn11.place(x=190,y=630)

btn12 = Button(window,text = "AC",width = 10, height = 6, command = lambda :ac())
btn12.place(x=320,y=630)

btn13 = Button(window,text = "CONVERT",width = 8, height = 4, command = lambda :convert())
btn13.place(x=120,y=200)

btn14 = Button(window,text = "EXIT",width = 8, height = 4, command = lambda :exit())
btn14.place(x=270,y=200)
















window.mainloop()