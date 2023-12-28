from wsgiref.simple_server import make_server


def app(environ, start_response):
    print(environ)
    status = "200 ok"
    headers = [("Content-type", "text/html")]
    body = b"<strong>HELLO WORD !!! </strong>"
    start_response(status, headers)
    return [body]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, app)
    server.serve_forever()
