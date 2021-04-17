from unittest.mock import patch
from unittest import TestCase
from common import prompt_multiple_numeric_input


class CommonTests(TestCase):
    @patch('common.get_input', return_value='2 6 3')
    def test_prompt_multiple_numeric_input__single_bound__in_range(self, input):
        # act
        result = prompt_multiple_numeric_input(3, [(1, 10)])

        # assert
        self.assertEqual(3, len(result))
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 6)
        self.assertEqual(result[2], 3)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)

    @patch('common.get_input', return_value='2 12 3')
    def test_prompt_multiple_numeric_input__single_bound__out_of_range(self, input):
        # act + assert
        with self.assertRaises(SystemExit):
            prompt_multiple_numeric_input(3, [(1, 10)])

    @patch('common.get_input', return_value='8 15')
    def test_prompt_multiple_numeric_input__multiple_bound__valid_bound_amount(self, input):
        # act
        result = prompt_multiple_numeric_input(2, [(1, 10), (3, 20)])

        # assert
        self.assertEqual(2, len(result))
        self.assertEqual(result[0], 8)
        self.assertEqual(result[1], 15)

    @patch('common.get_input', return_value='8 15')
    def test_prompt_multiple_numeric_input__multiple_bound__invalid_bound_amount(self, input):
        # act + assert
        with self.assertRaises(SystemExit):
            prompt_multiple_numeric_input(2, [(1, 10), (3, 20), (2, 8)])
