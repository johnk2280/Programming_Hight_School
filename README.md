
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

>_Проверяйте случаи, когда список пустой, содержит много элементов и один элемент: как в таких ситуациях будет работать удаление одного и нескольких элементов, вставка, поиск. Особое внимание уделите корректности полей head и tail после всех этих операций._

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
>
>_- вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);_
>
>_- вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);_
>
>_- попытка вставки элемента в недопустимую позицию;_
>
>_- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);_
>
>_- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);_
>
>_- попытка удаления элемента в недопустимой позиции._

### Стек.

#### Задание.

_1. Подберите подходящую динамическую структуру данных для хранения стека. Реализуйте методы **size(), pop(), push() и peek()**.
Добавьте тесты для каждого из этих четырёх методов._

_2. Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой_

_3. Оцените меру сложности для операций **pop** и **push**._

_4. Напишите функцию, которая получает на вход строку, состоящую из открывающих и закрывающих скобок (например,**"(()((())()))" или "(()()(()")** и, используя только стек и оператор цикла, определите, сбалансированы ли скобки в этой строке. Сбалансированной считается последовательность, в которой каждой открывающей обязательно соответствует закрывающая, а каждой закрывающей -- открывающая скобки, то есть последовательности **"())(" , "))((" или "((())"** будут несбалансированы._

_6*. (необязательное). бонус +300 золотых
Постфиксная запись выражения -- это запись, в которой порядок вычислений определяется не скобками и приоритетами, а только позицией элемента в выражении. Например, в выражениях разрешено использовать целые числа и операции + и * . Тогда выражение:_

_(1 + 2) * 3_

_запишется как:_

_1 2 + 3 * (верхушка стека слева)_

_Такой стек обрабатывается следующим образом: берём с верхушки объект, если это число, сохраняем во втором стеке, а если операция, выполняем её над двумя верхними элементами второго стека и возвращаем её обратно во второй стек._

_В нашем случае:_

_S1: 1 2 + 3 *_
_S2:_

_S1: 2 + 3 *_
_S2: 1_

_S1: + 3 *
S2: 2 1
Берём операцию + и применяем её к содержимому S2:_

_S1: 3 *
S2: 3_

_S1: *
S2: 3 3_

_S1:
S2: 9
Можно ещё добавить операцию = , которая выдаёт содержимое второго стека как результат. Напишите функцию, которая с помощью двух стеков реализует вычисление подобных постфиксных выражений._

_Рассчитайте с её помощью например такое выражение:_

_8 2 + 5 * 9 + =_

### Очереди

#### Задания.

_1. В классе Queue нам понадобятся три метода: **size()** (количество элементов в очереди), ***enqueue(item)** -- добавить элемент в хвост очереди, и **dequeue()**, которая возвращает элемент из головы очереди, удаляя его._

_2. Оцените меру сложности для операций **enqueue()** и **dequeue()**._

_3. Напишите функцию, которая "вращает" очередь по кругу на **N** элементов._

_4. Попробуйте реализовать очередь с помощью двух стеков._


### Двусторонняя очередь (deque)

#### Задания.

_1. Почему и как будет различаться мера сложности для **addHead/removeHead** и **addTail/removeTail**?_

_2. Напишите функцию, которая с помощью deque проверяет, является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево)._

_3. Добавьте для каждого из четырёх вышеупомянутых методов тесты: проверяйте изменившуюся длину очереди и наличие или отсутствие в ней добавляемого/удаляемого элемента._


### Упорядоченный список

#### Задания:

_1. Дополнительную опцию asc в конструкторе **OrderedList**, которая указывает, по возрастанию **(True)** или по убыванию **(False)** должны храниться элементы в массиве. Эту опцию сделайте приватной -- изменять её можно только в конструкторе и методе очистки **clean()**._

_2. Метод сравнения двух значений **compare()**. В общем случае, мы можем хранить в нашем списке произвольные объекты (например, экземпляры класса Cat), и способ, которым мы желаем их сравнивать, потенциально может быть самым произвольным. Пока сделайте базовый вариант этого метода, который сравнивает числовые значения._

_3. Добавление нового элемента по значению **add()** с единственным параметром -- новым добавляемым значением (новый узел для него создавайте внутри метода add). Элемент должен вставиться автоматически между элементами с двумя подходящими значениями (либо в начало или конец списка) с учётом его значения и признака упорядоченности. Используйте для этого метод сравнения значений из предыдущего пункта._

