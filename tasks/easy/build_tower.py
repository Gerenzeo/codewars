# Build a pyramid-shaped tower, as an array/list of strings,
# given a positive integer number of floors. A tower block is represented with "*" 
# character.

def tower_builder(n_floors):
    tmp_l = []
    for i in range(1, n_floors * 2, 2):
        tmp_l.append("*" * i)  

    width = len(tmp_l[-1]) 
    new_L = [row.center(width) for row in tmp_l]
    return new_L 