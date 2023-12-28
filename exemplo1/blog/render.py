from pathlib import Path
from database import co

cursor = co.cursor()
fields = ("id", "title", "content", "author")
results = cursor.execute("SELECT * FROM post;")
posts = [dict(zip(fields, post))for post in results]

# 2 - cria a pasta do destino ou site


site_dir = Path("site")
site_dir.mkdir(exist_ok=True)

# 3 - criar uma função para criar a nossa url


def post_url(post):
    slug = post['title'].lower().replace(" ", "-")
    return f"{slug}.html"

# 4 - Renderização


index_template = Path("list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li> <a href='{post_url(post)}'> {post['title']} </a> </li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list="\n".join(post_list))
)

# Renderização da pagina do blog 

for post in posts:
    post_template = Path("post.template.html").read_text()
    post_page = site_dir / Path(post_url(post))
    post_page.write_text(post_template.format(post=post))

print("Site generate !!!")

co.close()
