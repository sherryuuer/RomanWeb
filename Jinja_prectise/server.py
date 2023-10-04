from flask import Flask, render_template
from datetime import datetime
from functions import get_blogs, get_age, get_gender


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<name>')
def guess(name):
    date_of_the_year = datetime.now().year
    name, age = get_age(user_name=name)
    gender = get_gender(user_name=name)
    return render_template("guess.html", age = age, name = name, gender = gender, year = date_of_the_year)


@app.route('/blog/<int:blogid>')
def blog(blogid):
    contents = get_blogs()
    return render_template("blogs.html", blogs = contents, blogid = blogid)


if __name__ == '__main__':
    app.run(debug=True)
