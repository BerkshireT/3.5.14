# **********************************************************
#
#    filename:  evaluator.py
#
#    description: Evaluates the postfix operation
#
#    author: Tyler Berkshire
#    login id:  none
#
#    class:  CPS 452
#    instructor:  Perugini
#    assignment:  Homework #1
#
#    assigned:  Aug 21, 2019
#    due:  Aug 26, 2019
#
# **********************************************************

import sys
import op_help as op


def evaluate_postfix(exp):
    if len(exp) is 0:
        return ""

    inputArray = exp.split()
    stk = []
    for x in inputArray:
        try:
            if x is "+":
                stk.append(op.my_add(int(stk.pop()), int(stk.pop())))
            elif x is "-":
                stk.append(op.my_sub(int(stk.pop()), int(stk.pop())))
            elif x is "*":
                stk.append(op.my_mult(int(stk.pop()), int(stk.pop())))
            elif x is "/":
                stk.append(op.my_div(int(stk.pop()), int(stk.pop())))
            else:
                stk.append(x)
        except (IndexError, ValueError):
            return "Invalid Sentence"

    final = stk.pop()
    if final is "+" or final is "-" or final is "*" or final is "/":
        return "Invalid Sentence"
    else:
        return final
