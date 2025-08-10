from flask import Flask, jsonify, request

app = Flask(__name__)

products = [

    {"id": 1, "name": "Mobile", "price": 100, "quantity": 1},
    {"id": 2, "name": "Laptop", "price": 500, "quantity": 1}
]

def find_next_id():
    return max((prod["id"] for prod in products), default = 0 ) + 1

def find_product(product_id):
    return next((prod for prod in products if prod["id"] == product_id), None)

# get - get all products
@app.get("/products")
def get_all_products():
    return jsonify(products)

# get - get individual product by product id
@app.get("/products/<int:product_id>")
def get_products_by_id(product_id):
    prod = find_product(product_id)

    if prod:
        return jsonify(prod)
    else:
        return jsonify({"Error":"Product not found"}), 404

# post - create a new product
@app.post("/products")
def create_product():
    if request.is_json:

        data = request.get_json()

        required_fields = {"name", "price", "quantity"}
        if not required_fields.issubset(data):
            return jsonify({"Error": "Missing required fields"}), 400

        new_prod = {
            "id": find_next_id(),
            "name": data["name"],
            "price": data["price"],
            "quantity": data["quantity"]
        }

        products.append(new_prod)
        return new_prod, 201

    else:
        return {"Error":"Request must be JSON"}, 415

# put - full update a product
@app.put("/products/<int:product_id>")
def update_product(product_id):
    prod = find_product(product_id)

    if prod:

        data = request.get_json()

        required_fields = {"name", "price", "quantity"}
        if not required_fields.issubset(data):
            return jsonify({"Error": "Missing required fields"}), 400

        prod.update({
            "name": data["name"],
            "price": data["price"],
            "quantity": data["quantity"]
        })

        return jsonify(prod)
    else:
        return {"Error": "Product not found"}, 404

# patch - partial update a product
@app.patch("/products/<int:product_id>")
def patch_product(product_id):
    prod = find_product(product_id)

    if prod:

        data = request.get_json()

        required_fields = {"name", "price", "quantity"}

        for key in data:
            if key in required_fields:
                prod[key] = data[key]
            else:
                return {"Error": "Key not found"}, 404

        return jsonify(prod)
    else:
        return {"Error": "Product not found"}, 404

# delete - delete a product
@app.delete("/products/<int:product_id>")
def delete_product(product_id):
    prod = find_product(product_id)

    if prod:
        products.remove(prod)
        return {"Message":"Product deleted"}, 200
    else:
        return {"Error": "Product not found"}, 404







