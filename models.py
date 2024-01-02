"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Cupcake(db.Model):
    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False,default = "https://tinyurl.com/demo-cupcake")

    



