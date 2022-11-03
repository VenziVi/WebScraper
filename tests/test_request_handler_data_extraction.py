import unittest
from data_extraction.request_handler import RequestHandler
import variables_helper as vh


class TestRequestHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.req_handler = RequestHandler(vh.base_url)
        cls.helper = vh.SoupFromFiles()

    #  base_url
    def test__base_url__when_correct_webpage_is_given__expected_success(self):
        expected = "http://books.toscrape.com/"
        actual = self.req_handler.base_url
        self.assertEqual(expected, actual)

    #  create_request_handler
    def test__create_request_handler__when_correct_webpage_is_given__expected_success(self):
        test_url = "http://books.toscrape.com/index.html"
        expected = False
        raised = False
        try:
            self.req_handler.create_request_handler(test_url)
        except ValueError:
            raised = True
        self.assertEqual(expected, raised)

    def test__create_request_handler__when_incorrect_webpage_is_given__expected_Value_error(self):
        expected = ValueError
        actual = "http://"
        with self.assertRaises(expected):
            self.req_handler.create_request_handler(actual)

    def test__get_page__when_wrong_page_extension_is_given__expected_none(self):
        test_url = "http://"
        actual = self.req_handler.get_page(test_url)
        expected = None
        self.assertEqual(actual, expected)

    #  get_page
    def test__get_page__when_correct_webpage_is_given__expect_success(self):
        expected = self.req_handler.get_page()
        actual = self.req_handler.get_page(extension="")
        self.assertEqual(expected, actual)

    def test__get_page__when_incorrect_webpage_is_given__expect_none(self):
        expected = None
        actual = self.req_handler.get_page("https://")
        self.assertEqual(expected, actual)

    #  get_pages_text_async
    def test__get_pages_text_async__when_correct_value_is_given__expected_unicode_text(self):
        test_url = ["catalogue/a-light-in-the-attic_1000/index.html"]
        expected = 'unicode text'
        actual = self.req_handler.get_pages_text_async(test_url)
        self.assertNotEqual(expected, actual)

    def test__get_pages_text_async__when_wrong_website_is_given__expected_empty_list(self):
        test_url = None
        expected = []
        actual = self.req_handler.get_pages_text_async(test_url)
        self.assertEqual(expected, actual)
