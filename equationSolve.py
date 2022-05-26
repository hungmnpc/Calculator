from z3 import *


# giai phuong trinh bac 1,2,3,4
def equationSolver(args_list):
    x = Real('x')
    s = Solver()
    result = []

    number_of_args = len(args_list)

    if (number_of_args == 2):
        s.add(args_list[0] * x + args_list[1] == 0)
    elif (number_of_args == 3):
        s.add(args_list[0] * (x ** 2) + args_list[1] * x + args_list[2] == 0)
    elif (number_of_args == 4):
        s.add(args_list[0] * (x ** 3) + args_list[1] *
              (x ** 2) + args_list[2] * x + args_list[3] == 0)
    elif (number_of_args == 5):
        s.add(args_list[0] * (x ** 4) + args_list[1] * (x ** 3) +
              args_list[2] * (x ** 2) + args_list[3] * x + args_list[4] == 0)

    res = s.check()
    while (res == sat):
        m = s.model()
        if (str(m[x]) == "None"):
            result.append("Infinite solution")
        else:
            result.append(str(m[x]))
        block = []
        for var in m:
            block.append(var() != m[var])
        s.add(Or(block))
        res = s.check()
    return result

