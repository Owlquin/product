from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data (you should replace this with a database)
products = [
    {
        'id': 1,
        'name': 'Apple',
        'price': 1.99,
        'quantity': 100,
    },
    {
        'id': 2,
        'name': 'Banana',
        'price': 0.99,
        'quantity': 50,
    },
    # Add more product data here
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price'],
        'quantity': data['quantity'],
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
