## Comparison sorts: Insertion sort, selection sort, merge sort, heapsort, quicksort
## Direct access sorts: Counting sort, radix sort, bucket sort


###################################################
##Selection sort
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


