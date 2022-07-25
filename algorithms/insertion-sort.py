'''
Algorithm: Insertion Sort (Decrease and Conquer)
Shift Elements to right when you find a smaller element.
Start from 2nd element.
'''

def insertionSort(A):
    n = len(A)
    swappedcount = 0
    for i in range(1,n):
        j = i - 1
        temp = A[i]
        while j >= 0 and A[j] > temp:
            A[j+1] = A[j]
            j -= 1
            swappedcount += 1

        A[j+1] = temp

    print(A, ", swappedcount = ", swappedcount)
    return A


# Execution
insertionSort([5, 6, 7, 9, 1, 3, 4])
insertionSort([55, 6, 17, 91, -1, 200, 45])
insertionSort([10, 15, 25, 34, 76, 89, 96]) # Sorted Array (Ascending)
insertionSort([96, 89, 76, 34, 25, 15, 10]) # Sorted Array (Descending)


'''
Output:
[1, 3, 4, 5, 6, 7, 9] , swappedcount =  12
[-1, 6, 17, 45, 55, 91, 200] , swappedcount =  9
[10, 15, 25, 34, 76, 89, 96] , swappedcount =  0
[10, 15, 25, 34, 76, 89, 96] , swappedcount =  21
'''
