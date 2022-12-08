import search4web
import unittest

class TestSearch(unittest.TestCase):
    def test_add(self):
        # tests for the add() function
        self.assertEqual(search4web.search4letters("hola","aeiou"), {'o','a'})
        self.assertEqual(search4web.search4letters("holiii", "aeiou"), {'o','i'})
        self.assertEqual(search4web.search4letters("holita", "aeiou"), {'o', 'i', 'a'})
        self.assertEqual(search4web.search4letters("murcielago", "aeiou"), {'u', 'i', 'e', 'a', 'o'})

