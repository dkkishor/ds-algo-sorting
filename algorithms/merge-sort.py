'''
Algorithm: Merge Sort (Divide & Conquer)
Divides elements into 2 halves and sorts them recursively.
Merging & Sorting happens starting from the parent of the leaf node.
'''

def helper(A, start, end):
    # Handle Leaf node
    if start == end:
        return

    #identify the mid point
    mid = start + ((end - start) // 2)

    # call mergesort for first half
    helper(A, start, mid)
    # call mergesort for second half
    helper(A, mid + 1, end)

    # Merge 2 sorted halves from above.
    idx1 = start
    idx2 = mid + 1
    aux = []
    while idx1 <= mid and idx2 <= end:
        if A[idx1] <= A[idx2]:
            aux.append(A[idx1])
            idx1 += 1
        else:
            aux.append(A[idx2])
            idx2 += 1

    # Add remaining elements from first half
    while idx1 <= mid:
        aux.append(A[idx1])
        idx1 += 1

    # Add remaining elements from second half
    while idx2 <= end:
        aux.append(A[idx2])
        idx2 += 1

    # Overwrite main array with values from sorted array
    A[start:end+1] = aux
    return


def mergeSort(A):
    helper(A, 0, len(A) - 1)
    print(A)
    return A


# Execution
mergeSort([5, 6, 7, 9, 1, 3, 4])
mergeSort([55, 6, 17, 91, -1, 200, 45])
mergeSort([10, 15, 25, 34, 76, 89, 96]) # Sorted Array (Ascending)
mergeSort([96, 89, 76, 34, 25, 15, 10]) # Sorted Array (Descending)

'''
Output:
[1, 3, 4, 5, 6, 7, 9]
[-1, 6, 17, 45, 55, 91, 200]
[10, 15, 25, 34, 76, 89, 96]
[10, 15, 25, 34, 76, 89, 96]
'''