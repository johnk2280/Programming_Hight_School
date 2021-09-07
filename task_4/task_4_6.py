"""
Напишите функцию для расчета постфиксной записи
с использованием 2-х стеков.
"""


from task_4 import *


def get_result(polish_notation):
    stack1 = Stack()
    stack2 = Stack()
    for el in polish_notation.strip().split()[-1:: -1]:
        stack1.push(el)

    for i in range(stack1.size()):
        egg = stack1.pop()
        if egg.isdigit():
            stack2.push(int(egg))
        elif egg == '+':
            stack2.push(stack2.pop() + stack2.pop())
        elif egg == '*':
            stack2.push(stack2.pop() * stack2.pop())
        elif egg == '-':
            stack2.push(-stack2.pop() + stack2.pop())
        elif egg == '=':
            return stack2.pop()
        else:
            raise ValueError('Invalid value in notation')

    return stack2.pop() if stack2.size() == 1 else f'Invalid notation'

