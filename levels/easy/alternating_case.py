def to_alternating_case(string: str):
    """Converts each letter in the string to the opposite case.

    Args:
        string (str): The input string to be modified.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        str: A new string where uppercase letters are converted to lowercase and vice versa.
    """
    
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
