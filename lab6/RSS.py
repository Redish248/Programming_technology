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
      #  if self.path.startswith('/feed/get_news'):
     #       self._set_headers()
    #    self.send_response(200)
     #       message = next_iteration()
     #       self.wfile.write(json.dumps({
     #           'image': message[0],
     #           'varA': message[1],
     #           'varB': message[2],
      #          'correct_name': message[3]
      #      }).encode())
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



def parse_news(feed):
    interesting = feedparser.parse(feed)
    entry1 = interesting.entries[1]
    parsed_news = []
    for entry in interesting.entries:
        new_news = Entity.News(1, 0, entry.title, entry.id, entry.summary, entry.published)
        parsed_news.append(new_news)
    return parsed_news



# FIXME: проверить/дополнить структуру таблицы
def update_news():
    global connection, cursor
    cursor = connection.cursor()
    cursor.execute('select * from news_python')
    results = cursor.fetchall()
    database_news = []
    for row in results:
        entity = Entity.News(row[0], row[1], row[2], row[3], row[4], row[5])
        cursor.execute('select url from sites where id = ' + str(row[1]))
        results_site = cursor.fetchall()
        entity.site = results_site[0][0]
        database_news.append(entity)


# FIXME: проверить/дополнить структуру таблицы и классов News
# TODO: тут сайт как url, а надо сделать select и вытянуть id --- либо вообще сайт просто как url без доп таблицы? но как тогда хранить с разных мест --- или я задание не поняла (в смысле там с разных сайтов или куда-то переходить надо для разных)
def insert_news(parsed_news):
    global connection, cursor
    cursor = connection.cursor()
    for element in parsed_news:
        cursor.execute('insert into news_python (site, title, link, description, published) values (%s, %s, %s, %s, %s)',
                       element.site, element.title, element.link, element.description, element.published)


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
