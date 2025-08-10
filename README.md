# Task04-Python-REST-API

Flask-Based Product Management API<br/>
This is a simple RESTful API built with Flask that allows managing a list of products. The API supports operations such as retrieving all products, fetching a specific product by ID, creating new products, updating existing ones (full or partial), and deleting products.<br/>

<b>Features:</b><br/>
•	Get all products: Retrieve the complete list of products.<br/>
•	Get a product by ID: Fetch details of a specific product using its unique ID.<br/>
•	Create a new product: Add a new product with specified name, price, and quantity.<br/>
•	Update a product: Fully update an existing product's details.<br/>
•	Partially update a product: Modify specific fields of a product.<br/>
•	Delete a product: Remove a product from the list.<br/>

<b>How the Code Works:</b><br/>
•	Data Storage: The products are stored in an in-memory list called products, initialized with two sample products.<br/>
•	Helper Functions:<br/>
o	find_next_id(): Calculates the next available product ID.<br/>
o	find_product(product_id): Searches for a product by its ID.<br/>

•	API Endpoints:<br/>
o	GET /products: Returns the list of all products in JSON format.<br/>
o	GET /products/<product_id>: Retrieves a specific product by ID.<br/>
o	POST /products: Creates a new product. Expects JSON data with name, price, and quantity.<br/>
o	PUT /products/<product_id>: Fully updates an existing product. Requires all fields.<br/>
o	PATCH /products/<product_id>: Partially updates specific fields of a product.<br/>
o	DELETE /products/<product_id>: Deletes a product by ID.<br/>

<b>Usage:</b><br/>
To run this API:<br/>
1.	Save the code in a Python file (e.g., app.py).<br/>
2.	Install Flask if you haven't (pip install flask).<br/>
3.	Run the app (python app.py). <br/>
   Or you can setup environment using terminal such as:<br/>
   for Linux/Mac:<br/>
   $ export FLASK_APP=app.py<br/>
   $ export FLASK_ENV=development<br/>
   $ flask run<br/><br/>
   for Windows:<br/>
   C:\> set FLASK_APP=app.py<br/>
   C:\> set FLASK_ENV=development<br/>
   C:\> flask run<br/>

4.	Use tools like Postman or curl to interact with the API endpoints.<br/>

<b>Example</b><br/>
To retrieve all products:<br/>
curl -X GET http://localhost:5000/products<br/>

To add a new product:<br/>
curl -X POST -H "Content-Type: application/json" -d '{"name":"Tablet","price":200,"quantity":3}' http://localhost:5000/products<br/>

To update a product:<br/>
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Tablet","price":200,"quantity":3}' http://localhost:5000/products/product-id<br/>

To delete a product:<br/>
curl -X DELETE http://localhost:5000/products/product-id<br/>


