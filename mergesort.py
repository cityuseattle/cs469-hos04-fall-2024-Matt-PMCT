import math

def merge_sort(arr):
    # Base case for recursion
    if len(arr) < 2:
        return arr
    
    # Find the middle index of the array
    middle = math.ceil(len(arr) / 2)
    
    # Split the array into two halves
    # Copy the data to temporary arrays: left and right
    left, right = arr[:middle], arr[middle:]
    
    # Recursively sort the left and right halves
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    '''
    Merge the input arrays into one sorted array
    '''
    result = []
    while left and right:
        # Compare the first elements from two temporary arrays
        # Remove the smaller element from the original temporary array
        # Add the smaller element to the result array
        elem = left.pop(0) if left[0] <= right[0] else right.pop(0)
        result.append(elem)
    
    # In case right is empty and left still has elements
    while left:
        result.append(left.pop(0))
    # In case left is empty and right still has elements
    while right:
        result.append(right.pop(0))
        
    return result

# Test case 1 
arr1 = [5, 6, 1, 5, 6, 2, 3 , 9, 10, 55, 14, 62, 859]
print(merge_sort(arr1))

# Test case 2
import random
def rand_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    rd_list = []
    for i in range(length):
        rd_list.append(random.randint(start, stop))
    return rd_list

arr2 = rand_int_list(1, 1000, 100)
print(merge_sort(arr2))