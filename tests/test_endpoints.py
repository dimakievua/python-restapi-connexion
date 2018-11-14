from app import app
from flask import url_for
import flaskapi
import unittest

class FlaskTodosTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def tearDown(self):
        pass

    def setUp(self):
        # Set up test application client
        self.app = app.test_client() 
        self.app.testing = True

    def test_home_status_code(self):
        # Assert that user successfully lands on homepage
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

#    def test_home_data(self):
#        # sends HTTP GET request to the application
#        # on the specified path
#        result = self.app.get('/') 
#
#        # assert the response data
#        self.assertEqual(result.data, "Hello World!!!")

if __name__ == '__main__':
    unittest.main()
