# You will be given a list of strings. You must sort it alphabetically 
# (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.


def two_sort(array):
    return "***".join(sorted(array)[0])



if __name__ == "__main__":
    L = ["black", "pink", "yellow", "red", "orange", "blue", "silver"]

    res = two_sort(L)
    print(res)