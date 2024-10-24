# store_api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99}
]

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Endpoint to get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
