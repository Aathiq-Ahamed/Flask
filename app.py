from flask import Flask

app = Flask(__name__)


@app.route("/")
def print_name():
    return "Aathiq"


print(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
