#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    argv_len = len(sys.argv) - 1
    if not argv_len == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
        exit(1)
    argv_elem = sys.argv[1:]
    operators = "+-/*"
    operator = argv_elem[1]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /", end='\n')
        exit(1)
    a = int(argv_elem[0])
    b = int(argv_elem[2])
    op = [add, sub, mul, div]
    i = 0
    if operator == '+':
        i = 0
    if operator == '-':
        i = 1
    if operator == '*':
        i = 2
    if operator == '/':
        i = 3
    format_str = "{0:d} {1} {2:d} = {3:d}".format(a, operator, b, op[i](a, b))
    print(format_str, end='\n')
