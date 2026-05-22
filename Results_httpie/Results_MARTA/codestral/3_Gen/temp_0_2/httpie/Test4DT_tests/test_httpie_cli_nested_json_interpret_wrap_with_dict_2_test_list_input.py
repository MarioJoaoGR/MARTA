
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.nested_json.interpret import NestedJSONArray
from httpie.cli.nested_json.interpret import wrap_with_dict

def test_wrap_with_dict_list():
    with patch('httpie.cli.nested_json.interpret.NestedJSONArray', autospec=True) as mock_nested_json:
        mock_nested_json.return_value = NestedJSONArray([1, 2, 3])
        result = wrap_with_dict([1, 2, 3])
        assert result == {'' : mock_nested_json.return_value}
        mock_nested_json.assert_called_once_with([1, 2, 3])
