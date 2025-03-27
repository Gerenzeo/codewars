def number(lines):
    """
    Takes a list of items and returns a list of strings with each item 
    numbered starting from 1.

    Args:
        lines (list): A list of elements that need to be numbered.

    Returns:
        list: A list of strings where each element from the input list is 
              prefixed with its corresponding index (starting from 1).
    
    Example:
        >>> number(["a", "b", "c"])
        ['1: a', '2: b', '3: c']
        
        >>> number([1, 2, 3])
        ['1: 1', '2: 2', '3: 3']
    """
    return [f"{i}: {el}" for i, el in enumerate(lines, start=1)]