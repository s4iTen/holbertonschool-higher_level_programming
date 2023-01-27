#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i, element in enumerate(my_list):
        if i == x:
            break
        try:
            print("{:d}".format(element), end='')
            count += 1
        except IndexError as e:
            print(e)
            continue
    print()
    return count