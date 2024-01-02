"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.app = app
db.init_app(app)

with app.app_context():
    db.create_all()

def serialized_cupcake(cupcake):
    return {
        "id" : cupcake.id,
        "flavor":cupcake.flavor,
        "size":cupcake.size,
        "rating":cupcake.rating,
        "image":cupcake.image

    }

@app.route("/api/cupcakes")
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [serialized_cupcake(cupcake) for cupcake in cupcakes]
    return jsonify(cupcake=serialized)
    

@app.route("/api/cupcakes/<id>")
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    serialized = [serialized_cupcake(cupcake)]
    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes", methods = ["GET","POST"])
def create_cupcake():
    
    flavor = request.json["cupcake"][0]["flavor"]

   
    size = request.json["cupcake"][0]["size"]
    rating = request.json["cupcake"][0]["rating"]
    image = request.json["cupcake"][0]["image"]

    new_cupcake = Cupcake(flavor=flavor, size = size, rating = rating, image = image)
    


    db.session.add(new_cupcake)
    db.session.commit()
    cupcake = serialized_cupcake(new_cupcake)
    return (jsonify(cupcake=cupcake), 201)

@app.route("/api/cupcakes/<id>", methods=["GET","PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = request.json["cupcake"][0]["flavor"]
    cupcake.size = request.json["cupcake"][0]["size"]
    cupcake.rating = request.json["cupcake"][0]["rating"]
    cupcake.image = request.json["cupcake"][0]["image"]

    db.session.add(cupcake)
    db.session.commit()
    
    c = serialized_cupcake(cupcake)


    return jsonify(cupcake = c)

    
@app.route("/api/cupcakes/<id>", methods=["GET","DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    c = serialized_cupcake(cupcake)

    return jsonify(cupcake = c)  


@app.route('/', methods = ["GET", "POST"])
def user():
    return render_template('base.html')


