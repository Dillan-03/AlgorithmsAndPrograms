#Even Fibonacci Numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

total = 0
Fibonacci = [1,2]

while Fibonacci[-1] < 4000000:
     x = Fibonacci[-1]+Fibonacci[-2]
     Fibonacci.append(x)
print(Fibonacci)

for number in Fibonacci:
    if number % 2 == 0:
        total +=number

print(total)