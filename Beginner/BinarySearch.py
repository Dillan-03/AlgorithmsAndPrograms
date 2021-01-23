#!/Users/Dillan/PersonalProgramming/Python/Project_Env/bin/python

def binary_search_recursive(array, element):
    lo = 0
    hi = len(array)
    step = 0

    if hi < lo:
        return -1

    while lo<=hi:

        print("Subarray in step {}: {}".format(step,str(array[lo:hi+1])))
        step+=1

        mid = (lo + hi) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            hi = mid -1
        else:
            lo = mid + 1

    return -1

list = list(range(0,100,2))

user = int(input("Enter a random number: "))

print("Searching for {} in {}".format(user,list))
print("Index of {}: {}".format(user, binary_search_recursive(list,user)))
