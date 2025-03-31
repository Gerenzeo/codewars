# Task

# Given an array of integers, remove the smallest value. 
# Do not mutate the original array/list. 
# If there are multiple elements with the same value, remove the one with the lowest index. 
# If you get an empty array/list, return an empty array/list.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]


def remove_smallest(numbers: list) -> list:
    if not len(numbers):
        return []
    
    min_value = min(numbers)
    new_numbers = [number for number in numbers if number != min_value or (number == min_value and (min_value := None))]
    return new_numbers


    

    
    

print(remove_smallest([2, 2, 1, 2, 1]))