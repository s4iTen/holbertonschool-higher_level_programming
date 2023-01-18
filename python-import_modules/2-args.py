#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    line_len = len(sys.argv)

    for i in range(line_len):
        if line_len == 1:
            print("{} arguments.".format(line_len - 1))
        elif line_len == 2:
            if i == 1:
                print("{} argument:".format(line_len - 1))
                print("{}: {}".format(i, sys.argv[i]))
        elif i == 0:
            print("{} arguments:".format(line_len - 1))
        else:
            print("{}: {}".format(i, sys.argv[i]))
