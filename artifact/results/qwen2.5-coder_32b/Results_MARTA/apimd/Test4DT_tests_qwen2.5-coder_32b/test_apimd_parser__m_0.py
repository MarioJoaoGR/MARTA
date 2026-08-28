
import pytest
from apimd.parser import _m

def test_valid_input_two_parts():
    """Test valid input with two parts."""
    result = _m('package', 'submodule')
    assert result == 'package.submodule'

def test_valid_input_with_empty_string():
    """Test valid input with an empty string in the arguments."""
    result = _m('my_module', '', 'function')
    assert result == 'my_module.function'

def test_valid_input_multiple_parts():
    """Test valid input with multiple parts."""
    result = _m('root', 'level1', 'level2')
    assert result == 'root.level1.level2'

def test_single_part_module_name():
    """Test single part module name."""
    result = _m('single_module')
    assert result == 'single_module'

def test_no_parts_provided():
    """Test no parts provided (edge case)."""
    result = _m('', '', '')
    assert result == ''

def test_mixed_usage_with_dynamic_values():
    """Test mixed usage with dynamic values."""
    parts = ['app', 'services', 'user']
    result = _m(*parts)
    assert result == 'app.services.user'


def test_invalid_inputs_non_string_arguments():
    """Test invalid inputs/Error handling for non-string arguments."""
    with pytest.raises(TypeError):
        _m('package', 123)

def test_invalid_inputs_all_empty_strings():
    """Test invalid inputs with all empty strings."""
    result = _m('', '', '')
    assert result == ''