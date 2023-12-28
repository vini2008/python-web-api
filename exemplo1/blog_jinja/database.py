# 1 - se conectar ao banco de dados
from sqlite3 import connect

co = connect("blog.db")
conectando = co.cursor()

# 2 - Executando
co.execute(
    """\
        CREATE TABLE if not exists post(
            id integer PRIMARY KEY AUTOINCREMENT,
            title varchar UNIQUE NOT NULL,
            content varchar NOT NULL,
            author varchar NOT NULL
        );
    """
)
#   3 Criar os posts para adicionar ao seu blog
post = [
    {
        "title": "Python é eleita a linguagem mais popular do Brasil e do mundo",
        "content": """\
         Neste Blog você Aprederá a fazer um blog com python com python
         """,
         "author" : "SHIGIRU MIAMOTO",
    },
    {
        "title": "Como tirar espinhas na depilação a lazer",
        "content": """Você Sabia quem com a agua quente uma panela
        de Pressão e alho você Consegue tirar todas as espinhas.
        """,
        "author": "Nusereve DELAMAEROTO"
    }
]

# 4 - Inserimos o Post Caso O Banco De Dados esteja Vazio
count = conectando.execute("SELECT * FROM post;").fetchall()
if not count:
    conectando.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);
        """,
        post,
    )
    co.commit()
# 5 - verificamos quem foi realmente inseridos
posts = conectando.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2
