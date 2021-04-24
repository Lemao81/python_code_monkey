from unittest import TestCase
from cyclic_shift import validate_binary_string


class VariousTests(TestCase):
    def test_validate_binary_string_valid_binary(self):
        # act + assert
        validate_binary_string("110010101", 9)

    def test_validate_binary_string_invalid_binary(self):
        # act + assert
        with self.assertRaises(SystemExit):
            validate_binary_string("20101001101", 11)

    def test_validate_binary_string_valid_binary_wrong_length(self):
        # act + assert
        with self.assertRaises(SystemExit):
            validate_binary_string("10101001101", 12)
