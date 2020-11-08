"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь, который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...]

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import random
import sys

generated_words = {}


def mem_dict(filename):
    try:
        with open(filename, 'r') as file:
            all_words = list(read_all_words(file))
            i = 0
            current_word = all_words[0]
            while i < len(all_words):
                if all_words[i] is not None and i != len(all_words) - 1:
                    if generated_words.get(all_words[i].lower()) is None:
                        generated_words[all_words[i].lower()] = [all_words[i + 1].lower()]
                    else:
                        generated_words[all_words[i].lower()].append(all_words[i + 1].lower())
                i = i + 1

        new_file = open("new_dict.txt", "w")
        new_file.write(current_word + ' ')
        while current_word.lower() != 'coach':
            current_word = random.choice(generated_words.get(current_word.lower()))
            new_file.write(current_word.lower() + ' ')
        new_file.close()
    except IOError:
        print("Error during opening or reading file.")
    return


def read_all_words(file):
    for line in file:
        for word in line.split():
            yield word


def main():
    args = sys.argv[1:]
    if not args:
        print('Enter file name!')
        sys.exit(1)
    else:
        mem_dict(args[0])


if __name__ == '__main__':
    main()
