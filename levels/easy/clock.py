def past(h: int, m: int, s: int) -> int:
    """Converts the given hours, minutes, and seconds into milliseconds.

    Args:
        h (int): The number of hours.
        m (int): The number of minutes.
        s (int): The number of seconds.

    Raises:
        TypeError: If any of the arguments is not an integer.

    Returns:
        int: The total time in milliseconds.

    Example:
        >>> past(1, 1, 1)
        3661000
    """
    
    if not isinstance(h, int) or not isinstance(m, int) or not isinstance(s, int):
        raise TypeError("Type should be int")

    ms = 0
    
    if h >= 0:
        m += h * 60
        h = 0
    if m >= 0:
        s += m * 60
        m = 0
    if s >= 0:
        ms += s * 1000

    return ms
