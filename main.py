from flask import Flask, Blueprint
from books_routes import book_blueprint
from customer_routes import customer_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)
app.register_blueprint(customer_blueprint)



