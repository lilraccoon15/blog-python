from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/blog_de_camille'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
