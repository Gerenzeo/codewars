def password(st: str):
    
    if not isinstance(st, str):
        raise TypeError("Should be a str")

    check_length = len(st) >= 8
    check_upper = True if True in list(map(lambda c: c.isupper(), st)) else False
    check_lower = True if True in list(map(lambda c: c.islower(), st)) else False
    check_numeric = True if True in list(map(lambda c: c.isnumeric(), st)) else False

    return True if check_length and check_upper and check_lower and check_numeric else False