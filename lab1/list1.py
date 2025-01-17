# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему

def me(words):
    count = 0
    for element in words:
        if (len(element) > 2) and (element[0] == element[len(element) - 1]):
            count += 1
    return count


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    xlist = []
    olist = []
    for element in words:
        if element[0] == 'x':
            xlist.append(element)
        else:
            olist.append(element)
    xlist.sort()
    olist.sort()
    xlist.extend(olist)
    return xlist


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def cort(numbers):
    numbers.sort(key=lambda x: (x[len(x) - 1]))
    return numbers


def test(res, expt):
    print("Test result: " + str(expt == res))
    print("Actual: " + str(res) + "; Expected: " + str(expt))
    return res == expt


def main():
    print("Test 'me:'")
    test(me(['a', 'bbb', 'ads', 'ssss', 'aveg']), 2)
    test(me(['a', 'bwb', 'dddddwd', 'ssss', 'aveg']), 3)
    test(me(['arr', '5532', '11', 'ssss42a', 'avega']), 0)
    test(me(['arr', '5532', '11', 'ssss42a', 'avega']), 1)
    print("Test 'fx:'")
    test(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']), ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix'])
    test(fx(['bba', 'aaa', 'xsa', 'bab', 'xas']), ['xas', 'xsa', 'aaa', 'bab', 'bba'])
    test(fx(['bba', 'aaa', 'xsa', 'bab', 'xas']), ['xas', 'xsa', 'bba', 'bab', 'aaa'])
    print("Test 'cort:'")
    test(cort([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    test(cort([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 7), (3, 4, 5), (1, 3)])
    test(cort([(10, 7, 8), (1, 3), (3, 5), (2, 2)]), [(2, 2), (1, 3), (3, 5), (10, 7, 8)])


if __name__ == '__main__':
    main()
