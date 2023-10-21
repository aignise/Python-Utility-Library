def linear_search(arr, x):
    """
    Search for a value `x` in a list using linear search.

    Args:
    - arr (list): List of elements.
    - x (any): Value to search for.

    Returns:
    - int: Index of the value if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    """
    Search for a value `x` in a sorted list using binary search.

    Args:
    - arr (list): Sorted list of elements.
    - x (any): Value to search for.

    Returns:
    - int: Index of the value if found, otherwise -1.
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# ... other searching algorithms can be added.
