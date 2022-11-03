import unittest
from data_extraction.url_collector import UrlCollector
import variables_helper as vh


class TestUrlCollector(unittest.TestCase):
    def setUp(self):
        self.url_collector = UrlCollector(vh.base_url)

    def test__books_dict__returns_empty_book_dict__success(self):
        expected = {}
        actual = self.url_collector.books_dict
        self.assertEqual(expected, actual)

    def test__get_all_genres__expected_list_with_all_genres__success(self):
        expected = [u'young adult', u'art', u'childrens', u'paranormal', u'fantasy', u'suspense', u'nonfiction', u'politics', u'crime', u'biography', u'womens fiction', u'autobiography', u'humor', u'psychology', u'spirituality', u'travel', u'novels', u'poetry', u'fiction', u'romance', u'religion', u'add a comment', u'music', u'health', u'self help', u'christian', u'business', u'food and drink', u'horror', u'philosophy', u'contemporary', u'christian fiction', u'parenting', u'cultural', u'historical fiction', u'erotica', u'thriller', u'mystery', u'classics', u'sports and games', u'default', u'science', u'sequential art', u'science fiction', u'academic', u'adult fiction', u'historical', u'new adult', u'short stories', u'history']
        actual = self.url_collector.get_all_genres()
        self.assertEqual(expected, actual)

    def test__collect_books_urls__receive_all_book_urls__success(self):
        expected = vh.expected_book_urls
        actual = self.url_collector.collect_books_urls()
        self.assertEqual(expected, actual)


