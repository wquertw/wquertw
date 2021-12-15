
# ## Реализация функций

import timeit
import os.path


def read_file(name):
    with open(name, "r") as f:
        text = f.read()
        nums = text.split()
    return list(map(int, nums))

def maximum(lst):
    res = lst[0]
    for i in lst[1:]:
        if i > res:
            res = i
    return res
            
def minimum(lst):
    res = lst[0]
    for i in lst[1:]:
        if i < res:
            res = i 
    return res

# В Python ариметические операции реализованы при помощи длинной алгебры => вряд ли при следующей реализации
# появится переполнение, но всё-равно отлов ошибки переполнения реализован (последнее задание).
# Можно делать проверку на sys.maxsize (2^64 значений int), но есть ли в этом смысл, если переполнения не возникает
# всё равно.

def amount(lst):
    res = 0
    try:
        for i in lst:
            res += i
    except OverflowError:
        print("Ошибка переполнения")
        return None
    else:
        return res
        
def composition(lst):
    res = 1
    try:
        for i in lst:
            res *= i
    except OverflowError:
        print("Ошибка переполнения")
        return None
    else:
        return res


lst = read_file("file1.txt")
print(maximum(lst), minimum(lst), amount(lst), composition(lst))
print()


# ## Тестирование функций

def program(lst):
    return (maximum(lst), minimum(lst), amount(lst), composition(lst))

lst1 = [1,1,1,1]
lst2 = [2]
lst3 = [6,-5,4,-3,2,1,0,-1,-2,3,-3]
lst4 = list(range(1000))
lst5 = list(range(1,10))


assert(program(lst1) == (1,1,4,1))
assert(program(lst2) == (2,2,2,2))
assert(program(lst3) == (6,-5,2,0))
assert(program(lst4) == (999,0,499500,0))
assert(program(lst5) == (9,1,45,362880))


# ## Тестирование времени в зависимости от размера файла

def program_with_reading(name):
    lst = read_file(name)
    return (maximum(lst), minimum(lst), amount(lst), composition(lst))


print("Размер файла (байт): ", os.path.getsize("file1.txt"))
print("Время: ", timeit.timeit('''program_with_reading("file1.txt")''', number = 10000, globals=globals()))
print()
print("Размер файла (байт): ", os.path.getsize("file2.txt"))
print("Время: ", timeit.timeit('''program_with_reading("file2.txt")''', number = 10000, globals=globals()))
print()
print("Размер файла: (байт)", os.path.getsize("file3.txt"))
print("Время: ", timeit.timeit('''program_with_reading("file3.txt")''', number = 10000, globals=globals()))
print()


# ## Тестирование времени работы функций от средней длины числа

lst1 = [1]*1000
lst2 = [11]*1000
lst3 = [111]*1000
lst4 = [1111]*1000
lst5 = [11111]*1000

for i in [lst1, lst2, lst3, lst4, lst5]:
    print("средняя длина числа: ", len(str(i[0])))
    print("Время: ", timeit.timeit('''program({})'''.format(i), number = 10000, globals=globals()))
    print()

