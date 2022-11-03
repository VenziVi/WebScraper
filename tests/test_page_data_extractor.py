from data_extraction.extractors.page_data_extractor import PageDataExtractor
import unittest
import variables_helper as vh
import itertools


class PageDataExtractorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        vh.SoupFromFiles().files_creator()
        cls.home_page = PageDataExtractor(
            vh.SoupFromFiles.open_and_parse_files_to_make_soup('/Bookswebpage.html'))

        cls.book_page = PageDataExtractor(
            vh.SoupFromFiles.open_and_parse_files_to_make_soup('/Bookpage.html'))

        cls.category = PageDataExtractor(
            vh.SoupFromFiles.open_and_parse_files_to_make_soup(
                '/CurrentCategoryWebpage.html'))

    def test_html_text_setter__when_value_is_none__expected_raise_error(self):
        with self.assertRaises(ValueError):
            self.home_page.html_text = None

    def test_html_text_setter__when_value_is_valid__expected_success(self):
        expected = vh.SoupFromFiles.open_and_parse_files_to_make_soup('/Bookswebpage.html')
        actual = self.home_page.html_text
        self.assertEqual(actual, expected)

    def test_get_books_per_page__with_correct_website_given__expected_success(self):
        expected = 20
        actual = self.home_page.get_books_per_page()
        self.assertEqual(actual, expected)

    def test_get_books_per_page__with_wrong_website_given__expected_return_1(self):
        expected = 1
        actual = self.book_page.get_books_per_page()
        self.assertEqual(actual, expected)

    def test_get_books_per_page__when_there_is_no_range_of_books__expected_success(
        self):
        expected = 11
        actual = self.category.get_books_per_page()
        self.assertEqual(actual, expected)

    def test_get_books_categories__with_valid_input__expected_success(self):
        expected = vh.expected_book_categories
        actual = self.home_page.get_books_categories()
        self.assertEqual(actual, expected)

    def test_books_urls_generator__when_there_is_a_limit_according_to_amount_of_needed_books__expected_success(self):
        actual = len(list(self.home_page.books_urls_generator(5)))
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_books_per_page__when_scraping_from_main_page__expected_success(
        self):
        expected = 20
        actual = self.home_page.get_books_per_page()
        self.assertEqual(expected, actual)

    def test_get_next_page__when_next_page_tag_is_present__expected_success(self):
        expected = 'catalogue/page-2.html'
        actual = self.home_page.get_next_page()
        self.assertEqual(expected, actual)

    def test_get_next_page__when_next_page_tag_is_missing_and_returns_none__expected_success(self):
        expected = None
        actual = self.category.get_next_page()
        self.assertEqual(expected, actual)

    def test_get_titles_from_collection_page__when_correct_page_is_given__expected_success(self):
        number_of_titles = 10
        actual = self.home_page.get_titles_from_collection_page(number_of_titles)
        expected = dict(itertools.islice(vh.expected_dict_of_titles.items(), number_of_titles))
        self.assertEqual(expected, actual)

    def test_get_titles_from_collection_page__when_wrong_page_is_given__expected_index_error(self):
        expected = None
        actual = self.book_page.get_titles_from_collection_page(3)
        self.assertEqual(expected, actual)
