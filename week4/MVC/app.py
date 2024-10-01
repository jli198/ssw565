from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Sample data for users and roles
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "guest": {"password": "guest123", "role": "Guest"},
    "user": {"password": "user123", "role": "User"}  # Adding the User role
}

# Sample data for products
products = [
    {"id": 1, "name": "Product 1"},
    {"id": 2, "name": "Product 2"},
    {"id": 3, "name": "Product 3"}
]

# Utility function to check user role
def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not auth or not (auth.username in users and auth.password == users[auth.username]["password"]):
                return jsonify({"message": "Unauthorized"}), 401
            user_role = users[auth.username]["role"]
            # Check if the user's role matches the required role or is Admin
            if user_role != role and user_role != "Admin":
                return jsonify({"message": "Access Denied"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Route to view all products - accessible by Guest, User, and Admin
@app.route("/products", methods=["GET"])
@role_required("Guest")
def get_products():
    return jsonify(products), 200

# Route to add a new product - accessible only by Admin
@app.route("/products", methods=["POST"])
@role_required("Admin")
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify({"message": "Product added"}), 201

# Route to update a product - accessible by User and Admin
@app.route("/products/<int:product_id>", methods=["PUT"])
@role_required("User")  # Allow "User" and "Admin" roles to access
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    updated_data = request.json
    if "name" in updated_data:
        product["name"] = updated_data["name"]
    return jsonify({"message": "Product updated"}), 200

# Route to delete a product - accessible only by Admin
@app.route("/products/<int:product_id>", methods=["DELETE"])
@role_required("Admin")
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

# Route for logging in and verifying credentials
@app.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth or not (auth.username in users and auth.password == users[auth.username]["password"]):
        return jsonify({"message": "Invalid credentials"}), 401
    return jsonify({"message": f"Logged in as {auth.username}"}), 200

# Home route to provide a welcome message
@app.route("/", methods=["GET"])
def home():
    return (
        "Welcome to the Flask MVC Example! \n"
        "Use /products to view products, /login to login, and other routes for operations."
    )

if __name__ == "__main__":
    app.run(debug=True)
