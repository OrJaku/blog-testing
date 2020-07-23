from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test_name", "Test_post_content")
        self.assertEqual("Test_name", p.title)
        self.assertEqual("Test_post_content", p.content)

    def test_json(self):
        p = Post("Test_json_name", "Test_post_json_content")
        expected = {'title': 'Test_json_name', 'content': 'Test_post_json_content'}

        self.assertDictEqual(expected, p.json())
