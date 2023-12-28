#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
nome = form.getvalue("nome")
mensagem = form.getvalue("mensagem")

print("Content-type:text/html\r\n\r\n")
print(
    """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">"""
    )
print("</head>")
print("<title>ENVIADO</title>")
print("</head>")
print("<body>")
print("<h1>Enviado com Sucesso !!!</h1>")
print(f"<h2> {nome} - {mensagem} <h2>")
print("</body>")
print("</html>")
