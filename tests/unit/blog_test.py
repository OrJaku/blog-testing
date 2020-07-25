from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test_blog", "Test_blog_author")

        self.assertEqual("Test_blog", b.title)
        self.assertEqual("Test_blog_author", b.author)
        self.assertListEqual([], b.post)

    def test_repr(self):
        b = Blog("Test_blog", "Test_blog_author")
        b2 = Blog("Pierwszy post", "Kuba")
        b2.post = ["testowy", "drugi testowy"]
        self.assertEqual(b.__repr__(), "Test_blog by Test_blog_author (0 post)")
        self.assertEqual(b2.__repr__(), "Pierwszy post by Kuba (2 posts)")

