import search4web
import unittest

class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search4web.search4letters("hola","aeiou"), {'o','a'})
        self.assertEqual(search4web.search4letters("holiii", "aeiou"), {'o','i'})
        self.assertEqual(search4web.search4letters("holita", "aeiou"), {'o', 'i', 'a'})
        self.assertEqual(search4web.search4letters("murcielago", "aeiou"), {'u', 'i', 'e', 'a', 'o'})

    def test_search_up(self):
        self.assertEqual(search4web.search4letters_upgrade("hola me llamo sergio. Y tu?","aeiou"), [['hola me llamo sergio', ' Y tu?'], [{'a', 'e', 'i', 'o'}, {'u'}]])
        self.assertEqual(search4web.search4letters_upgrade("Adios Maribel. Ten cuidado", "aeiou"), [['Adios Maribel', ' Ten cuidado'], [{'e', 'i', 'a', 'o'}, {'e', 'i', 'u', 'o', 'a'}]])
        self.assertEqual(search4web.search4letters_upgrade("No me lo puedo creer. Has sido capaz","aeiou"), [['No me lo puedo creer', ' Has sido capaz'], [{'u', 'o', 'e'}, {'o', 'i', 'a'}]])
        self.assertEqual(search4web.search4letters_upgrade("Chicos. A cenar.","aeiou"), [['Chicos', ' A cenar'], [{'i', 'o'}, {'a', 'e'}]])
