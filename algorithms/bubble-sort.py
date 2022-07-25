'''
Algorithm: Bubble Sort (Brute Force)
Best case performance can be improved to O(N) with swapped boolean variable
'''

def bubbleSort(A):
    n = len(A)
    swappedcount = 0
    for i in range(n):
        swapped = False
        for j in range(n-1, i, -1):
            if A[j-1] > A[j]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
                swapped = True
                swappedcount += 1

        if not swapped:
            break;

    print(A, ", swappedcount =", swappedcount)
    return A

'''
        j = n-1-i
        while j - 1 >= i:
            j -= 1
'''

# Execution
bubbleSort([5, 6, 7, 9, 1, 3, 4])
bubbleSort([55, 6, 17, 91, -1, 200, 45])
bubbleSort([10, 15, 25, 34, 76, 89, 96])
bubbleSort([96, 89, 76, 34, 25, 15, 10]) # Sorted Array (Descending)


'''
Output:
[1, 3, 4, 5, 6, 7, 9] , swappedcount = 12
[-1, 6, 17, 45, 55, 91, 200] , swappedcount = 9
[10, 15, 25, 34, 76, 89, 96] , swappedcount = 0
[10, 15, 25, 34, 76, 89, 96] , swappedcount = 21
'''