from data_extraction.extractors.book_data_extractor import BookDataExtractor
import unittest
import variables_helper as vh


class BookDataExtractorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        vh.SoupFromFiles().files_creator()

    def setUp(self):
        self.home_page = BookDataExtractor(
            vh.SoupFromFiles.open_and_parse_files_to_make_soup('/Bookswebpage.html'))

        self.book_page = BookDataExtractor(
            vh.SoupFromFiles.open_and_parse_files_to_make_soup('/Bookpage.html'))

        self.category = BookDataExtractor(
            vh.SoupFromFiles.open_and_parse_files_to_make_soup(
                '/CurrentCategoryWebpage.html'))

    def test_get_upc__when_upc_length_is_correct__expected_success(self):
        expected = 16
        actual = len(self.book_page.get_upc())
        self.assertEqual(expected, actual)

    def test_get_upc__when_wrong_webpage_is_given__expected_fail(self):
        expected = None
        actual = self.home_page.get_upc()
        self.assertEqual(expected, actual)

    def test_html_text__when_wrong_data_is_passed__expected_value_error(self):
        with self.assertRaises(ValueError):
            self.home_page.html_text = None

    #  get_title
    def test_get_title__when_correct_webpage_is_given__expected_success(self):
        expected = 'A Light in the Attic'
        actual = self.book_page.get_title()
        self.assertEqual(expected, actual)

    def test_get_title__when_wrong_webpage_is_given__expected_fail(self):
        expected = 'A Light in the Attic'
        actual = self.category.get_title()
        self.assertNotEqual(expected, actual)

    def test_get_genre__when_correct_webpage_is_given__expected_success(self):
        expected = 'Poetry'
        actual = self.book_page.get_genre()
        self.assertEqual(expected, actual)

    def test_get_genre__when_wrong_webpage_is_given__expected_fail(self):
        expected = 'Poetry'
        actual = self.home_page.get_genre()
        self.assertNotEqual(expected, actual)

    #  get_product_type
    def test_get_product_type__when_correct_webpage_is_given__expected_success(self):
        expected = 'Books'
        actual = self.book_page.get_product_type()
        self.assertEqual(expected, actual)

    def test_get_product_type__when_wrong_webpage_is_given__expected_index_error_and_return_none(self):
        expected = None
        actual = self.home_page.get_product_type()
        self.assertEqual(expected, actual)

    #  get_price_incl_tax
    def test_get_price_incl_tax__when_correct_book_page_is_given__expected_success(self):
        expected = 51.77
        actual = self.book_page.get_price_incl_tax()
        self.assertEqual(expected, actual)

    def test_get_price_incl_tax__when_wrong_page_is_given__expected_return_0(self):
        expected = 0.0
        actual = self.category.get_price_incl_tax()
        self.assertEqual(expected, actual)

    def test_get_price_incl_tax__when_price_is_none__expected_index_error_return_0_0(self):
        actual = self.home_page.get_price_incl_tax()
        expected = 0.0
        self.assertEqual(expected, actual)

    #  get_price_excl_tax
    def test_get_price_excl_tax__when_correct_webpage_is_given__expected_success(self):
        expected = 51.77
        actual = self.book_page.get_price_excl_tax()
        self.assertEqual(expected, actual)

    def test_get_price_excl_tax__when_wrong_webpage_is_given__expected_index_error_return_0_0(self):
        expected = 0.0
        actual = self.home_page.get_price_excl_tax()
        self.assertEqual(expected, actual)

    #  get_tax
    def test_get_tax__when_correct_webpage_is_given__expected_success(self):
        expected = 0.0
        actual = self.book_page.get_tax()
        self.assertEqual(expected, actual)

    def test_get_tax__when_wrong_webpage_is_given_expected_return_none(self):
        expected = 0.0
        actual = self.home_page.get_tax()
        self.assertEqual(expected, actual)

    #  get_quantity
    def test_get_quantity__when_correct_webpage_is_given__expected_success(self):
        expected = 22
        actual = self.book_page.get_quantity()
        self.assertEqual(expected, actual)

    def test_get_quantity__when_wrong_webpage_is_given__expected_index_error_and_return_0_0(self):
        expected = None
        actual = self.home_page.get_quantity()
        self.assertEqual(expected, actual)

    #  get_rating
    def test_get_rating__when_correct_webpage_is_given__expected_success(self):
        expected = 3
        actual = self.book_page.get_rating()
        self.assertEqual(expected, actual)

    #  get_description
    def test_get_description__when_correct_webpage_is_given__expected_success(self):
        expected = vh.expected_book_description
        actual = self.book_page.get_description()
        self.assertEqual(expected, actual)

    def test_get_description_fail(self):
        expected = None
        actual = self.home_page.get_description()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
