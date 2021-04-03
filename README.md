# item_service
Backend service for item management

### Application Setup:
Execute following command for setup and dependencies installation.

> python setup.py install

OR

Installing dependencies directly from requirements.txt 

> pip install -r requirements.txt


### Run application:
Execute following command to run app on local server. APIs can be triggered with any API client(e.g. postman).

> python media_upload_app.py

API's are developed using flask framework and other required libraries. A basic sqlite database is used to keep project simple and focus on API related functionalities. 
Code structure is divided in three basic parts: 1) media_upload_app.py: for configuration, db preparation, adding endpoints and running application. 2) models/item.py: for item table in database. 3) resources/item.py: for Item and ItemList resources and methods. A test file is also included (app_test.py) with 7 basic test cases.


### Run test cases:
Execute following command to run all the test cases in app_tests.py file.
Total 7 test cases are included in this file along with setup and teardown functions. 

> python -m unittest app_tests

To disable deprecation warning use below command.

> python -W ignore::DeprecationWarning -m unittest app_tests

### APIs Description:
All API routes are included in media_upload_app.py. API routes, methods and description is as below.

1)  Route : '/items/\<int:id\>'<br />
    Method : GET<br />
    Description : Response item details for given valid id. API format 'http://example.com/api/items/98'
   
2)  Route : '/items'<br />
    Method : GET<br />
    Description : Response list of items and details for given valid id. This could be very large data and hence pagination or any other method will be needed. API format 'http://example.com/api/items'
   
3)  Route : '/items'<br />
    Method : POST<br />
    Description : Requires complete and valid item details in json. Creates new item and gives its URI in the response header. API format 'http://example.com/items'
   
4)  Route : '/items/\<int:id\>'<br />
    Method : PUT<br />
    Description : Requires complete and valid item details in json along with valid id. API format 'http://example.com/items/87'
   
5)  Route : '/items/\<int:id\>'<br />
    Method : DELETE<br />
    Description : Requires valid id. Deletes item. API format 'http://example.com/items/87'







