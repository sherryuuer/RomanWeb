from flask import Flask, render_template


app = Flask(__name__)


@app.route("/page1")
def site1():
    return render_template("sally-page1.html")


@app.route("/page2")
def site2():
    return render_template("sally-page2.html")


if __name__ == "__main__":
    app.run(debug=True)
