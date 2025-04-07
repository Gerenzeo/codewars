# Your task is to make a function that can take any non-negative integer as an argument
# and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

# Examples:

# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321


def descending_order(num):
    if not len(str(num)):
        return 0
    
    num = [int(el) for el in str(num)]

    for i in range(len(num)-1):
        for j in range(len(num) - i - 1):
            if num[j] < num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

    return int("".join(str(el) for el in num))