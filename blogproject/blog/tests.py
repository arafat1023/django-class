from django.test import TestCase
from .models import Post, Category
from django.contrib.auth import get_user_model

class PostTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Django')
        self.post = Post.objects.create(title='Test Post', content='Content', author=self.user, category=self.category)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')