#Input a number to determine whether it is part of the Fibonacci sequence

holder = [0,1]

def Fibonacci(value):
    while holder[-1] < value:
        holder.append((holder[-1]+holder[-2]))
        
    if holder[-1] == value:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if Fibonacci(number):
    print(number,"is in the Fibonacci sequence")
else:
    print(number,"is NOT in the Fibonacci sequence")
