from flask import Flask

app = Flask(__name__)
print(__name__)


def make_bold(func):

    def wrapper():
        data = func()
        return f"<b>{data}<b>"
    return wrapper


def make_emphasis(func):

    def wrapper():
        data = func()
        return f"<em>{data}<em>"
    return wrapper


def make_underlined(func):

    def wrapper():
        data = func()
        return f"<u>{data}<u>"

    return wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)

# run this on pycharm
