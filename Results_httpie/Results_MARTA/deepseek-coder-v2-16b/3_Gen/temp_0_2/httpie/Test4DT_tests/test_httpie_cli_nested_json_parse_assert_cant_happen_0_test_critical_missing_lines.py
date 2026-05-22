
import unittest.mock as mock
from httpie.cli.nested_json.parse import assert_cant_happen

def test_critical_missing_lines():
    with mock.patch('httpie.cli.nested_json.parse.assert_cant_happen') as mock_assert:
        try:
            assert_cant_happen()
        except ValueError as e:
            assert str(e) == 'Unexpected value'
