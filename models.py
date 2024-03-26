from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    author = db.Column(db.String(256), nullable=False)
    category = db.Column(db.String(256), nullable=True)

def create_db_and_models(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
