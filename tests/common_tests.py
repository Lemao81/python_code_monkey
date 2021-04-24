from unittest.mock import patch
from unittest import TestCase
from common import prompt_multiple_numeric_input, right_shift_string_extended, right_shift_string, left_shift_string, get_next_rotating_index


class CommonTests(TestCase):
    @patch('common.get_input', return_value='2 6 3')
    def test_prompt_multiple_numeric_input__single_bound__in_range(self):
        # act
        result = prompt_multiple_numeric_input(3, [(1, 10)])

        # assert
        self.assertEqual(3, len(result))
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 6)
        self.assertEqual(result[2], 3)

    @patch('common.get_input', return_value='2 12 3')
    def test_prompt_multiple_numeric_input__single_bound__out_of_range(self):
        # act + assert
        with self.assertRaises(SystemExit):
            prompt_multiple_numeric_input(3, [(1, 10)])

    @patch('common.get_input', return_value='8 15')
    def test_prompt_multiple_numeric_input__multiple_bound__valid_bound_amount(self):
        # act
        result = prompt_multiple_numeric_input(2, [(1, 10), (3, 20)])

        # assert
        self.assertEqual(2, len(result))
        self.assertEqual(result[0], 8)
        self.assertEqual(result[1], 15)

    @patch('common.get_input', return_value='8 15')
    def test_prompt_multiple_numeric_input__multiple_bound__invalid_bound_amount(self):
        # act + assert
        with self.assertRaises(SystemExit):
            prompt_multiple_numeric_input(2, [(1, 10), (3, 20), (2, 8)])

    def test_right_shift_string_extended(self):
        # act
        result = right_shift_string_extended('11010100')

        # assert
        self.assertEqual('01101010', result)

    def test_right_shift_string(self):
        # act
        result = right_shift_string('0110101011')

        # assert
        self.assertEqual('1011010101', result)

    def test_left_shift_string(self):
        # act
        result = left_shift_string('0110101011')

        # assert
        self.assertEqual('1101010110', result)

    def test_get_next_rotating_index__inside_array(self):
        # act
        result = get_next_rotating_index(3, [1, 2, 3, 4, 5, 6])

        # assert
        self.assertEqual(4, result)

    def test_get_next_rotating_index__end_of_array(self):
        # act
        result = get_next_rotating_index(5, [1, 2, 3, 4, 5, 6])

        # assert
        self.assertEqual(0, result)
