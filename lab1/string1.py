# 1.
# Входящие параметры: int <count> ,
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'

def num_of_items(count):
    if count >= 10:
        return "Number of: many"
    else:
        return "Number of: " + str(count)


# 2.
# Входящие параметры: string s,
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
    return s[0:2] + s[len(s) - 2:len(s)]


# 3.
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb)

def replace_char(s):
    ch = s[0]
    return s.replace(ch, "*").replace("*", ch, 1)


# 4
# Входящие параметры: string a и b,
# Результат: string где <a> и <b> разделены пробелом
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    return b[0:2] + a[2:len(a)] + ' ' + a[0:2] + b[2:len(b)]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
    print("Test result: " + str(expt == res))
    print("Actual: " + res + "; Expected: " + expt)
    return res == expt


def main():
    print("Test 'num_of_items:'")
    test(num_of_items(11), "Number of: many")
    test(num_of_items(4), "Number of: 4")
    test(num_of_items(10), "Number of: many")
    test(num_of_items(9), "Number of: 9")
    print("Test 'start_end_symbols:'")
    test(start_end_symbols('welcome'), 'weme')
    test(start_end_symbols('cat'), 'caat')
    test(start_end_symbols('thunder'), 'ther')
    print("Test 'replace_char:'")
    test(replace_char('bibble'), 'bi**le')
    test(replace_char('aaaaa'), '*****')
    test(replace_char('rrekdrneerr'), 'r*ekd*nee**')
    print("Test 'str_mix:'")
    test(str_mix('max', 'pid'), 'pix mad')
    test(str_mix('dog', 'dinner'), 'dig donner')
    test(str_mix('cat', 'kitten'), 'dig donner')
    test(str_mix('mouse', 'sun'), 'dig donner')


if __name__ == '__main__':
    main()
