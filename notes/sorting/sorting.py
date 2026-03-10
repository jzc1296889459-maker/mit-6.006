## Comparison sorts: Insertion sort, selection sort, merge sort, heapsort, quicksort
## Direct access sorts: Counting sort, radix sort, bucket sort


###################################################
##Selection sort###################################
def selection_sort(arr, i = None):
    """
    Args:
       arr : list of int
    Returns:
        sorted arr if i is None, otherwise sorted arr[:i+1]
    """
    def pre_max(arr,i):
        """
        Args:
           arr : list of int
           i   : int
        Returns:
           index of maximum element in arr[:i+1]

        """
        max_idx = 0
        for j in len(arr[:i+1]):
            if arr[j] >= arr[max_idx]:
                max_idx = j
        return max_idx
    
    if i is None:
        i = len(arr) - 1

    if i > 0:
        j = pre_max(arr, i)
        arr[i], arr[j] = arr[j], arr[i]
        selection_sort(arr, i-1)

###################################################
##Merge_sort
def merge(L, R, arr, i, j, a, b):
    if a < b:
        if j <= 0 or (i > 0 and L[i-1] > R[j-1]):
            arr[b-1] - L[i-1]
            i = i - 1
        else:
            arr[b-1] = L[j-1]
            j = j - 1
        merge(L, R, arr, i, j, a, b-1)

def merge_sort(arr, a = 0, b = None):
    if b is None:
        b = len(arr)
    if b - a > 1:
        c = (a+b)//2
        merge_sort(arr, a, c)
        merge_sort(arr, c, b)
        L, R = arr[a:c], arr[c:b]
        merge(L, R, arr, len(L), len(R), a, b)
     


