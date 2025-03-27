def digitize(n: int):
    """
    Converts a given number into a list of its digits in reverse order.

    This function takes an integer `n`, converts it into a string, then 
    converts each character of the string back into an integer. The resulting 
    list of digits is then reversed before being returned. If the input 
    is not an integer, a TypeError is raised.

    Args:
        n (int): The number to be converted into a list of digits.

    Returns:
        list: A list of digits (in reverse order) from the input number.
    
    Raises:
        TypeError: If the input is not an integer.
    
    Example:
        >>> digitize(123)
        [3, 2, 1]
        
        >>> digitize(4567)
        [7, 6, 5, 4]
    """

    if not isinstance(n, int):
        raise TypeError("Input should be an integer")
    
    if n < 0:
        n = abs(n)

    return list(map(lambda x: int(x), list(str(n))))[::-1]
