from flask_caching import Cache

app.config['CACHE_TYPE'] = 'SimpleCache'
cache = Cache(app)

@app.route('/products/<int:product_id>', methods=['GET'])
@cache.cached(timeout=60, key_prefix="product_<product_id>")
def get_product(product_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    
    if product:
        return jsonify({"id": product[0], "name": product[1], "price": product[2]}), 200
    return jsonify({"error": "Product not found"}), 404
