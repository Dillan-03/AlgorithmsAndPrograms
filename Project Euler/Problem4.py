# Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.

p = []
largest = 0
for i in range(100,1000):
    for j in range(100,1000):
        z = str(i * j)
        # print("{} * {} = {}".format(i,j,z))
        
        if len(z) == 6:
            if (z[0] == z[-1] and z[1] == z[-2] and z[2] == z[3]):
                if i*j > largest:
                    largest = i*j
                
print(largest)