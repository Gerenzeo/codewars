# Task

# Create a method to see whether the string is ALL CAPS.
# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True



def is_uppercase(input: str):
    
    for char in input:
        if char.islower():
            return False
        
    return True

if __name__ == "__main__":
    S = "SSS I AM SONALD"

    res = is_uppercase(S)
    print(res)
    

