#Multiples of 3 and 5
#Find the sum of all the multiples of 3 or 5 below 1000

x = 1
total = 0
while x < 1000:
    if (x % 3 == 0) or (x % 5 == 0):
        total +=x
    x+=1
print(total)
