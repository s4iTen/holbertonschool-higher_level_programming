#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    str_1 = roman_string
    R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    str_1 = str_1.upper()
    result = 0
    for i in range(len(str_1)):
        current_value = R[str_1[i]]
        if i+1 < len(str_1) and R[str_1[i]] < R[str_1[i+1]]:
            result -= current_value
        else:
            result += current_value
    return result
