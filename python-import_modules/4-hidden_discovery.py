#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4

    modules = dir(hidden_4)

    for name in modules:
        if name[0:2] != "__":
            print(name)
