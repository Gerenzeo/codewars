
# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345

# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    if not len(arr):
        return []
    
    min_value = arr[0]

    for element in arr:
        if min_value > element:
            min_value = element
    
    return min_value



print(find_smallest_int([]))


