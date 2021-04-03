from flask import Flask
from flask_restful import Api
from db import db
from resources.item import Item, ItemList

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.create_all()

# Adding endpoints to resource
api.add_resource(Item, '/items/<int:id>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)