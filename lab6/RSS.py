import cgi
import json

import feedparser
import psycopg2
import Entity
from http.server import BaseHTTPRequestHandler, HTTPServer

global connection, cursor

hostName = "localhost"
serverPort = 8080


class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "http://localhost:3000")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.end_headers()

    def do_GET(self):
        if self.path == '/feed/get_sites':
            self.send_response(200)
            self._set_headers()
            message = get_sites()
            self.wfile.write(json.dumps(message, default = lambda x: x.__dict__).encode())
        if self.path.startswith('/feed/get_news'):
            self.send_response(200)
            self._set_headers()
            site_id = self.path[self.path.index("id=") + 3:self.path.index("&")]
            page = self.path[self.path.index("page=") + 5:]
            message = get_news(site_id, page)
            self.wfile.write(json.dumps({
                'news': message[0],
                'isLastPage': message[1]
            }, default = lambda x: x.__dict__).encode())
        if self.path.startswith('/feed/update_news'):
            self.send_response(200)
            self._set_headers()
            site_id = self.path[self.path.index("id=") + 3:]
            update_news(site_id)
            message = get_news(site_id, 1)
            self.wfile.write(json.dumps({
                'news': message[0],
                'isLastPage': message[1]
            }, default=lambda x: x.__dict__).encode())
        return

    def do_POST(self):
        if self.path.startswith('/feed/add_site'):
            feed_url = ''
            ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
            if ctype == 'multipart/form-data':
                pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
                feed_url = cgi.parse_multipart(self.rfile, pdict).get('url')[0]
            result = add_site(feed_url)
            if result is not None:
                self.send_response(200)
                self._set_headers()
                self.wfile.write(json.dumps(result, default = lambda x: x.__dict__).encode())
            else:
                self.send_response(409)
                self._set_headers()
                self.wfile.write(bytes('Site exists!', 'utf-8'))
        return


def update_news(site_id):
    global connection, cursor
    cursor = connection.cursor()
    cursor.execute('select url from sites where id = ' + site_id)
    results = cursor.fetchall()
    parsed_news = parse_news(results[0][0])
    insert_new_news(parsed_news, site_id)


def insert_new_news(parsed_news, site_id):
    global connection, cursor
    cursor = connection.cursor()
    for news in parsed_news:
        cursor.execute('select * from news_python where id = \'' + site_id + '\' and link = \'' + news.link + '\'')
        exists = cursor.fetchall()
        if len(exists) == 0:
            try:
                cursor.execute('insert into news_python (site, title, link, description, published)  values ('
                               + site_id + ',\'' + news.title + '\', \'' + str(news.link) + '\', \'' + str(news.description) +
                               '\', \'' + news.published[:-5] + '\')')
                connection.commit()
            except psycopg2.Error:
                connection.rollback()


def get_news(site_id, page):
    global connection, cursor
    cursor = connection.cursor()
    cursor.execute('select * from news_python where site = ' + site_id)
    results = cursor.fetchall()
    news = []
    for row in results:
        entity = Entity.News(row[0], row[1], row[2], row[3], row[4], row[5])
        news.append(entity)
    isLastPage = (len(news) <= int(page)*10)
    return [news[int(2)*10 - 10:int(2)*10], isLastPage]


def parse_news(feed):
    interesting = feedparser.parse(feed)
    parsed_news = []
    for entry in interesting.entries:
        new_news = Entity.News(1, 0, entry.title, entry.id, entry.summary, entry.published)
        parsed_news.append(new_news)
    return parsed_news


def add_site(site_url):
    global connection, cursor
    cursor = connection.cursor()
    cursor.execute('select * from sites where url = \'' +  str(site_url) + '\'')
    if len(cursor.fetchall()) == 0:
        name = feedparser.parse(site_url).feed.title
        cursor.execute('insert into sites (name, url)  values (\'' + name + '\', \'' + site_url + '\')')
        connection.commit()
        cursor.execute('select * from sites where url = \'' + str(site_url) + '\'')
        entity = cursor.fetchall()
        return Entity.Site(entity[0][0], entity[0][1], entity[0][2])
    else:
        return None


def get_sites():
    global connection, cursor
    cursor = connection.cursor()
    cursor.execute('select * from sites')
    results = cursor.fetchall()
    sites = []
    for row in results:
        entity = Entity.Site(row[0], row[1], row[2])
        sites.append(entity)
    return sites


def main():
    webServer = HTTPServer((hostName, serverPort), MyHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))
    global connection, cursor
    try:
        connection = psycopg2.connect(user="redish",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    webServer.server_close()
    print("Server stopped.")


if __name__ == '__main__':
    main()
