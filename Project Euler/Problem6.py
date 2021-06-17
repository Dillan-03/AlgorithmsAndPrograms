# Sum square difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum = 0 
square = 0
for i in range(1,101):
    sum += i**2
    square += i
    squared = square ** 2 
    
print(squared-sum)
