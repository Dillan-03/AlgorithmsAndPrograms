#SERIAL SEARCH

import random

def serial():
    preset = random.sample(range(0, 20), 10)
    number = random.randint(0,10)

    for i in range(0,len(preset)):
        if preset[i] == number:
            return True

go = serial()

if go == True:
    print('Number is in the list')
else:
    print("Number does not exist in the preset list")