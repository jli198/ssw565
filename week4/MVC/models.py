class ProductModel:
    def __init__(self):
        # A simple in-memory storage for products
        self.products = [
            {'id': 1, 'name': 'Product 1'},
            {'id': 2, 'name': 'Product 2'},
            {'id': 3, 'name': 'Product 3'}
        ]
        self.next_id = 4
    
    def get_all_products(self):
        return self.products
    
    def add_product(self, name):
        new_product = {'id': self.next_id, 'name': name}
        self.products.append(new_product)
        self.next_id += 1

    def delete_product(self, product_id):
        self.products = [product for product in self.products if product['id'] != product_id]
