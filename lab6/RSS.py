import feedparser
import psycopg2
import Entity

global connection, cursor

database_news = []
parsed_news = []


# TODO: решить, как парсить, т.е. что будет оттуда вставлять в табличку
def parse_news(feed):
    interesting = feedparser.parse(feed)
    entry = interesting.entries[1]
    # засунуть в parsed_news

# FIXME: проверить/дополнить структуру таблицы
def update_news():
    global connection, cursor
    cursor = connection.cursor()
    cursor.execute('select * from news_python')
    results = cursor.fetchall()
    for row in results:
        entity = Entity.News(row[0], row[1], row[2], row[3], row[4], row[5])
        cursor.execute('select url from sites where id = ' + str(row[1]))
        results_site = cursor.fetchall()
        entity.site = results_site[0][0]
        database_news.append(entity)


# FIXME: проверить/дополнить структуру таблицы и классов News
# TODO: тут сайт как url, а надо сделать select и вытянуть id --- либо вообще сайт просто как url без доп таблицы? но как тогда хранить с разных мест --- или я задание не поняла (в смысле там с разных сайтов или куда-то переходить надо для разных)
def insert_news():
    cursor = connection.cursor()
    for element in parsed_news:
        cursor.execute('insert (site, title, link, description, published) into news_python values (%s, %s, %s, %s, %s)',
                       element.site, element.title, element.link, element.description, element.published)


# TODO: пофиксить/дополнить вывод -- передавать как параметр массив с каким-то количеством элементов(как страницы)
def print_news(news):
    for element in news:
        print("Сайт: %s,\n Заголовок: %s,\n Ссылка: %s,\n Описание: %s,\n Дата публикации: %s\n\n\n",
              element.site, element.title, element.link, element.description, element.published)


def main():
    global connection, cursor
    try:
        connection = psycopg2.connect(user="redish",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        parse_news("https://habrahabr.ru/rss/interesting/")
        insert_news()
        update_news()
        print("rss")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    main()
