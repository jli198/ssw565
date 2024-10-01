from flask import Flask, render_template, request, redirect, url_for
from models import ProductModel
from views import display_products

app = Flask(__name__)
product_model = ProductModel()

@app.route('/')
def index():
    # Controller fetches data from the Model and passes it to the View
    products = product_model.get_all_products()
    return display_products(products)

@app.route('/add', methods=['POST'])
def add_product():
    # Controller handles user input and updates the Model
    product_name = request.form['name']
    product_model.add_product(product_name)
    return redirect(url_for('index'))

@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    # Controller handles deleting a product
    product_model.delete_product(product_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
