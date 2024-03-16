# test_web_scraper.py
import unittest
from src.scraper import web_scraper


class TestWebScraper(unittest.TestCase):
    def test_open_webpage_with_chrome(self):
        url = "http://github.com"
        page_source = web_scraper.open_webpage_with_chrome(url)
        self.assertIsNotNone(page_source)

    def test_get_json_from_api(self):
        api_url = "http://api.github.com"
        json_data = web_scraper.get_json_from_api(api_url)
        self.assertIsNotNone(json_data)

    def test_post_json_to_api(self):
        api_url = "http://api.github.com"
        data = {"test": "data"}
        response = web_scraper.post_json_to_api(api_url, data)
        self.assertIsNotNone(response)

    def test_open_webpage_with_chrome_exception(self):
        url = "http://nonexistentwebsite.com"
        with self.assertRaises(Exception):
            web_scraper.open_webpage_with_chrome(url)

    def test_get_json_from_api_exception(self):
        api_url = "http://nonexistentapi.com"
        with self.assertRaises(Exception):
            web_scraper.get_json_from_api(api_url)

    def test_post_json_to_api_exception(self):
        api_url = "http://nonexistentapi.com"
        data = {"test": "data"}
        with self.assertRaises(Exception):
            web_scraper.post_json_to_api(api_url, data)


if __name__ == '__main__':
    unittest.main()
