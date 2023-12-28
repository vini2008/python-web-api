import cgi
from database import co
from pathlib import Path


def get_post_from_database(post_id=None):
    cursor = co.cursor()
    fields = ("id", "title", "content", "author")
    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]


def get_post_list(posts):
    post_list = [
        f"""<li> <a href='{post['id']}'> {post['title']} </a> </li>"""
        for post in posts
    ]
    return "\n".join(post_list)


def render(template_name, **context):
    template = Path(template_name).read_text()
    return template.format(**context).encode("utf-8")


def new_post(post):
    cursor = co.cursor()
    cursor.execute(
        """\
            INSERT INTO post (title, content, author)
            VALUES (:title, :content, :author)
            """,
        post,
    )
    co.commit()


def app(environ, start_response):
    status = "404 Not Found"
    body = b"Content Not found"
    # processar o request
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]

    if path == "/" and method == "GET":
        posts = get_post_from_database()
        body = render("list.template.html", post_list=get_post_list(posts))
        status = "200 OK"
    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render(
            "post.template.html",
            post=get_post_from_database(post_id=post_id)[0],
        )
        status = "200 OK"
    elif path == "/new" and method == "GET":
        body = render("form.html")
        status = "200 OK"
    elif path == "/new" and method == "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"], environ=environ, keep_blank_values=1
        )
        post = {item.name: item.value for item in form.list}
        new_post(post)
        body = b"New post is created with sucess"
        status = "201 created"

    # Criar o response
    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [body]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, app)
    server.serve_forever()
