#QUICKSORT 

global Hi,Lo,TempLo,TempHi

def quicksort(numbers,Lo,Hi):
    TempLo = Lo
    TempHi = Hi
    pivot =  (round((Lo + Hi)/2))

    while TempLo <= TempHi:

        while numbers[TempLo] < pivot and TempLo < Hi:
            TempLo = TempLo + 1  
        while numbers[TempHi] > pivot and TempHi > Lo:
            TempHi = TempHi - 1 

        if TempLo <= TempHi: 
            temp = numbers[TempLo]
            numbers[TempLo] = numbers[TempHi]
            numbers[TempHi] = temp
            TempLo = TempLo + 1 
            TempHi = TempHi - 1 
      
        if TempLo < Hi: quicksort(numbers,TempLo,Hi)
        if TempHi > Lo: quicksort(numbers,Lo,TempHi)
    return numbers
    

holder = []
length = int(input("Enter length of list: "))
for i in range(0,int(length)):
    num = input("At index["+str(i)+"] Enter a number: ")
    holder.append(int(num))

print(quicksort(holder,0,int(length)-1))