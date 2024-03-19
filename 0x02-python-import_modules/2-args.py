#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv_len = len(sys.argv) - 1
    if not argv_len == 1:
        if not argv_len == 0:
            argv_ = "arguments:"
        else:
            argv_ = "arguments."
    else:
        argv_ = "argument:"
    argv_output = "{0:d} {1}".format(argv_len, argv_)
    print(argv_output)
    if argv_len > 0:
        values = sys.argv[1:]
        for index, value in enumerate(values, start=1):
            value_ = "{0:d}: {1}".format(index, value)
            print(value_)
