#INSERTION SORT

def insertion_sort(numbers,length):

    for i in range(length): 
        temp = numbers[i]
        z = i 
        while z > 0 and numbers[z-1] > temp:
            numbers[z] = numbers[z-1]
            z = z - 1 
        
            numbers[z] = temp
        print(numbers)
    

holder = []
length = int(input("Enter length of list: "))
for i in range(0,int(length)):
    num = input("At index["+str(i)+"] Enter a number: ")
    holder.append(int(num))

insertion_sort(holder,int(length))