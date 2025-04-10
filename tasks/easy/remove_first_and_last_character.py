# It's pretty straightforward. Your goal is to create a function that removes the first and last 
# characters of a string. You're given one parameter, the original string. 
# You don't have to worry about strings with less than two characters.

def remove_char(s):
    return s[slice(1, -1)]



if __name__ == "__main__":
    result = remove_char("")
    print(result)