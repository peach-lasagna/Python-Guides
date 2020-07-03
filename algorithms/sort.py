def bubble_sort(array):
    """Этот простой алгоритм выполняет итерации по списку,
    сравнивая элементы попарно и меняя их местами,
    пока более крупные элементы не «всплывут» в начало списка,
    а более мелкие не останутся на «дне».

    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True


def selection_sort(array):
    """Этот алгоритм сегментирует список на две части:
    отсортированную и неотсортированную.
    Наименьший элемент удаляется из второго списка и добавляется в первый.

    """
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(array)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        array[i], array[lowest_value_index] = array[lowest_value_index], array[i]


def insertion_sort(array):
    """Как и сортировка выборкой, этот алгоритм сегментирует список на две части:
    отсортированную и неотсортированную.
    Алгоритм перебирает второй сегмент и
    вставляет текущий элемент в правильную позицию первого сегмента.

    """
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(array)):
        item_to_insert = array[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        # Вставляем элемент
        array[j + 1] = item_to_insert


def heap_sort(array):
    """Сначала преобразуем список в Max Heap — бинарное дерево,
    где самый большой элемент является вершиной дерева.
    Затем помещаем этот элемент в конец списка. 
    После перестраиваем Max Heap и снова помещаем новый наибольший элемент
        уже перед последним элементом в списке.
    Этот процесс построения кучи повторяется, пока все вершины дерева не будут удалены.

    """
    def heapify(array, heap_size, root_index):
            # Индекс наибольшего элемента считаем корневым индексом
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and array[left_child] > array[largest]:
            largest = left_child

        # То же самое для правого потомка корня
        if right_child < heap_size and array[right_child] > array[largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            # Heapify the new root element to ensure it's the largest
            heapify(array, heap_size, largest)

    n = len(array)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


def merge_sort(array):
    """Этот алгоритм относится к алгоритмам «разделяй и властвуй».
    Он разбивает список на две части, каждую из них он разбивает ещё на две и т. д.
    Список разбивается пополам, пока не останутся единичные элементы.

    Соседние элементы становятся отсортированными парами.
    Затем эти пары объединяются и сортируются с другими парами.
    Этот процесс продолжается до тех пор, пока не отсортируются все элементы.

    """
    # Возвращаем список, если он состоит из одного элемента
    if len(array) <= 1:
        return array

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(array) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])

    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        # Длина списков часто используется, поэтому создадим переменные для удобства
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # Сравниваем первые элементы в начале каждого списка
                # Если первый элемент левого подсписка меньше, добавляем его
                # в отсортированный массив
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                # Если первый элемент правого подсписка меньше, добавляем его
                # в отсортированный массив
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            # Если достигнут конец правого списка, элементы левого списка
            # добавляем в отсортированный массив
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


def quick_sort(array):
    """Этот алгоритм также относится к алгоритмам «разделяй и властвуй».
    Его используют чаще других алгоритмов, описанных в этой статье.
    При правильной конфигурации он чрезвычайно эффективен и не требует дополнительной памяти,
        в отличие от сортировки слиянием.
    Массив разделяется на две части по разные стороны от опорного элемента.
    В процессе сортировки элементы меньше опорного помещаются перед ним,
        а равные или большие —позади.

    """
    def partition(array, low, high):
            # Выбираем средний элемент в качестве опорного
            # Также возможен выбор первого, последнего
            # или произвольного элементов в качестве опорного
        pivot = array[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while array[i] < pivot:
                i += 1

            j -= 1
            while array[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            array[i], array[j] = array[j], array[i]

    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(array, 0, len(array) - 1)
