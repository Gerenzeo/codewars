from typing import Union

def is_even(n: Union[int, float]) -> bool:
    """Checks if a number is even.

    Args:
        n (Union[int, float]): The number to be checked, which can be either an integer or a floating-point number.

    Raises:
        TypeError: If the input is not a numeric value (int or float).

    Returns:
        bool: True if the number is even, False otherwise.

    Example:
        >>> is_even(4)
        True

        >>> is_even(3)
        False

        >>> is_even(3.0)
        False

    """
    if not isinstance(n, (int, float)):
        raise TypeError("Please enter a correct numeric value!")

    return n % 2 == 0
