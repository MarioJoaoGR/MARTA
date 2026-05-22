
import argparse
from unittest import TestCase, mock
from httpie.cli.argtypes import KeyValueArgType

class TestKeyValueArgType(TestCase):
    def setUp(self):
        self.key_value_parser = KeyValueArgType()

    @mock.patch('httpie.cli.argtypes.Escaped', autospec=True)
    def test_escaped_characters(self, MockEscaped):
        with mock.patch('httpie.cli.argtypes.KeyValueArgType.__call__', return_value='expected'):
            result = self.key_value_parser(r'foo\=bar')
            self.assertEqual(result, 'expected')
