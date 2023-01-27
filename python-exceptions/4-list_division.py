#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret = []
    if (len(my_list_1) > len(my_list_1)):
        lenList = len(my_list_1)
    else:
        lenList = len(my_list_2)
    for i in range(lenList):
        try:
            j = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            j = 0
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except TypeError:
            print("wrong type")
            j = 0
        finally:
            ret.append(j)
    return ret
