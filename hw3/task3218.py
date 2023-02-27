#Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

def nearest_value(items, value):
    found = items[0]
    for item in items:
        if abs(item - value) < abs(found - value):
            found = item
    return found