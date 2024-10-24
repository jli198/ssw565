# product_model.py
import sqlite3

def get_product_by_id(product_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

# store_api.py (incomplete)
from product_model import get_product_by_id

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify({"id": product[0], "name": product[1], "price": product[2]}), 200
    return jsonify({"error": "Product not found"}), 404
