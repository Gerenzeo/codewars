def remove_exclamation_marks(s: str) -> str:
    """Removes all exclamation marks from the given string.

    Args:
        s (str): The input string from which exclamation marks will be removed.

    Raises:
        TypeError: If the input string does not contain any exclamation marks.

    Returns:
        str: A new string with all exclamation marks removed.

    Example:
        >>> remove_exclamation_marks("Hello World!")
        'Hello World'
        
        >>> remove_exclamation_marks("Python!!!")
        'Python'
    """
    if not isinstance(s, str):
        raise TypeError("Type should be str")
    
    if not "!" in s:
        raise ValueError("! is required for result!")
    
    return s.replace("!", "")