_4. Создайте **OrderedStringList** -- наследник текущего класса, который будет упорядоченно хранить строки. Для этого переопределите в нём метод сравнения значений -- он должен сравнивать строки, очищенные от начальных и конечных пробелов._

_5. Переделайте функцию поиска элемента по значению с учётом признака упорядоченности и возможности раннего прерывания поиска, если найден заведомо больший или меньший элемент, нежели искомый. Оцените сложность операции поиска, изменилась ли она?_

_6. Добавьте тесты для добавления, удаления и поиска элемента по его значению -- каждый случай с учётом признака упорядоченности._

### Хэширование.
#### Задания:
_В классе хэш-таблицы потребуются два параметра: размер хэш-таблицы (желательно простое число, для экспериментов можно например брать 17 или 19), и длину шага (количество слотов) для поиска следующего свободного слота (например, 3)._

_В этом классе требуется реализовать четыре метода:_

_- хэш-функцию **hash_fun(value)**, которая по входному значению вычисляет индекс слота;_

_- функцию поиска слота **seek_slot(value)**, которая по входному значению сперва рассчитывает индекс хэш-функцией, а затем отыскивает подходящий слот для него с учётом коллизий, или возвращает None, если это не удалось;_

_- **put(value)**, который помещает значение value в слот, вычисляемый с помощью функции поиска;_

_- **find(value)**, который проверяет, имеется ли в слотах указанное значение, и возвращает либо слот, либо None._


>_Напишите тесты, которые проверяют работу этих четырёх методов._

### Ассоциативный массив.
#### Задания:
_Реализуйте три метода:_

_- **put(key, value)** - сохранение внутри класса ассоциативного массива пары ключ-значение по описанной выше схеме;_

_- **is_key(key)** - проверка, имеется ли в слотах такой ключ;_

_- **get(key)** - поиск и извлечение значения по ключу, или None, если ключ не найден._

>_Сделайте тесты, проверяющие, как работают put(), is_key() и get():_
>- _добавление значения по новому ключу и добавление значения по уже существующему ключу с проверками что записалось,_ 
>- _проверка присутствующего и отсутствующего ключей, извлечение значения по существующему и отсутствующему ключу._

### Множества.
#### Задания:

_Реализуйте следующие типичные для множества методы:_

_- **remove(значение)** -- удаление элемента из множества;_

_- **intersection()**, в качестве параметра выступает другое множество, а возвращается пересечение этих множеств (множество, в котором есть только те элементы, которые имеются в каждом из множеств);_

_- **union()**, в качестве параметра выступает другое множество, а возвращается объединение этих множеств (множество, в котором есть все элементы из каждого множества);_

_- **difference()**, в качестве параметра выступает другое множество, а возвращается подмножество текущего множества из таких элементов, которые не входят в множество-параметр;_

_- **issubset()**, в качестве параметра выступает другое множество, и проверяется, входят ли все его элементы в текущее множество (будет ли множество-параметр подмножеством текущего множества)._

>_Добавьте тесты, которые проверяют:_
>
>_- возможность добавления отсутствующего элемента и невозможность добавления присутствующего в множестве элемента с помощью put();_
>
>_- удаление элемента с помощью remove();_
>
>_- пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества;_
>
>_- объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество;_
>
>_- разница difference(), чтобы в результате получались как пустое, так и непустое множества;_
>
>_- подмножество issubset() -- рассмотрите три случая (все элементы параметра входят в текущее множество, все элементы текущего множества входят в параметр, не все элементы параметра входят в текущее множество);_
>
>_- быстродействие (операции над множествами из десятков тысяч элементов укладываются в пару секунд)._

### Фильтр Блюма.
#### Задания:
_Реализуйте классический фильтр Блюма для строк на основе битового (не булевского) массива, выясните, имеется ли в выбранном языке программирования подходящий тип данных._

_Для тестового примера можно использовать и обычное 32-разрядное целое число, то есть размер фильтра m=32. Примем количество значений для фильтра n=10, и получим примерное количество хэш-функций k=2._

_Реализуйте две хэш-функции для строк по вышеописанной схеме. В качестве результата первой итерации используйте ноль. В качестве случайных чисел для первой функции используйте 17, для второй 223. В качестве 10 тестовых строк используйте строки "0123456789" "1234567890" ... "8901234567" "9012345678"_

