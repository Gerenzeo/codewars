# You will be given a number and you will need to return it as a 
# string in Expanded Form. For example:

# 12 --> "10 + 2"
# 45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"



def expanded_form(num):
    ready = []
    for i, element in enumerate(str(num)[::-1]):
        if element == "0":
            continue

        print(i, element)
        ready.append(f"{element}{i * '0'}")
    return " + ".join(ready[::-1])



result = expanded_form(203)

print(result)


