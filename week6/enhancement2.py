import sqlite3

def init_db():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    conn.commit()
    conn.close()

@app.route('/products', methods=['POST'])
@token_required
def add_product():
    data = request.get_json()
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (data['name'], data['price']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product added!"}), 201
