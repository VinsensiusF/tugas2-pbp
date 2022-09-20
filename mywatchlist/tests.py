from django.test import TestCase, Client

class TestMyWatchList(TestCase):
    def test_html_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    def test_json_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    def test_xml_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)