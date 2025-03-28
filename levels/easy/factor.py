def check_for_factor(base, factor):
    if not isinstance(base, int) or not isinstance(factor, int):
        raise TypeError("Should be int")
    return True if base % factor == 0 else False