#BUBBLE SORT

def bubble_sort(numbers,length):
    swapped = True


    while swapped==True:
        swapped = False
        for i in range(1,length):
            if numbers[i-1] > numbers[i]:
                temp = numbers[i-1]
                numbers[i-1] = numbers[i]
                numbers[i] = temp
                swapped = True
                print(numbers)


holder = []
length = int(input("Enter length of list: "))
for i in range(0,int(length)):
    num = input("At index["+str(i)+"] Enter a number: ")
    holder.append(int(num))

bubble_sort(holder,int(length))