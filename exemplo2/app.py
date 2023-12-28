from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_word():
    return """
    <body>
        <h1> Digite Seu Nome </h1>
        <form action="/hello" method="post">
        <label for="title">DIGITE SEU NOME AQUI EM BAIXO :</label><br>
        <input type="text" name="title"><br>
        <input type="submit" value="ENVIAR">
        </form>
    </body>
    """


