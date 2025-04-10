# Character recognition software is widely used to digitise printed texts.
# Thus the texts can be edited, searched and stored on a computer.

# When documents (especially pretty old ones written 
# with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. 
# You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1

def correct(s: str):
    if "1" in s:
        s = s.replace("1", "I")
    if "0" in s:
        s = s.replace("0", "O")
    if "5" in s:
        s = s.replace("5", "S")
    
    return s
    

s = "PAR1S"
print(correct(s))