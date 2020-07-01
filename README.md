# quickselect
returns the kth largest element in an unsorted array using the quickselect algorithm in O(n) time

pseudo code as follows

quickselect (array A, length n, index)
- if n == 1, return
- randomly choose a pivot, p
- partition A around p such that everything to the left of p is smaller than p and everything right of p is larger than p
- if index of p = index, return the value of the pivot
- if index of p < index, search the right half
- else if index of p > index, search the left half
