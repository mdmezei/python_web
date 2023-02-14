from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Eu aqui de novo"        
    }
]

@app.route("/")
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)