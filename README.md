# Высшая школа программирования Сергея Бобровского
##  Первый курс по алгоритмам/структурам данных (списки, стеки, очереди, ...)

В данном репозитории собраны решения задач курса.

### Связанный (связный) список

#### Задание.

>_Пункты, помеченные * реализуйте отдельно._

*1. Добавьте в класс **LinkedList** метод удаления одного узла по его значению
**delete(val, all=False)**
где флажок **all=False** по умолчанию -- удаляем только первый нашедшийся элемент.*

*2. Дополните этот метод удалением всех узлов по конкретному значению (флажок **all=True**).*

*3. Добавьте в класс **LinkedList** метод очистки всего содержимого (создание пустого списка) -- **clean()***

*4. Добавьте в класс **LinkedList** метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов).
**find_all(val)***

*5. Добавьте в класс **LinkedList** метод вычисления текущей длины списка -- **len()***

*6. Добавьте в класс **LinkedList** метод вставки узла newNode после заданного узла **afterNode** (из списка)
**insert(afterNode, newNode)**
Если **afterNode = None**, добавьте новый элемент первым в списке.*

*7. Напишите проверочные тесты для каждого из предыдущих заданий.*

*8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.*

>_Рекомендации по тестированию._
>_Проверяйте случаи, когда список пустой, содержит много элементов и один элемент: как в таких ситуациях будет работать удаление одного и нескольких элементов, вставка, поиск. Особое внимание уделите корректности полей **head** и **tail** после всех этих операций._

### Введение в тестирование

#### Задание.

_1. Напишите функцию поиска подстроки в строке (на основе вашего решения выпускной задачи начального курса) и четыре вида тестов для неё._

### Двунаправленный связный (связанный) список.

#### Задания.

_1. Добавьте в класс **LinkedList2** метод поиска первого узла по его значению.
**find(val)**_

_2. Добавьте в класс **LinkedList2** метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
**find_all(val)**_

_3. Добавьте в класс **LinkedList2** метод удаления одного узла по его значению.
**delete(val, all=False)**
где флажок **all=False** по умолчанию -- удаляем только первый нашедшийся элемент._

_4. Дополните этот метод удалением всех узлов по конкретному значению (флажок **all=True**)._

_5. Добавьте в класс **LinkedList2** метод вставки узла после заданного узла.
**insert(afterNode, newNode)**
Если **afterNode = None** и список пустой, добавьте новый элемент первым в списке.
Если **afterNode = None** и список непустой, добавьте новый элемент последним в списке._

_6. Добавьте в класс **LinkedList2** метод вставки узла самым первым элементом.
**add_in_head(newNode)**_

_7. Добавьте в класс **LinkedList2** метод очистки всего содержимого (создание пустого списка) -- **clean()**_

_8. Добавьте в класс **LinkedList2** метод вычисления текущей длины списка -- **len()**_

>_Напишите проверочные тесты для каждого из предыдущих заданий._

### Динамические массивы.

#### Задание.

_1. Добавьте метод **insert(i, itm)**, который вставляет в **i-ю** позицию объект **itm**, сдвигая вперёд все последующие элементы. Учтите, что новая длина массива может превысить размер буфера._

_2. Добавьте метод **delete(i)**, который удаляет объект из **i-й** позиции, при необходимости сжимая буфер. В обоих случаях, если индекс **i** лежит вне допустимых границ, генерируйте исключение. Важно, единственное исключение: для метода **insert()** параметр **i** может принимать значение, равное длине рабочего массива count, в таком случае добавление происходит в его хвост._

_3. Оцените меры сложности для этих двух методов._

>_Напишите тесты, проверяющие работу методов **insert()** и **delete()**:_
>_- вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);_
>_- вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);_
>_- попытка вставки элемента в недопустимую позицию;_
>_- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);_
>_- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);_
>_- попытка удаления элемента в недопустимой позиции._

