#Collection of Algorihms and Data Structures

##Algorithms

### Bubble Sort
A Bubble sort is a simple sorting algorithms which works by repeatedly going through the list and comparing each pair of adjacent items and swapping them if they are in wrong order. 
A pass is made through the data, comparing each value with the following one and swapping them if necessary.
A number of passes are made until the data is in order.  When a pass is made through the entire list and no swaps are needed , it would indicate that the list has been sorted.

Space Complexity is O(1) as the temp variable is being store in memory 

### Insertion Sort
Insertion Sort is a simple algorithm , efficient for small lists. It works by starting with the second item in the list, comparing all of the items before it in the list and shifting them up one place until the correct place to insert it is found.

Space Complexity is O(1) 

### Quicksort

Quicksort is a more complex sorting algorithm to understand, but it is much faster at sorting longer list. It uses a recursive(keeps looping) approach to sort the list.
Concept behind Quicksort:
- Choose a pivot in the list (data before the pilot as ListA and after the pilot as ListB). The pivot will be the midpoint of the list.
- Move data less than the pivot into List A and data after the pivot in ListB.
- Quicksort ListA and ListB.
- Firstly you would choose a pivot ( ideally the middle index from the list) . Data before the pivot = ListA and data after the pivot as ListB . You would start by choosing the itemfromleft which is greater than the pivot and the itemfromright which is smaller than the pivot. Swap the items. Continue doing this. You would stop when itemfromleft > itemfromright. Swap itemfromleft with pivot. Further Quicksort ListA and ListB.

As it is a recursive algorithm, some may argue that it uses more memory during executing therefore is an inefficient sorting algorithm.

6 steps to perform Quicksort:
1) Find a pivot (ideally the middle item in the list)
2) Choose the first ItemfromLeft that is larger than the pivot
3) Choose the first ItemfromRight that is smaller than the pivot
4) Swap them
5) Stop when ItemfromLeft > ItemfromRight
6) Swap ItemfromLeft with pivot

Time Complexity is O(nlogn)

Space Complexity is O(logn)





##Data Structures





##Big O Notation and Time Complexity


