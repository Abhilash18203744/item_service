from flask import request
from flask_restful import Resource
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from models.item import ItemModel
import datetime

# For validation of input JSON
validate_json_schema = {
    'type': 'object',
    'required': ['file_name', 'media_type'],
    'properties': {
        'file_name': { 'type': 'string' },
        'media_type': { 'type': 'string' },
    }
}

class JsonInputs(Inputs):
   json = [JsonSchema(schema=validate_json_schema)]

def validate_json_input(request):
   inputs = JsonInputs(request)
   if inputs.validate():
       return None
   else:
       return inputs.errors


# Item class with GET, PUT, DELETE methods, id needed in the endpoint
class Item(Resource):
    def get(self, id):
        item = ItemModel.query.get(id)
        if item:
            return item.json(), 200
        return {"Message": "Item not found."}, 404

    def put(self, id):
        # Validate input json
        error = validate_json_input(request)
        if error:
            return {"Message": "Invalid input json."}, 422

        item = ItemModel.query.get(id)
        if not item:
            return {"Message": "Item not found."}, 404

        file_name = request.json["file_name"]
        media_type = request.json["media_type"]

        if ItemModel.find_by_name_type(file_name, media_type):
            return {"Message": "An item with name '{}' and '{}' already exists.".format(file_name, media_type)}, 409

        # Updating item details
        item.file_name = file_name
        item.media_type = media_type
        item.updated_at = datetime.datetime.now()

        try:
            item.save_to_db()
        except:
            return {"Message": "An error occurred while updating the item record."}, 500

        return {"Message": "Item with ID {} altered.".format(id)}, 200

    def delete(self, id):
        if not id:
            return {'Message': 'Must provide the item ID'}, 400
        item = ItemModel.query.get(id)
        if item:
            item.delete_from_db()
            return {"Message": "Item with ID {} deleted.".format(id)}, 200

        return {"Message": "Item not found."}, 404


# ItemList class with GET, POST methods, id not expected in the endpoint
class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}, 200

    def post(self):
        # validate input json
        error = validate_json_input(request)
        if error:
            return {"Message": "Invalid input json."}, 422

        file_name = request.json["file_name"]
        media_type = request.json["media_type"]

        if ItemModel.find_by_name_type(file_name, media_type):
            return {"Message": "An item with name '{}' and '{}' already exists.".format(file_name, media_type)}, 409

        # created_at and updated_at will be same
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

        item = ItemModel(file_name, media_type, created_at, updated_at)
        try:
            item.save_to_db()
        except:
            return {"Message": "An error occurred while inserting the item."}, 500

        return {"Message": "Item with name '{}' created.".format(file_name)}, 201, {'location': '/items/{}'.format(item.id)}
