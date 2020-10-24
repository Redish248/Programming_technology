import sys
from lxml import html as et

woman = {}
man = {}


# Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
# '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
def extr_name(filename):
    file = et.parse(filename)
    year = file.xpath('/html/body/table/tr/td/form/input')[0].value
    allTable = file.xpath('/html/body/table/tr/td/table/tr')
    allPeople = []
    for col in allTable:
        row = col.xpath('td')
        if len(row) == 3:
            if woman.get(row[2].text) is None:
                woman[row[2].text] = int(row[0].text)
            else:
                woman[row[2].text] += int(row[0].text)
            if man.get(row[1].text) is None:
                man[row[1].text] = int(row[0].text)
            else:
                man[row[1].text] += int(row[0].text)
            allPeople.append((row[0].text, row[2].text))
            allPeople.append((row[0].text, row[1].text))
    print_list(allPeople, year)
    return


# напечатать ТОП-10 муж и жен имен из всех переданных файлов
def get_top(table_list):
    i = 0
    table_list = sorted(table_list.items(), key=lambda item: item[1], reverse=True)
    for person in table_list:
        if i < 10:
            print(person[0])
        i = i + 1
    return


def print_list(allPeople, year):
    print(year + ':')
    allPeople.sort(key=lambda x: (x[1]))
    for person in allPeople:
        print(person[1] + ' ' + person[0])
    return


# для каждого переданного аргументом имени файла, вывести имена  extr_name
def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    else:
        for i in args:
            extr_name(i)
    print("ТОП-10 женских имён:")
    get_top(woman)
    print("ТОП-10 мужских имён:")
    get_top(man)


if __name__ == '__main__':
    main()
