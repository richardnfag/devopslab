from flask import Flask
from flask_wtf.csrf import CSRFProtect
from os import getenv

app = Flask(__name__)

csrf = CSRFProtect(app)


@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps - Final"


if __name__ == "__main__":
    port = int(getenv("PORT", "80"))
    app.run("0.0.0.0", port=port)
