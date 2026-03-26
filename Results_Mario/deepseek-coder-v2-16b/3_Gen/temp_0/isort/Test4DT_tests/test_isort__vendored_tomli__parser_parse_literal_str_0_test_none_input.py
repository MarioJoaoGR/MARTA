
import unittest

from isort._vendored.tomli._parser import parse_literal_str


class TestParseLiteralStr(unittest.TestCase):
    def test_none_input(self):
        # Test when src is an empty string, which means no input provided
        with self.assertRaises(ValueError):
            parse_literal_str("", 0)

if __name__ == "__main__":
    unittest.main()
