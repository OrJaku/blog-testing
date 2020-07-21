from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test_name", "Test_post_content")
        self.assertEqual("Test_name", p.title)
        self.assertEqual("Test_post_content", p.content)