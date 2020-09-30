# 1.
# Bx: списко чисел, Возвр: список числе, где
# повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].
def rm_adj(nums):
    return list(set(nums))


# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список
def sort_all(list1, list2) -> list:
    return sorted(list1 + list2)


def test(res, expt):
    print("Test result: " + str(expt == res))
    print("Actual: " + str(res) + "; Expected: " + str(expt))
    return res == expt


def main():
    print("Test 'rm_adj:'")
    test(rm_adj([0, 2, 2, 3]), [0, 2, 3])
    test(rm_adj([0, 0, 0, 0, 2, 2, 3]), [0, 2, 3])
    test(rm_adj([0, 2, 3]), [0, 2, 3])
    test(rm_adj([0, 0, 2, 2, 3, 3, 3, 3]), [0, 2, 3])
    print("Test 'sort_all:'")
    test(sort_all([6, 7, 8], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5, 6, 7, 8])
    test(sort_all([15, 16, 17], [1, 3, 4]), [1, 3, 4, 15, 16, 17])
    test(sort_all([-5, -4, -3], [0, 1, 2]), [-5, -4, -3, 0, 1, 2])


if __name__ == '__main__':
    main()
