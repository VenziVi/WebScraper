from data_storage.sorting import SortingMixin
import variables_helper as vh
import unittest


class TestSortings(unittest.TestCase):
    correct_website = ''
    wrong_websit = ''
    wrong_book_page = ''

    @classmethod
    def setUpClass(cls):
        cls.sorting_upc_ascending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['upc', 'ascending']])
        cls.sorting_title_ascending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['default', 'ascending']])
        cls.sorting_by_rating_ascending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['rating', 'ascending']])
        cls.sorting_by_genre_ascending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['genre', 'ascending']])
        cls.sorting_by_quantity_ascending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['quantity', 'ascending']])
        cls.sorting_by_price_ascending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['price', 'ascending']])

        cls.sorting_upc_descending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['upc', 'descending']])
        cls.sorting_title_descending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['default', 'descending']])
        cls.sorting_by_rating_descending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['rating', 'descending']])
        cls.sorting_by_genre_descending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['genre', 'descending']])
        cls.sorting_by_quantity_descending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['quantity', 'descending']])
        cls.sorting_by_price_descending = SortingMixin.any_sort(vh.dict_to_test_sortings, [['price', 'descending']])

        cls.sorting_by_missing_key_value = SortingMixin.any_sort(vh.dict_to_test_sortings, [['writer', 'ascending']])

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_upc_key_ascending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[0])
        actual = self.sorting_upc_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_upc_key_descending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[0], reverse=True)
        actual = self.sorting_upc_descending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_rating_key_ascending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Rating'])
        actual = self.sorting_by_rating_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_rating_key_descending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Rating'], reverse=True)
        actual = self.sorting_by_rating_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_title_key_ascending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Title'])
        actual = self.sorting_title_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_title_key_descending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Title'], reverse=True)
        actual = self.sorting_title_descending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_genre_key_ascending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Genre'])
        actual = self.sorting_by_genre_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_genre_key_descending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Genre'], reverse=True)
        actual = self.sorting_by_genre_descending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_quantity_key_ascending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Quantity'])
        actual = self.sorting_by_quantity_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_quantity_key_descending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Quantity'], reverse=True)
        actual = self.sorting_by_quantity_descending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_price_key_ascending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Price_incl_tax'])
        actual = self.sorting_by_price_ascending
        self.assertEqual(expected, actual)

    def test__any_sort__when_correct_dict_key_is_passed_to_sort_by_price_key_descending__expected_success(self):
        expected = sorted(vh.dict_to_test_sortings.items(), key=lambda item: item[1]['Price_incl_tax'], reverse=True)
        actual = self.sorting_by_price_descending
        self.assertEqual(expected, actual)

    def test__any_sort__when_wrong_dict_key_is_passed_to_sort_by_rating_key_ascending__expected_none(self):
        expected = None
        actual = self.sorting_by_missing_key_value
        self.assertEqual(expected, actual)

