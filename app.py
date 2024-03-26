from flask import Flask, render_template
from flask_scss import Scss
from config import Config
from flask_migrate import Migrate
from models import db, create_db_and_models
from utils import get_post_by_id


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    create_db_and_models(app)
    migrate = Migrate(app, db)

    Scss(app)   

    return app

app = create_app()

@app.route('/')
def index():
    from models import Post
    posts = Post.query.all()
    return render_template('homePage.html', posts=posts)

@app.route('/article/<int:id>')
def article(id):
    post = get_post_by_id(id)
    return render_template('article.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
