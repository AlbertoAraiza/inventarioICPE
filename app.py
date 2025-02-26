from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return f'<p>Hello, {escape(name)}!</p>'

@app.route('/')
def index():
    return '<p>Index page</p>'

@app.route('/hello')
def hello():
    return '<p>Hello, World!</p>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'<p>User {escape(username)}</p>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<p>Post {post_id}</p>'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'<p>Subpath {escape(subpath)}</p>'

@app.route('/projects/')
def projects():
    return '<p>The project page</p>'

@app.route('/about')
def about():
    return '<p>The about page</p>'