import unittest
import variables_helper as vh


class BookTest(unittest.TestCase):
    def setUp(self):
        self.book = vh.create_book_class_instance()

    #  upc - setter
    def test_upc__when_correct_length_upc_is_given__expected_success(self):
        expected = 'a897fe39b1053632'
        self.book.upc = expected
        actual = self.book.upc
        self.assertEqual(expected, actual)

    def test_upc__when_wrong_length_is_given__expected_value_error(self):
        expected = ValueError
        with self.assertRaises(expected):
            self.book.upc = 'a897fe39b105363'

    #  title - setter
    def test_title__when_correct_title_is_given__expected_success(self):
        expected = 'A Light in the Attic'
        self.book.title = expected
        actual = self.book.title
        self.assertEqual(expected, actual)

    def test_title__when_wrong_title_is_given_expected_none(self):
        expected = ValueError
        actual = None
        with self.assertRaises(expected):
            self.book.title = actual

    #  genre - setter
    def test_genre__when_correct_genre_is_given__expected_success(self):
        expected = 'Poetry'
        self.book.genre = expected
        actual = self.book.genre
        self.assertEqual(expected, actual)

    def test_genre__when_wrong_title_is_given__expected_value_error(self):
        expected = ValueError
        actual = None
        with self.assertRaises(expected):
            self.book.genre = actual

    #  product_type - setter
    def test_product_type__when_correct_type_is_given__expected_success(self):
        expected = 'Books'
        self.book.product_type = expected
        actual = self.book.product_type
        self.assertEqual(expected, actual)

    def test_product_type__when_wrong_type_is_given__expected_value_error(self):
        expected = ValueError
        actual = 'Newspapers'
        with self.assertRaises(expected):
            self.book.product_type = actual

    #  price_with_tax - setter
    def test_price_with_tax__when_correct_price_is_given__expected_success(self):
        expected = 51.77
        self.book.price_with_tax = expected
        actual = self.book.price_with_tax
        self.assertEqual(expected, actual)

    def test_price_with_tax__when_wrong_value_is_given__expected_string(self):
        current_value = None
        self.book.price_with_tax = current_value
        expected = 'N\A'
        actual = self.book.price_with_tax
        self.assertEqual(expected, actual)

    #  price_excl_tax - setter
    def test_price_excl__when_correct_price_is_given__expected_success(self):
        expected = 51.77
        self.book.price_excl_tax = expected
        actual = self.book.price_excl_tax
        self.assertEqual(expected, actual)

    def test_price_excl_tax__when_wrong_value_is_given__expected_string(self):
        current_value = None
        self.book.price_excl_tax = current_value
        expected = 'N\A'
        actual = self.book.price_excl_tax
        self.assertEqual(expected, actual)

    #  tax - setter
    def test_tax__when_correct_value_is_given__expected_success(self):
        expected = 0.0
        self.book.tax = expected
        actual = self.book.tax
        self.assertEqual(expected, actual)

    def test_tax__when_negative_value_is_given__expected_value_error(self):
        expected = -1
        with self.assertRaises(ValueError):
            self.book.tax = expected

    #  qty - setter
    def test_qty__when_correct_value_is_given__expected_success(self):
        expected = 10
        self.book.qty = expected
        actual = self.book.qty
        self.assertEqual(expected, actual)

    def test_qty__when_negative_value_is_give__expected_value_error(self):
        expected = -1
        with self.assertRaises(ValueError):
            self.book.qty = expected

    #  rating - setter
    def test_rating__when_correct_value_is_given__expected_success(self):
        expected = 3
        self.book.rating = expected
        actual = self.book.rating
        self.assertEqual(expected, actual)

    def test_rating___when_negative_value_is_given__expected_value_error(self):
        expected = -1
        with self.assertRaises(ValueError):
            self.book.rating = expected

    #   description - setter
    def test_description__when_correct_description_is_given__expected_success(self):
        expected = vh.expected_book_description
        self.book.description = expected
        actual = self.book.description
        self.assertEqual(expected, actual)

    def test_description__when_wrong_description_is_given__expected_string(self):
        current_value = None
        self.book.description = current_value
        expected = 'N\A'
        actual = self.book.description
        self.assertEqual(expected, actual)

    def test_description__when_a_number_insted_of_a_description_is_given__expected_string(self):
        current_value = 3
        self.book.description = current_value
        expected = 'N\A'
        actual = self.book.description
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
