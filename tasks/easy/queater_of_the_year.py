# Given a month as an integer from 1 to 12, 
# return to which quarter of the year it belongs as an integer number.

# For example: 
# month 2 (February), 
# is part of the first quarter; 
# month 6 (June), is part of the second quarter; 
# and month 11 (November), 
# is part of the fourth quarter.

# Constraint:
# 1 <= month <= 12


def quarter_of(month):
    if not 1 <= month <= 12:
        return 0
    
    data = {
        (1, 2, 3): 1,
        (4, 5, 6): 2,
        (7, 8, 9): 3,
        (10, 11, 12): 4
    }
    
    for key, value in data.items():
        if month in key:
            return value