from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_URI'] = 'mongodb://localhost:27017/data_base_products'

mongo = PyMongo(app)

@app.route('/products', methods=['GET'])
def get_sorted_products():
    collection_products = mongo.db.Prodcuts

    output = []

    for query in collection_products.find().sort("name", 1):
        output.append({'name': query['name']})

    return jsonify({'result': output})

@app.route('/products/<string:parametr>', methods=['GET'])
def get_all_filter(parametr):
    collection_products = mongo.db.Prodcuts

    output = []

    for query in collection_products.find({'parameters.' + parametr: {'$exists': 'true'}}).sort('parameters.' + parametr, -1):
        output.append({'name': query['name'], 'parameters': query['parameters']})

    return jsonify({'result': output})

@app.route('/product/<int:id>', methods=['GET'])
def get_one_framework(id):
    collection_products = mongo.db.Prodcuts

    query = collection_products.find_one({'_id': id})

    if query:
        output = {'name': query['name'], 'description': query['description'], 'parameters': query['parameters']}
    else:
        output = 'No results found'

    return jsonify({'result': output})

@app.route('/product_post', methods=['POST'])
def add_framework():
    collection_products = mongo.db.Prodcuts

    id = request.json['_id']
    name = request.json['name']
    description = request.json['description']
    parameters = request.json['parameters']

    framework_id = collection_products.insert({"_id": id,'name' : name, 'description': description, "parameters": parameters})
    new_prod = collection_products.find_one({'_id': framework_id})

    output = {'name': new_prod['name'], 'description': new_prod['description'], 'parameters':new_prod['parameters']}

    return jsonify({'result': output})

if __name__ == '__main__':
    app.run()