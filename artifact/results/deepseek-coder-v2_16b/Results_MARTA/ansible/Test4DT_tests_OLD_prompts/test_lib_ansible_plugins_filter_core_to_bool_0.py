
from ansible.plugins.filter.core import to_bool
import pytest
from unittest.mock import patch


@patch('ansible.plugins.filter.core.to_bool')
def test_to_bool_with_truthy_string(mock_to_bool):
    mock_to_bool.return_value = True
    # Test with a string that is truthy according to the conversion rules
    assert to_bool('Yes') == True
    assert to_bool('on') == True
    assert to_bool('1') == True
    assert to_bool('true') == True

@patch('ansible.plugins.filter.core.to_bool')
def test_to_bool_with_falsy_string(mock_to_bool):
    mock_to_bool.return_value = False
    # Test with a string that is falsy according to the conversion rules
    assert to_bool('off') == False
    assert to_bool('0') == False
    assert to_bool('false') == False


@patch('ansible.plugins.filter.core.to_bool')
def test_to_bool_with_falsy_value(mock_to_bool):
    mock_to_bool.return_value = False
    # Test with a falsy value that is not a string
    assert to_bool(0) == False
    assert to_bool('') == False
    assert to_bool([]) == False
    assert to_bool({}) == False