'''
Algorithm: Selection Sort (Brute Force)
Inner loop executes in n*(n-1)/2 times
'''

def selectionSort(A):
    n = len(A)
    swappedcount = 0
    for i in range(n):
        minindex = i
        for j in range(i+1, n):
            if A[j] < A[minindex]:
                minindex = j

        #if i != minindex:
        temp = A[i]
        A[i] = A[minindex]
        A[minindex] = temp
        swappedcount += 1

    print(A, ", swappedcount = ", swappedcount)
    return A


# Execution
selectionSort([5, 6, 7, 9, 1, 3, 4])
selectionSort([55, 6, 17, 91, -1, 200, 45])
selectionSort([10, 15, 25, 34, 76, 89, 96]) # Sorted Array (Ascending)
selectionSort([96, 89, 76, 34, 25, 15, 10]) # Sorted Array (Descending)


'''
Output:
[1, 3, 4, 5, 6, 7, 9]
[-1, 6, 17, 45, 55, 91, 200]
'''
