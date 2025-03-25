def to_alternating_case(string: str):

    if not isinstance(string, str):
        raise TypeError("This is not a string")

    new_S = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                new_S += char.upper()
            else:
                new_S += char.lower()
        else:
            new_S += char
    return new_S