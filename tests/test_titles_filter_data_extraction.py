import os
import unittest
from data_extraction.filters.titles_filter import TitlesFilter
import variables_helper as vh


class TestTitlesFilter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = os.getcwd() + '/books.json'
        cls.test_instance = TitlesFilter(cls.file_path)

    def test__titles_list__returns_titles_list__success(self):
        expected = vh.expected_file_contents['titles']
        actual = self.test_instance.titles_list
        self.assertEqual(expected, actual)

    def test__is_file_empty__when_correct_file_path_is_given__expected_return_false(self):
        expected = False
        actual = self.test_instance.is_file_empty(self.file_path)
        self.assertEqual(actual, expected)

    def test__is_file_empty__when_wrong_file_path_is_given__expected_return_false(self):
        test_path = ''
        expected = True
        actual = self.test_instance.is_file_empty(test_path)
        self.assertEqual(actual, expected)

    def test__read_titles_from_file__when_correct_path_is_given__expected_return_list_of_titles(self):
        expected = vh.expected_file_contents['titles']
        actual = self.test_instance._TitlesFilter__read_titles_from_file(self.file_path)
        self.assertEqual(expected, actual)

    def test__read_titles_from_file__when_wrong_path_is_given__expected_return_empty_list(self):
        test_path = ''
        expected = []
        actual = self.test_instance._TitlesFilter__read_titles_from_file(test_path)
        self.assertEqual(expected, actual)

    def test__read_titles_from_file__when_correct_path_but_wrong_file_is_given__expected_raise_value_error_return_empty_list(self):
        create_test_files = vh.SoupFromFiles().files_creator()
        test_path = './Bookpage.html'
        expected = []
        actual = self.test_instance._TitlesFilter__read_titles_from_file(test_path)
        self.assertEqual(expected, actual)

    def test__book_url_list__getter__expected_success(self):
        self.test_instance._TitlesFilter__book_url_list = 'http://test.url.com'
        expected = 'http://test.url.com'
        actual = self.test_instance.book_url_list
        self.assertEqual(expected, actual)

    def test__filter_books_by_titles__when_books_do_not_exist_in_dict__expected_empty_list(self):
        expected = []
        actual = TitlesFilter(self.file_path).filter_books_by_titles(vh.expected_book_categories)
        self.assertEqual(expected, actual)

    def test__filter_books_by_titles__when_books_exist_in_dict__expected_empty_list(self):
        self.test_instance.filter_books_by_titles(vh.expected_file_contents)
        expected = 'http://test.url.com'
        actual = self.test_instance.filter_books_by_titles(vh.expected_file_contents)
        self.assertEqual(expected, actual)
