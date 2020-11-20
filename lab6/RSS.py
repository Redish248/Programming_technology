import feedparser
import psycopg2
import Entity

global connection, cursor

news = []


def parseNews(feed):
    interesting = feedparser.parse(feed)
    entry = interesting.entries[1]


def connect_to_database():
    global connection, cursor
    try:
        connection = psycopg2.connect(user="redish",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        cursor.execute('select * from news_python')
        results = cursor.fetchall()
        for row in results:
            entity = Entity.News(row[0], row[1], row[2], row[3], row[4], row[5])
            cursor.execute('select url from sites where id = ' + str(row[1]))
            results_site = cursor.fetchall()
            entity.site = results_site[0][0]
            news.append(entity)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def main():
    connect_to_database()
    parseNews("https://habrahabr.ru/rss/interesting/")
    print("rss")


if __name__ == '__main__':
    main()
