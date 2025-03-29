# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!


def remove_every_other(my_list: list) -> list:
    return list(el for i, el in enumerate(my_list) if i % 2 == 0)

if __name__ == "__main__":
    L = ["Keep", "Remove", "Keep", "Remove", "Keep", ...]
    print(remove_every_other(L))