
import pytest
from ansible.plugins.filter.core import path_join
from ansible.errors import AnsibleFilterTypeError
from unittest.mock import patch, MagicMock

# Test scenario 1: test_valid_case_single_string
def test_valid_case_single_string():
    with patch('ansible.plugins.filter.core.os') as mock_os:
        mock_os.path.join = MagicMock(return_value='foo')
        result = path_join("foo")
        assert result == 'foo'
        mock_os.path.join.assert_called_once_with('foo')

# Test scenario 2: test_valid_case_sequence_of_strings
def test_valid_case_sequence_of_strings():
    with patch('ansible.plugins.filter.core.os') as mock_os:
        mock_os.path.join = MagicMock(return_value='foo/bar')
        result = path_join(["foo", "bar"])
        assert result == 'foo/bar'
        mock_os.path.join.assert_called_once_with('foo', 'bar')

# Test scenario 3: test_invalid_type
def test_invalid_type():
    with pytest.raises(AnsibleFilterTypeError):
        path_join(42)
