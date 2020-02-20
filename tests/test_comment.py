import unittest
from app.models import Post, User, Comment

class TestUser(unittest.TestCase):
    '''
        Test Class to test the behaviour of the db
      '''

    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.user = User(username='dummy', email="dummytest@gmail.com", password="password")
        self.post = Post(title="new blog post", content="This is a new blog post",
                    category="Entertainment", summary="blog post summary",
                    image_file="default.jpg", author=self.user)

    def tearDown(self):
        self.user = None
        self.post = None


    def test_comment_model(self):
        comment = Comment(post_id=self.post.id, description="I like this post",
                          author=self.user)
