from mergesort import mergeSort
import random

def main():
    arr = []
    num = 0
    with open('QuickSort_List.txt', 'r') as file:
        for line in file:
            num += 1
            arr.append(int(line))
    print(num)

    # arr = [20, 60, 30, 70, 40, 50, 10, 30, 50, 70, 5]
    # print(arr)
    # mergeSort(arr)

    # arr = [0,1,2,3,4,5]

    # temp = arr
    index = 6969
    result = quickSelect(arr, 0, len(arr) - 1, index)
    # print(arr)
    print(result)

    # mergeSort(temp)
    # # print(temp)
    # print(temp[index])


# Return the value of ith largest value inside an array where 1 < i < array length
def quickSelect(arr, start, end, i):
    if start >= end:
        return arr[i - 1]
    
    # randomly choose a pivot
    pivot_index = choosePivot(arr, start, end)

    partition_index = partition(arr, start, end, pivot_index)

    if partition_index == i - 1:
        return arr[partition_index] 
    if partition_index > i - 1:
        return quickSelect(arr, start, partition_index - 1, i)
    if partition_index < i - 1:
        return quickSelect(arr, partition_index + 1, end, i) 
    else:
        raise IndexError()


def choosePivot(arr, start, end):
    # randomly choose a pivot
    pivot_index = random.randint(start, end)
    return pivot_index


def partition(arr, start, end, pivot_index):

    pivot = arr[pivot_index]

    # swap the pivot element with the first element of the array
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]

    i = start + 1

    # place everything smaller or equal to the pivot on the left
    for j in range(start + 1, end + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # swap the pivot into its rightful position
    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    return i - 1
    

if __name__ == "__main__":
    main()