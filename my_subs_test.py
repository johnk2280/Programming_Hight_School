import unittest
import my_subs
import random


class FindSubs(unittest.TestCase):

    def test_find_subs_returns_index(self):
        self.assertEqual(my_subs.find_subs('туча мглою', 'а м'), 'туча мглою'.find('а м'))
        self.assertEqual(my_subs.find_subs('а м', 'туча мглою'), 'а м'.find('туча мглою'))
        self.assertEqual(my_subs.find_subs('туча_мглою_небо_кроет', 'а м'), 'туча_мглою_небо_кроет'.find('а м'))
        self.assertEqual(my_subs.find_subs('джлыражптавжлиьт', 'а м'), 'джлыражптавжлиьт'.find('а м'))
        self.assertEqual(my_subs.find_subs(r'94793fjd098[eenco', '098'), r'94793fjd098[eenco'.find('098'))
        self.assertEqual(my_subs.find_subs('Hello world!', 'd!'), 'Hello world!'.find('d!'))
        self.assertEqual(my_subs.find_subs('Мой дядя самых честных правил,\nКогда не в шутку занемог,\nОн уважать себя заставил\t\tИ лучше выдумать не мог.\nЕго пример другим наука;\n', 'шут'),
                         'Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог. Его пример другим наука;'.find('шут'))

    def test_find_subs_random_result(self):
        s = ''.join([chr(random.randint(40, 128)) for _ in range(1000)])
        subs = ''.join([chr(random.randint(40, 128)) for _ in range(10)])
        spam = (s[:500] + subs + s[500:])
        self.assertEqual(my_subs.find_subs(s, subs), s.find(subs))
        self.assertEqual(my_subs.find_subs(spam, subs), spam.find(subs))

