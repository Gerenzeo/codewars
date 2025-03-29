# Complete the function that accepts a string parameter,
# and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text: str):
    return " ".join(list(map(lambda s: s[::-1], text.split(" "))))

if __name__ == "__main__":
    S = "double  spaces"
    res = reverse_words(S)
    print(res)