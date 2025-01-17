import re


# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing",
# если в конце нет уже "ing", иначе добавить "ly".
def add_tail(s):
    if len(s) > 3:
        if s.endswith('ing'):
            s += 'ly'
        else:
            s += 'ing'
    return s


# 2.
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!
# def not_bad_old(s):
#    try:
#        if s.index('bad') > s.index('not'):
#            return s[0:s.index('not')] + 'good' + s[s.index('bad') + 3:len(s)]
#        else:
#            return s
#    except ValueError:
#        return s


def not_bad(s):
    return re.sub('not[\w\s]*bad', 'good', s)


def test(res, expt):
    print("Actual: " + str(res) + "; Expected: " + str(expt))
    print("Test result: " + str(expt == res) + '\n')
    return res == expt


def main():
    print("Test 'add_tail:'")
    test(add_tail('ma'), 'ma')
    test(add_tail('block'), 'blocking')
    test(add_tail('blocking'), 'blockingly')
    print("Test 'not_bad:'")
    test(not_bad('This music is not so bad!'), 'This music is good!')
    test(not_bad('This music is cool!'), 'This music is cool!')
    test(not_bad('bad aaaaaaaa not aaaa not aaa bad'), 'bad aaaaaaaa good')


if __name__ == '__main__':
    main()
