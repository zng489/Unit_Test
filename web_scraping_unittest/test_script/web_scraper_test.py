import unittest
from unittest.mock import patch
import requests
from script.scraper import web_scrap


class TestWebScrap(unittest.TestCase):

    def test_webscrap(self):
            self.assertEqual(web_scrap(), '<Response [200]>')



if __name__ == '__main__':
    unittest.main()