#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    modules = dir(hidden_4)
    for mod in modules:
        start = mod[:2]
        if start != '__':
            print(mod)
