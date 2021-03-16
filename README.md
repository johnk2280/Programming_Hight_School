# Высшая школа программирования Сергея Бобровского
##  Первый курс по алгоритмам/структурам данных (списки, стеки, очереди, ...)

В данном репозитории собраны решения задач курса.

### Связанный (связный) список

#### Задание.

>_Пункты, помеченные * реализуйте отдельно._

*1. Добавьте в класс LinkedList метод удаления одного узла по его значению
delete(val, all=False)
где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.*

*2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).*

*3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()*

*4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов).
find_all(val)*

*5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()*

*6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
insert(afterNode, newNode)
Если afterNode = None, добавьте новый элемент первым в списке.*

*7. Напишите проверочные тесты для каждого из предыдущих заданий.*

*8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.*

>_Рекомендации по тестированию._
>_Проверяйте случаи, когда список пустой, содержит много элементов и один элемент: как в таких ситуациях будет работать удаление одного и нескольких элементов, вставка, поиск. Особое внимание уделите корректности полей head и tail после всех этих операций._

### Введение в тестирование

#### Задание.

_1. Напишите функцию поиска подстроки в строке (на основе вашего решения выпускной задачи начального курса) и четыре вида тестов для неё._

