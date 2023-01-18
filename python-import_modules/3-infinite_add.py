#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 0

    for i in sys.argv[1:]:
        j += (int(i))
    print(j)
