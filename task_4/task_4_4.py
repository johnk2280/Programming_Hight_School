"""
Напишите функцию, которая получает на вход строку, состоящую из открывающих и закрывающих скобок
Например, "(()((())()))" или "(()()(()".
Используя только стек и оператор цикла, определите, сбалансированы ли скобки в этой строке.
Сбалансированной считается последовательность, в которой каждой открывающей обязательно соответствует закрывающая,
а каждой закрывающей -- открывающая скобки.
То есть последовательности "())(" , "))((" или "((())" будут несбалансированы.
"""


from task_4 import *


def check_balance(string):
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push('(')
        elif char == ')' and stack.peek() == '(':
            stack.pop()
        elif char == ')' and stack.size() == 0:
            return False

    return stack.size() == 0


