"""
import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)        

if __name__ == '__main__':
    unittest.main()
---
from swagger_tester import swagger_test

authorize_error = {
    'get': {
        '/health': [200],
    }
}

def test_swagger():
    swagger_test('./swagger/swagger.yml', authorize_error=authorize_error)
---
"""
import pytest
import server
import connexion

flask_app = connexion.FlaskApp(api)
flask_app.add_api('../swagger/swagger.yml')

@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
"""
---
import server
import health
from flask import url_for
import unittest
# from swagger_tester import swagger_test

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
        # swagger_test(app_url='/api/health', use_example=True)
        # Set up test application client
        self.app = server.app.test_client() 
        self.app.testing = True
    def test_home_status_code(self):
        # Assert that user successfully lands on homepage
        result = self.app.get('/api/health')
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the response data
        self.assertEqual(result.data, "Hello World!!!")

if __name__ == '__main__':
    unittest.main()
"""