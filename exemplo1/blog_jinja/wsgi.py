from serve import Serve
from database import co


app = Serve()


def get_post_from_database(post_id=None):
    cursor = co.cursor()
    fields = ("id", "title", "content", "author")
    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]


@app.route("^/$", template="list.template.html")
def post_list():
    posts = get_post_from_database()
    return {"post_list": posts}


@app.route("^/api$")
def post_list_api():
    posts = get_post_from_database()
    return {"post_list": posts}


@app.route("^/(?P<id>\d{1,})$", template="post.template.html")
def post_detail(id):
    post = get_post_from_database(post_id=id)[0]
    return {"post": post}


@app.route("^/new$", template="form.template.html")
def new_post_form():
    return {}


@app.route("^new$", method="POST")
def add_new_post(form):
    post = {item.name: item.value for item in form.list}
    new_post(post)
    return "POST CREATED WITH SUCESS", "201 CREATED", "text/plain"


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


if __name__ == "__main__":
    app.run()
