import json
import unittest
from item_service_app import app
from db import db

# Binding db to app
db.init_app(app)

class BasicTests(unittest.TestCase):

    # Setup and Teardown
    # Executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    # Executed after each test
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_empty_db(self):
        """
        Test case (GET request) to fetch data from empty db
        """
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        expected = {"items":[]}
        self.assertEqual(expected, json.loads(response.get_data(as_text=True)))

    def test_create_item(self):
        """
        Test case (POST request) to create new item
        """
        item_data = {
            "file_name": "Digital watermark",
            "media_type": "mov"
        }
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_item(self):
        """
        Test case (GET request) to fetch item details from db
        """
        item_data = {
            "file_name": "Digital watermark",
            "media_type": "mov"
        }
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')

        response = self.client.get(response.headers['location'])
        self.assertEqual(response.status_code, 200)

    def test_create_duplicate_item(self):
        """
        Test case (POST request) to create item already exists
        """
        item_data = {
            "file_name": "Digital watermark",
            "media_type": "mov"
        }
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_update_item(self):
        """
        Test case (PUT request) to update item data
        """
        item_data = {
            "file_name": "Digital watermark",
            "media_type": "mov"
        }
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')
        updated_item_data = {
            "file_name": "Digital watermark new",
            "media_type": "mov"
        }
        response = self.client.put(response.headers['location'],
                                    data=json.dumps(updated_item_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        """
        Test case (DELETE request) to delete intem
        """
        item_data = {
            "file_name": "Digital watermark",
            "media_type": "mov"
        }
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')
        response = self.client.delete(response.headers['location'])
        self.assertEqual(response.status_code, 200)

    def test_create_item_invalid_data(self):
        """
        Test case (POST request) to create item with invalid data
        """
        item_data = {
            "file_name": "Digital watermark",
            "user_id": 123412
        }
        response = self.client.post('/items',
                                    data=json.dumps(item_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 422)