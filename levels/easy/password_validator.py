
def password(st: str):
    check_upper = list(zip(map(lambda x: x.isupper(), st)))

    print(check_upper)



if __name__ == "__main__":
    test_password = "Abcd1234" # True

    result = password(test_password)
    print(result)