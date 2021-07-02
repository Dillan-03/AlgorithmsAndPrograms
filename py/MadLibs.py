import tkinter as tk

#Window Dimensions
window = tk.Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title('-----Mad Libs Story Selection-----')
window.config(bg ='lightgrey')

#Two Labels for user attention
tk.Label(window, text= 'Mad Libs Story Generator!' , bg = "lightgrey", font="Helvetica 20 bold ").pack()
tk.Label(window, text = 'Choose one story :', bg = "lightgrey", font = 'Helvetica 15 italic').place(x=30, y=60)

#Exit the game
def finish():
    window.destroy()

#A Day at the Zoo
def firststory():
    adjective = str(input("Enter a adjective: "))
    noun = str(input("Enter a noun: "))
    verbpast = str(input("Enter a verb in the past tense: "))
    adverb = str(input("Enter a adverb: "))
    anotheradjective = str(input("Enter another adjective: "))
    anothernoun = str(input("Enter another noun: "))
    thirdnoun = str(input("Enter another noun: "))
    thirdadjective = str(input("Enter another adjective: "))
    verb = str(input("Enter a verb: "))
    anotheradverb = str(input("Enter another adverb: "))
    lastverb = str(input("Enter another verb in the past tense: "))
    lastadjective = str(input("Enter another adjective: "))

    print("\nToday I went to the zoo. I saw a '{}' '{}', jumping up and down in its tree. He '{}' '{}' through the large tunnel that led to its '{}' '{}'. I got some peanuts and passed them through the cage to a gignantic grey '{}' towering above my head. Feeding that animal made me hungry. I went to get a '{}' scoop of ice-cream. It filled my stomach. Afterwards I had to '{}' '{}' to catch our bus. When I got home I '{}' my mom for a '{}' day at the zoo.".format(adjective,noun,verbpast,adverb,anotheradjective,anothernoun,thirdnoun, thirdadjective,verb,anotheradverb,lastverb,lastadjective))

#Majestic Snow
def secondstory():
    animal = str(input("Enter a animal: "))
    country = str(input("Enter a country: "))
    plural_noun = str(input("Enter a plural noun: "))
    food = str(input("Enter a food: "))
    screen = str(input("Enter a type of screen device(e.g smartphone,tablet, etc): "))
    noun = str(input("Enter a noun: "))
    verb = str(input("Enter a verb: "))
    anotherverb = str(input("Enter another verb: "))
    adjective = str(input("Enter a adjective: "))

    print("\nThe majestic '{}' has roamed the forests of '{}' for thousands of years. Today, she wanders in search of '{}'. She must find food to survive. While hunting for '{}', she found a/an '{}' hidden behind a '{}'. She has never seen anything like this before. What will she do? With the device in her teeth, she tries to '{}', but nothing happens. She takes it back to her family. When the family sees it, they quickly '{}'. Soon the device becomes '{}', and the family decides to put it back where they found it.".format(animal,country,plural_noun,food,screen,noun,verb,anotherverb,adjective))
def thirdstory():
    verb = str(input("Enter a verb: "))
    first_noun = str(input("Enter a noun: "))
    adverb = str(input("Enter a adverb: "))
    pastverb = str(input("Enter a verb (past tense): "))
    plural_noun = str(input("Enter a plural noun: "))
    anotherplural_noun = str(input("Enter anohter plural noun: "))
    adjective = str(input("Enter a adjective: "))
    third_pluralnoun = str(input("Enter a plural noun: "))
    verb_ing = str(input("Enter a verb ending in -ing: "))
    color = str(input("Enter a colour: "))
    fourth_plural_noun = str(input("Enter a plural noun: "))
    noun = str(input("Enter a noun: "))
    another_noun = str(input("Enter another noun: "))
    interjection = str(input("Enter a interjection: "))
    another_adjective = str(input("Enter a adjective: "))
    another_verb = str(input("Enter a verb: "))
    third_adjective = str(input("Enter a adjective: "))
    fourth_adjective = str(input("Enter one more adjective: "))

    print("\nO say can you '{}' by the dawn's early '{}'. What so '{}' we '{}' at the twilight's last gleaming. Whose brand '{}' and bright '{}' through the '{}' fight, O'er the '{}' we watched, were so gallantly '{}'? And the rockets' '{}' glare, the '{}' bursting in '{}', Gave proof through the night that our '{}' was still there; '{}' does that '{}' banner yet '{}', O'er the land of the '{}' and the home of the '{}'?".format(verb, first_noun, adverb,pastverb,plural_noun,anotherplural_noun,adjective,third_pluralnoun,verb_ing,color,fourth_plural_noun,noun,another_noun,interjection,another_adjective,another_verb,third_adjective,fourth_adjective))

tk.Button(window, width = 25, text = 'A Day At The Zoo', font = 'Helvetica 15', padx = 10, pady = 10, bg ='grey', command = firststory).place(x=182,y=53)
tk.Button(window, width = 25, text = 'Majestic Snow', font = 'Helvetica 15', padx = 10, pady = 10, bg ='grey', command = secondstory).place(x=182,y=103)
tk.Button(window, width = 25, text = 'Star Banner', font = 'Helvetica 15', padx = 10, pady = 10, bg ='grey', command = thirdstory).place(x=182,y=153)

tk.Button(window, text = 'EXIT', font = 'Helvetica 15', padx = 10, pady = 10, bg ='grey', command = finish).place(x=182,y=203)

window.mainloop()