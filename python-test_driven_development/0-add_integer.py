#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add_integer(1, 2)
    >>> 3
    add_integer(100, -2)
    >>> 98
    add_integer(2)
    >>> 100
    add_integer(100.3, -2)
    >>> 98
    
    """
    if isinstance(a, (float, int)):
        if isinstance(b, (float, int)):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError('a must be an integer')
