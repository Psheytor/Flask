import unittest
from app import app
class FormTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_login_form(self):
        response = self.app.post('/check_auth', data={'name': 'testuser',
                                                      'email': 'testuser@example.com',
                                                      'password': 'afsfDaaaaa'
        })
        self.assertEqual(response.status_code, 200)

    def test_registration_form(self):
        response = self.app.post('/check_reg', data={'name': 'testuser',
                                                      'email': 'testuser@example.com',
                                                      'password': 'afsfDaaaaa',
                                                      'repassword': 'afsfDaaaaa'
        })
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()