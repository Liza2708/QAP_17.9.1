import random

# быстрая сортировка
def quick_sort(array, first, last):
    if first >= last:
        return

    i, j = first, last
    pivot = array[random.randint(first, last)]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort(array, first, j)
    quick_sort(array, i, last)
    return array


# Двоичный поиск
def binary_search(array, element, first, last):
    if first > last:  # если левая граница превысила правую,
        return None  # значит элемент отсутствует


    middle = (last + first) // 2  # находимо середину
    if array[middle] < element and array[middle+1]>=element:  # если элемент соответствует условию,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, first, middle - 1)
    else:  # иначе в правой
        if middle+1==len(array)-1: # проверка на последний элемент
            return None
        else:
            return binary_search(array, element, middle + 1, last)


# обработка исключения на тип данных при вводе
try:
    list_of_numbers = list(map(int, input("Введите числа через пробел: ").split()))
    digit = int(input("Введите число для поиска: "))
except ValueError:
    print("Введены некорректные значения для списка (должны быть числа через пробел) или числа для поиска")
else:
    print(f"1) Введена последовательность чисел: {list_of_numbers}")
    print(f"Введено число для поиска: {digit}")

    sort_list_of_numbers = quick_sort(list_of_numbers,0,len(list_of_numbers)-1)
    print(f"2) Отсортированный список: {sort_list_of_numbers}")

    index = binary_search(sort_list_of_numbers, digit,0,len(sort_list_of_numbers)-1)

    if index is not None:
        print(f"3) Номер искомой позиции: {index}")
    else:
        print(f"3) Индекс элемента не найден")






