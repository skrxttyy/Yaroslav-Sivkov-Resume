import unittest
from scripts.export import render

class ExportTests(unittest.TestCase):
    def test_escaping(self):
        self.assertIn('&lt;script&gt;', render([{'name':'<script>', 'url':'https://github.com/a/b'}]))

    def test_unsafe_url(self):
        with self.assertRaises(ValueError):
            render([{'name':'a', 'url':'javascript:alert(1)'}])
