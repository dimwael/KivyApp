from  flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init Flask application
app = Flask(__name__)

# Get file path 
file_path = os.path.abspath(os.getcwd()) + '/database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init DB
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Create Product Class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    # Instantiate Product Class
    def __init__(self,name,description,price,qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Create Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ['id','name', 'description', 'price', 'qty']
    
# Instantiate Product Schema
product_schema  = ProductSchema()
products_schema = ProductSchema(many= True )

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    # Create Product Instanace
    new_product = Product(name,description,price,qty)

    #Save Instanace to DB
    db.session.add(new_product)
    db.session.commit()

    # return request json
    return product_schema.jsonify(new_product)

# Run the Application
if(__name__=="__main__"):
    app.run(debug=True)