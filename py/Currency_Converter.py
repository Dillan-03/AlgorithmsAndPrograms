#Real-Life Currency Converter

from tkinter import * 
import requests
from tkinter import ttk
from currency_symbols import CurrencySymbols
import math

#Window Dimensions
window = Tk()
window.geometry('800x350')
window.resizable(0,0)
window.title('-Currency Converter-')
window.config(bg ='white')

#ExchangeRate
url = requests.get('https://api.exchangerate-api.com/v4/latest/GBP').json() #Base Currency GBP
rates = url.get('rates')
# print(rates)

#Title 
title = Label(window,
        text=" WELCOME TO REAL TIME CURRENCY CONVERTER",
        font = "Arial 20 bold").place(x=10,y=5)

#Entries
currency = StringVar()
from_currency = Entry(window,
                text='',
                width=12,
                highlightthickness=0.2, 
                highlightbackground="black",
                textvariable = currency,
                font = 'Arial 19').place(x=200,y=170)

#Dropdown-Currencies Rate
currency_v = StringVar()
currency_v.set("GBP")
to_currency_v = StringVar()
to_currency_v.set("USD") 
 
currency_dropdown = ttk.Combobox(textvariable = currency_v,
                    values=list(rates.keys()), 
                    font = 'Arial 17', 
                    state = 'readonly', 
                    width = 12, 
                    justify = CENTER).place(x=200,y=120)
to_currency_dropdown = ttk.Combobox(textvariable = to_currency_v,
                       values=list(rates.keys()),
                       font = 'Arial 17', 
                       state = 'readonly', 
                       width = 12, 
                       justify = CENTER).place(x=400,y=120)
 
#Labels
global rate
rate = StringVar()
Label(text = 'Date: '+ url['date'], font = 'Arial 20 bold').place(x=600, y= 5)
rate = CurrencySymbols.get_symbol('GBP') + '  =  ' + CurrencySymbols.get_symbol('USD')
x = Label(window, text = rate, bg ='white', font = 'Arial 24')
x.pack()
x.place(x=310, y=60)

#Convert
def convert():
    global change
   
    different_url = requests.get(('https://api.exchangerate-api.com/v4/latest/{}').format(currency_v.get())).json() #Different base currency
    different_rates = different_url.get('rates')

    change = []
    
    change.append(CurrencySymbols.get_symbol(currency_v.get()))
    change.append(currency.get())
    change.append(' = ')
    change.append(CurrencySymbols.get_symbol(to_currency_v.get()))

    multiple = different_rates[str(to_currency_v.get())]
    multiple = float(multiple)

    change.append(str(round((float(currency.get())*multiple),2)))

    [str(x) for x in change]
    # print(change)
    
    change = "".join(change)
    
    x.config(text=change)

#Exit
def exit():
    window.destroy()

#Buttons
conv = Button(window, text = 'Exit', font = 'Arial 15', padx = 10, pady = 10, bg ='grey' ,highlightbackground='white', command = exit)
quit = Button(window, text = 'Convert', font = 'Arial 15', padx = 10, pady = 10, bg ='grey' ,highlightbackground='white', command = convert)

conv.pack()
quit.pack()

conv.place(x=600,y=250)
quit.place(x=600,y=160)


window.mainloop()