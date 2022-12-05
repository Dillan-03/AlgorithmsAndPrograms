#Program which converts decimal to binary representation through recursion
import math

holder = []
def dectobin(x,holder):

	if x > 0:
		holder.append(str((x%2)))
		dectobin(math.floor(x/2),holder)
	temp = holder[::-1]
	return ''.join(temp)

var = dectobin(13,holder)

print(var)
		
