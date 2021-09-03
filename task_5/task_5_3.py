"""Напишите функцию, которая "вращает" очередь по кругу на N элементов."""


def scroll(q, n):
    for i in range(n):
        q.enqueue(q.dequeue())
    return q


