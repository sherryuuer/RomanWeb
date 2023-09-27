from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# run on pycharm
# now I understand the different between vscode and pycharm.Pycharm give me a env at the very first.
# https://flask.palletsprojects.com/en/2.3.x/
