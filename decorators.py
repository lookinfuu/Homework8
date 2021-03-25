import time


def time_decorator(f):

    def my_func():
        ts = time.time()
        f()
        fin_time = time.time() - ts
        print(f'На выполнение функции ушло: {fin_time:.4f} сек.')
    return my_func


def count_call(f):
    
    def inn(*args):
        inn.count += 1
        return f(*args)
    inn.count = 0
    return inn


@count_call
def sym_del(text_list, a, i):
    i1 = text_list.index(i)
    while a != 1:
        i2 = text_list.index(i,i1 + 1,len(text_list))
        text_list.pop(i2)
        i1 = i2 - 1
        a -= 1
    return text_list


@time_decorator
def list_del():
    text_list = list(input('Введите Ваш список значений:'))
    print(f'Список до обработки: {text_list}')
    for i in text_list:
        a = text_list.count(i)
        if a > 1:
            text_list = sym_del(text_list, a, i)
        if i == text_list[-1]:
            print(f'Список после обработки: {text_list}')

print('Программа по удалению элемета в списке, если такой встречался ранее.')
list_del()
print(f'''Количество вызовов функции для удаления элементов: {sym_del.count}''')