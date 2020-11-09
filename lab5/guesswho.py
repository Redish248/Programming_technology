import json
import random
import requests
from lxml import html
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

level = 1
people = []


class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', "http://localhost:3000")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        if self.path == '/game/next_question':
            self._set_headers()
            message = next_iteration()
            self.wfile.write(json.dumps({
                'image': message[0],
                'varA': message[1],
                'varB': message[2],
                'correct_name': message[3]
            }).encode())
        return

    def do_POST(self):
        if self.path == '/game/send_level':
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            global level
            level = int(str(post_body)[str(post_body).index("level") + 14])
            execute_game()
            self.send_response(200)
        return


def read_file(file):
    for line in file:
        yield line


def execute_game():
    global people
    with open('guess.txt', 'r') as file:
        people = list(read_file(file))
    people = choose_level()
    return


def next_iteration():
    correct_name = random.choice(people)
    if people[people.index(correct_name) + 1] is not None:
        varA = people[people.index(correct_name) + 1]
    else:
        varA = people[people.index(correct_name) - 2]
    if people[people.index(correct_name) - 1] is not None:
        varB = people[people.index(correct_name) - 1]
    else:
        varB = people[people.index(correct_name) + 2]
    image = get_image(correct_name)
    return [image, varA, varB, correct_name]


def choose_level():
    return {
        1: people[:10],
        2: people[:50],
        3: people
    }[level]


def get_image(name):
    req_key = str(name).replace("\n", " ") + " лицо"
    google_page = requests.get(f'https://www.google.com/search?tbm=isch&q={req_key}')
    images = html.fromstring(google_page.content).xpath("//img/@src")
    del images[0]
    return random.choice(images)


def main():
    webServer = HTTPServer((hostName, serverPort), MyHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


if __name__ == '__main__':
    main()
