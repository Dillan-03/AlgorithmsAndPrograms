#Program which converts decimal to binary representation through recursion
import math

holder = []
def dectobin(x):
	# input decimal integer x 
	# output binary representation

	if x > 0:
		dectobin(math.floor(x/2))
		holder.append(x%2)
	return ''.join(map(str, holder))

var = dectobin(13)

print(var)


