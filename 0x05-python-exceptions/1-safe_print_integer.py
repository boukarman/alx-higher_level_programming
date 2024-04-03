#!/usr/bin/python3
def safe_print_int(value):
    try:
        if not isinstance(value, int):
            raise Exception
        print("{:d}".format(value))
    except Exception:
        return (False)
    else:
        return (True)
