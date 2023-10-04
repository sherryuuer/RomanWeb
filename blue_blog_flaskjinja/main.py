from flask import Flask, render_template
from post import Post

post = Post()
contents = post.get_blogs()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs = contents)

@app.route('/blog/<int:id>')
def blog(id):
    return render_template("post.html", blogs = contents, blogid = id )



if __name__ == "__main__":
    app.run(debug=True)
