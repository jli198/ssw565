import jwt
from functools import wraps

SECRET_KEY = "your_secret_key"

# Token-based authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({"message": "Token is invalid!"}), 403
        return f(*args, **kwargs)
    return decorated

# Apply the decorator to secure routes
@app.route('/products', methods=['POST'])
@token_required
def add_product():
    data = request.get_json()
    if "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input!"}), 400
    
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201
