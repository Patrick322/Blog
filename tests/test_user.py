import unittest
from app import db,create_app,bcrypt
from app.models import User,Post,Comment

class TestUser(unittest.TestCase):
    '''
        Test Class to test the behaviour of the db
      '''

    def setUp(self):
        '''
         Set up method that will run before every Test
        '''

    def tearDown(self):
        pass

    def test_password_hash(self):
        password = 'password'
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        is_valid = bcrypt.check_password_hash(hashed,password)
        self.assertTrue(is_valid is True)

    def test_user_model(self):
        user = User(username='dummy',email="dummytest@gmail.com",password="password")
        self.assertEqual('dummy',user.username)
    


if __name__ == "__main__":
    unittest.main()