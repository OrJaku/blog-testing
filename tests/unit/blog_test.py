from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test_blog", "Test_blog_author")

        self.assertEqual("Test_blog", b.title)
        self.assertEqual("Test_blog_author", b.author)
        self.assertListEqual([], b.post)
